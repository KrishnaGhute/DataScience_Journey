# 🗺️ California Housing Price Prediction & Spatial Analysis Engine

An interactive, production-ready full-stack web application that leverages an optimized **XGBoost Regressor** to predict California real estate valuations in real time based on geographic coordinates and demographic attributes. The interface features a fluid, continuous geospatial map layer built to analyze market dynamics seamlessly.

---

## 🚀 Live Demo & Visuals

### 🖥️ Interactive Web Application Interface
<img src="https://raw.githubusercontent.com/KrishnaGhute/DataScience_Journey/main/California_Housing_Deployment/image/Screenshot%202026-06-04%20100344.png" alt="California Housing Dashboard" width="600">
---

## 📊 Core Architecture & Features

1. **Precision ML Engine:** Powered by an `XGBoost Regressor` achieving an **$R^2$ Score of 72.4%** and a remarkably low **Mean Absolute Error (MAE) of \$15,838.62**.
2. **Robust Multi-Tier Pipeline:** Data transformation pipelines utilize an absolute column-mapped `StandardScaler` backed by a pandas structural data frame to prevent feature misalignment.
3. **Dynamic Baseline Land Valuator:** Implements a custom spatial economic proximity engine. If a user hovers over empty terrains or unbuilt parcels where property markers scale below zero, the system automatically runs Euclidean calculations against major California economic hubs (SF & LA) to generate an accurate raw land asset valuation.
4. **Advanced Geospatial Analysis Layers:** Contains advanced notebook visualizations translating individual points into structural market trend surfaces.

> ### ⬢ Geospatial Price Surface Density & Hexagonal Binning
> ![Geospatial Analysis Layers](path_to_your_screenshot/geospatial_layers.png)
> *Placeholder: Replace the path above with a screenshot of your interactive Plotly Hexbin or Density Map layers.*

---

## 📂 Project Directory Layout

```text
California_Housing_Deployment/
├── app.py                  # Main Flask backend controller with custom valuation logic
├── model.pkl               # Serialized production XGBoost Regressor artifact
├── scaler.pkl              # Serialized Scikit-Learn preprocessing pipeline
├── Procfile                # Production-grade web server WSGI configuration
├── requirements.txt        # Frozen environmental dependency tracking list
├── README.md               # Complete repository documentation
└── templates/
    └── index.html          # Interactive UI frontend incorporating Leaflet maps
