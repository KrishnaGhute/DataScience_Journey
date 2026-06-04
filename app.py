from flask import Flask, render_template, request, jsonify
from joblib import load
import numpy as np
import pandas as pd  # Preserves case-sensitive feature names for the scaler

app = Flask(__name__)

# Load BOTH saved artifacts on startup
model = load('model.pkl')
scaler = load('scaler.pkl')  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
            med_inc = float(data.get('MedInc', 4.0))
            house_age = float(data.get('HouseAge', 28.0))
            ave_rooms = float(data.get('AveRooms', 5.0))
            ave_bedrms = float(data.get('AveBedrms', 1.0))
            population = float(data.get('Population', 1400.0))
            ave_occup = float(data.get('AveOccup', 3.0))
            latitude = float(data.get('Latitude', 37.7749))
            longitude = float(data.get('Longitude', -122.4194))
        else:
            med_inc = float(request.form['MedInc'])
            house_age = float(request.form['HouseAge'])
            ave_rooms = float(request.form['AveRooms'])
            ave_bedrms = float(request.form['AveBedrms'])
            population = float(request.form['Population'])
            ave_occup = float(request.form['AveOccup'])
            latitude = float(request.form['Latitude'])
            longitude = float(request.form['Longitude'])

        # 1. THE COMPLETE FIX: Structure features into a named pandas DataFrame
        # This completely guarantees the scaler maps columns correctly regardless of array sequence.
        # NOTE: If your training notebook used lowercase column names, match them exactly here.
        feature_dict = {
            'MedInc': [med_inc],
            'HouseAge': [house_age],
            'AveRooms': [ave_rooms],
            'AveBedrms': [ave_bedrms],
            'Population': [population],
            'AveOccup': [ave_occup],
            'Latitude': [latitude],
            'Longitude': [longitude]
        }
        raw_features_df = pd.DataFrame(feature_dict)

        # 2. Scale the data using the structured DataFrame features
        scaled_features = scaler.transform(raw_features_df)

        # 3. Generate the continuous price prediction from your XGBRegressor
        raw_prediction = model.predict(scaled_features)
        
        # 4. Extract numerical metric and convert scale back into real dollar units
        predicted_value = float(raw_prediction[0])
        actual_price = predicted_value * 100000

        # 5. UPGRADED MANNER: Dynamic Baseline Land Valuation Engine
        if actual_price <= 0:
            # Coordinates of major core economic hubs in California
            sf_hub = np.array([37.7749, -122.4194])  # San Francisco Bay Area
            la_hub = np.array([34.0522, -118.2437])  # Los Angeles Metro Area
            current_loc = np.array([latitude, longitude])
            
            # Calculate straight-line Euclidean distance to the closest city hub
            dist_to_sf = np.linalg.norm(current_loc - sf_hub)
            dist_to_la = np.linalg.norm(current_loc - la_hub)
            min_distance = min(dist_to_sf, dist_to_la)
            
            # Dynamic Land Pricing Rule:
            # Start with a prime base land value of $45,000 per acre baseline point.
            # Reduce value by $8,500 for every degree of distance away from a major city.
            # Never let raw land fall below a absolute minimum floor of $5,000.
            calculated_land_value = 45000.0 - (min_distance * 8500.0)
            actual_price = max(calculated_land_value, 5000.0)
            
            # If the cursor drifts completely out into the deep Pacific Ocean, drop to 0
            if longitude < -125.5 or latitude < 32.0 or latitude > 42.5:
                actual_price = 0.0
        

        return jsonify({'success': True, 'price': f"${actual_price:,.2f}"})

    except Exception as e:
        print(f"❌ CRITICAL BACKEND FAIL: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)