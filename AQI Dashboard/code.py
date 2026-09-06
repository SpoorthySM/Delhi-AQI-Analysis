import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Delhi AQI Dashboard", layout="wide")

# Title
st.title("🌫️ Delhi Air Quality Index (AQI) Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Data/delhiaqi.csv") # Make sure the path is correct
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.strftime('%B')
    df['year'] = df['date'].dt.year
    df['AQI'] = df['pm2_5']
    return df

df = load_data()

# Sidebar filters
pollutants = ['pm2_5', 'pm10', 'no', 'no2', 'nh3', 'co', 'so2', 'o3']
selected_pollutant = st.sidebar.selectbox("📌 Select Pollutant", pollutants)
selected_month = st.sidebar.selectbox("📅 Select Month", sorted(df['month'].unique()))

# 1️⃣ AQI over time
st.subheader(f"📈 {selected_pollutant.upper()} Over Time")
fig, ax = plt.subplots(figsize=(10, 4))
monthly_avg = df.groupby(['date'])[selected_pollutant].mean().rolling(7).mean()
ax.plot(monthly_avg, color='tab:blue')
ax.set_title(f"{selected_pollutant.upper()} Daily Avg (7-day rolling)")
ax.set_ylabel("µg/m³")
st.pyplot(fig)

# 2️⃣ Pollutant trend across months
st.subheader(f"📊 Monthly Average {selected_pollutant.upper()}")
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_trend = df.groupby('month')[selected_pollutant].mean().reindex(month_order)

fig2, ax2 = plt.subplots()
monthly_trend.plot(kind='bar', color='coral', ax=ax2)
ax2.set_ylabel("µg/m³")
ax2.set_title(f"Monthly Avg of {selected_pollutant.upper()}")
st.pyplot(fig2)

# 3️⃣ AQI Category coloring
st.subheader("🌈 AQI Category Heatmap")
aqi_bins = [0, 50, 100, 200, 300, 400, 500]
aqi_labels = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
df['AQI_Category'] = pd.cut(df['AQI'], bins=aqi_bins, labels=aqi_labels)

category_counts = df['AQI_Category'].value_counts().reindex(aqi_labels)

fig3, ax3 = plt.subplots()
category_counts.plot(kind='bar', color=['#50f5a5', '#9be67b', '#f2d43f', '#f29e3f', '#f25c3f', '#ff0000'], ax=ax3)
ax3.set_title("AQI Category Distribution")
st.pyplot(fig3)

# 4️⃣ Summary Insights
st.subheader("📋 Summary Insights")
col1, col2, col3 = st.columns(3)

with col1:
    worst_month = df.groupby('month')['AQI'].mean().idxmax()
    st.metric("🚨 Worst Month (AQI)", worst_month)
               
with col2:
    best_month = df.groupby('month')['AQI'].mean().idxmin()
    st.metric("🌿 Best Month (AQI)", best_month)

with col3:
    top_pollutants = df[pollutants].mean().sort_values(ascending=False).head(3)
    st.markdown("**Top 3 Pollutants:**")
    for i, (p, val) in enumerate(top_pollutants.items(), 1):
        st.markdown(f"{i}. {p.upper()} – {val:.2f} µg/m³")

# 5️⃣ Correlation heatmap
st.subheader("📌 Correlation Between Pollutants")
fig4, ax4 = plt.subplots(figsize=(10, 8))
sns.heatmap(df[pollutants].corr(), cmap='coolwarm', annot=True, fmt=".2f", ax=ax4)
ax4.set_title("Correlation Matrix")
st.pyplot(fig4)

# Footer
st.markdown("---")
