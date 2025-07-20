
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

from google.colab import files
uploaded = files.upload()  


df = pd.read_csv('delhiaqi.csv') 


df.head()
df.info()
df.describe()


df.isnull().sum()


df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.sort_values(by='date')
df = df.dropna(subset=['date'])


plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='date', y='AQI', marker='o', color='orange')
plt.title('Delhi AQI Over Time')
plt.xlabel('date')
plt.ylabel('Air Quality Index')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df['Month'] = df['date'].dt.month
monthly_avg = df.groupby('Month')['AQI'].mean()

plt.figure()
sns.barplot(x=monthly_avg.index, y=monthly_avg.values, palette='coolwarm')
plt.title('Average Monthly AQI in Delhi')
plt.xlabel('Month')
plt.ylabel('Average AQI')
plt.show()
