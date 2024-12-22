import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Step 1: Create the DataFrame with your data
data = {
    "Location": ["Stop #1 Lansdowne Park"] * 12,
    "Traffic Count": [61, 24, 11, 9, 17, 5, 28, 9, 1, 14, 25, 15],
    "Longitude": [-75.68580531, -75.68068081, -75.68610983, -75.68449478, 
                  -75.6796243, -75.68421071, -75.6780816, -75.67975324, 
                  -75.68355528, -75.68651711, -75.6783432, -75.67955396],
    "Latitude": [45.3987385, 45.39891803, 45.39938252, 45.39934569, 
                 45.3979209, 45.40008528, 45.4005321, 45.40002445, 
                 45.40011895, 45.39976627, 45.4016608, 45.40077915]
}

df = pd.DataFrame(data)

# Step 2: Create the map centered around the average latitude and longitude
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=15)

# Step 3: Create a MarkerCluster to group nearby markers
marker_cluster = MarkerCluster().add_to(m)

# Step 4: Add markers to the map with traffic count as popup and color coding based on traffic count
for idx, row in df.iterrows():
    traffic_count = row['Traffic Count']
    color = 'green' if traffic_count < 10 else 'orange' if traffic_count < 20 else 'red'  # Color based on traffic count
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Traffic Count: {traffic_count}",
        icon=folium.Icon(color=color)
    ).add_to(marker_cluster)

# Step 5: Add a custom legend for the map
legend_html = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 200px; height: 120px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 14px; font-family: Arial, sans-serif; padding: 10px;">
    <b>Traffic Count Legend</b><br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (0-10)<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (11-20)<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (21+)<br>
</div>
"""

# Add the legend to the map
m.get_root().html.add_child(folium.Element(legend_html))

# Step 6: Save the map to an HTML file
m.save('traffic_count_map_with_legend.html')

# Print a message to indicate that the map has been saved
print("Map has been saved as 'traffic_count_map_with_legend.html'.")
