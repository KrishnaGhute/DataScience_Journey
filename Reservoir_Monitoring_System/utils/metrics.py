# utils/metrics.py
import pandas as pd

def calculate_kpis(daily_records_list):
    """Calculates summary KPIs using the freshest log per dam."""
    if not daily_records_list:
        return {"total_storage": 0.0, "avg_pct": 0.0, "net_flow": 0.0}
        
    df = pd.DataFrame(daily_records_list)
    df['record_date'] = pd.to_datetime(df['record_date'])
    
    # Get the latest entry for each distinct dam
    latest_records = df.sort_values('record_date').groupby('dam_id').last()
    
    total_current_storage = latest_records['current_storage'].sum()
    avg_storage_percentage = latest_records['storage_pct'].mean()
    total_net_flow = latest_records['net_flow'].sum()
    
    return {
        "total_storage": round(total_current_storage, 2),
        "avg_pct": round(avg_storage_percentage, 1),
        "net_flow": round(total_net_flow, 2)
    }