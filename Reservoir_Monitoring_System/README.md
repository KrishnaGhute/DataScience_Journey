# 🌊 Reservoir Monitoring System

A professional web-based platform for monitoring, analyzing, and managing reservoir operations using interactive visualizations, geospatial mapping, and cloud-based data management.

---

## 📌 Overview

The Reservoir Monitoring System is designed to provide an intuitive interface for monitoring historical reservoir observations across South India.

The platform enables users to:

- Monitor reservoir storage
- Analyze historical trends
- Compare multiple reservoirs
- Visualize reservoirs on an interactive map
- Manage daily observations through a secure administrator portal

The application is developed using **Python**, **Streamlit**, **Supabase**, and **Plotly**, providing a modern cloud-based monitoring solution.

---

# ✨ Features

### 📊 Interactive Dashboard

- Live reservoir overview
- System KPIs
- Interactive GIS map
- Storage visualization
- Capacity utilization charts

---

### 🏞 Reservoir Analysis

- Historical storage analysis
- Water level trends
- Inflow & Outflow analysis
- Net flow monitoring
- Reservoir Inspection Report
- CSV export
- PDF report generation

---

### 🔄 Reservoir Comparison

- Multi-reservoir comparison
- Capacity utilization
- Storage comparison
- Water level comparison
- Inflow comparison
- Outflow comparison
- Summary statistics

---

### 🔐 Administrator Panel

- Secure administrator login
- Daily observation entry
- Bulk CSV upload
- Database management
- Dataset migration

---

### ℹ Additional Pages

- About
- Help
- User Guide

---

# 🛠 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Framework | Streamlit |
| Database | Supabase |
| Visualization | Plotly |
| Data Processing | Pandas, NumPy |
| Mapping | OpenStreetMap |

---

# 🗂 Dataset

Dataset Characteristics

- Region: South India
- Reservoirs: 19
- Daily Records: 55,500
- Observation Period: 2018–2025

Recorded Parameters

- Reservoir Storage
- Water Level
- Daily Inflow
- Daily Outflow
- Capacity Utilization
- Net Water Flow

---

# 📂 Project Structure

```text
Reservoir_Monitoring_System/

app.py

pages/

1_Dashboard.py

2_Dam_Analysis.py

3_Comparison.py

4_Admin_Login.py

5_About.py

6_Help.py

admin/

panel.py

utils/

database.py

map.py

plot_config.py

sidebar.py

footer.py

messages.py

assets/

logo.png

profile.jpg
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Reservoir_Monitoring_System.git
```

Move into the project

```bash
cd Reservoir_Monitoring_System
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configuration

Create Streamlit secrets:

```toml
SUPABASE_URL="YOUR_SUPABASE_URL"

SUPABASE_KEY="YOUR_SUPABASE_KEY"
```

---

# ▶ Running the Project

```bash
streamlit run app.py
```

---

# 📄 Application Pages

| Page | Description |
|------|-------------|
| Dashboard | System overview |
| Dam Analysis | Historical reservoir analysis |
| Comparison | Multi-reservoir comparison |
| Admin Login | Secure authentication |
| About | Project information |
| Help | User assistance |

---

# 🚀 Future Roadmap

Planned enhancements include:

- Machine Learning Forecasting
- Weather API Integration
- Flood Early Warning System
- Drought Prediction
- Satellite Data Integration
- Mobile Application

---

# 👨‍💻 Developer

## Krishna Ghute

**Data Science Professional**

Specialization:

- Data Science
- Machine Learning
- Geospatial Analytics
- Data Visualization

---

# 📜 License

This project is intended for educational, research, and demonstration purposes.