import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# Data (replace with actual data)
data = {
    'Location': ['Lansdowne Park', 'Elgin Street', 'ByWard Market'],
    'Vegetation Index': [0.7, 0.4, 0.6],  # Example vegetation index scores
    'EQI': [80, 60, 75],  # Example EQI scores
    'Pedestrian Count': [200, 300, 150]  # Example pedestrian counts
}
df = pd.DataFrame(data)

# Scatter plots
plt.figure(figsize=(12, 6))

# Vegetation Index vs Pedestrian Count
plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='Vegetation Index', y='Pedestrian Count', hue='Location', s=100)
plt.title('Vegetation Index vs Pedestrian Count')
plt.xlabel('Vegetation Index')
plt.ylabel('Pedestrian Count')

# EQI vs Pedestrian Count
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='EQI', y='Pedestrian Count', hue='Location', s=100)
plt.title('EQI vs Pedestrian Count')
plt.xlabel('EQI')
plt.ylabel('Pedestrian Count')

plt.tight_layout()
plt.show()
