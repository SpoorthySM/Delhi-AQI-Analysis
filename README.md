# Delhi AQI Analysis Dashboard 🌫️

An interactive air quality analysis dashboard built with Python and Streamlit, 
analysing Delhi's pollution data across 8 pollutants with multi-filter 
visualisations and anomaly detection.

🔗 **Live Demo:** https://delhi-aqi-analysis.streamlit.app/

---

## What it does

- Explores Delhi air quality data across **8 pollutants** including PM2.5, 
  PM10, NO2, SO2, CO, O3, NH3, and NOx
- Identifies statistically significant pollution spikes using 
  **Isolation Forest anomaly detection** (Scikit-learn)
- Provides **seasonal trend analysis** and temporal pollutant variation
- Sidebar filters let users drill down by pollutant, season, and category
- Category-based colour mapping for intuitive AQI level interpretation

---

## Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Dashboard | Streamlit |
| Visualisation | Plotly, Matplotlib, Seaborn |
| Data Processing | Pandas, NumPy |
| ML | Scikit-learn (Isolation Forest) |

---

## Project Structure
Delhi-AQI-Analysis/
├── AQI Dashboard/
│ ├── code.py # Main Streamlit dashboard
│ └── requirements.txt
├── Data/
│ └── delhiaqi.csv # Delhi air quality dataset (562 records)
├── Notebook/ # EDA notebooks and analysis scripts
├── Visuals/ # Saved plots and charts
└── requirements.txt

## Key Findings

- **PM2.5** identified as the primary pollutant driving AQI spikes in Delhi
- Clear **seasonal patterns** observed — winter months show significantly 
  higher pollution levels
- Anomaly detection flagged statistically significant pollution events 
  across multiple pollutant categories
- Strong correlation between PM2.5 and PM10 levels across all seasons

---

## Run Locally

```bash
git clone https://github.com/SpoorthySM/Delhi-AQI-Analysis.git
cd Delhi-AQI-Analysis
pip install -r requirements.txt
streamlit run "AQI Dashboard/code.py"
```

---

## Built By

**Spoorthy Sree Mundarinti** — B.Tech CSE (Data Science Minor), MGIT  
Built during Data Science Internship at Shadowfox, Hyderabad (Jul–Aug 2025)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/spoorthysree)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black)](https://github.com/SpoorthySM)
