import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Traffic data
traffic_data = {
    "Location": ["Stop #1 Lansdowne Park"] * 12,
    "Count": [61, 24, 11, 9, 17, 5, 28, 9, 1, 14, 25, 15],
    "Longitude": [-75.68580531, -75.68068081, -75.68610983, -75.68449478, 
                  -75.6796243, -75.68421071, -75.6780816, -75.67975324, 
                  -75.68355528, -75.68651711, -75.6783432, -75.67955396],
    "Latitude": [45.3987385, 45.39891803, 45.39938252, 45.39934569, 
                 45.3979209, 45.40008528, 45.4005321, 45.40002445, 
                 45.40011895, 45.39976627, 45.4016608, 45.40077915],
    "Type": ["Traffic"] * 12
}

# Pedestrian data
pedestrian_data = {
    "Location": ["Stop #1 Lansdowne Park"] * 12,
    "Count": [5, 14, 4, 6, 3, 3, 6, 2, 7, 2, 4, 18],
    "Longitude": [-75.68570327, -75.68608501, -75.68573379, -75.685212, 
                  -75.68517646, -75.67992822, -75.68485444, -75.68461947, 
                  -75.68473223, -75.68447114, -75.68381162, -75.6856984],
    "Latitude": [45.3994541, 45.39946985, 45.39958372, 45.400013, 
                 45.39968338, 45.39987131, 45.3999348, 45.40002635, 
                 45.39998241, 45.40001867, 45.40034716, 45.3988238],
    "Type": ["Pedestrian"] * 12
}

# Combine the traffic and pedestrian data
df_traffic = pd.DataFrame(traffic_data)
df_pedestrian = pd.DataFrame(pedestrian_data)

# Create the clustered map
m_clustered = folium.Map(location=[df_traffic['Latitude'].mean(), df_traffic['Longitude'].mean()], zoom_start=15)

# MarkerCluster for clustering
marker_cluster = MarkerCluster().add_to(m_clustered)

# Function to set color based on traffic count (Updated red shades)
def get_traffic_color(count):
    if count < 10:
        return 'lightred'  # Light Red for low traffic
    elif 10 <= count < 20:
        return 'red'  # Red for medium traffic
    else:
        return 'darkred'  # Dark Red for high traffic

# Function to set color based on pedestrian count
def get_pedestrian_color(count):
    if count < 5:
        return 'lightblue'
    elif 5 <= count < 10:
        return 'blue'
    else:
        return 'darkblue'

# Add traffic markers to clustered map
for idx, row in df_traffic.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Traffic Count: {row['Count']}<br>Coordinates: {row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=get_traffic_color(row['Count']), icon='car', prefix='fa')
    ).add_to(marker_cluster)

# Add pedestrian markers to clustered map
for idx, row in df_pedestrian.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Pedestrian Count: {row['Count']}<br>Coordinates: {row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=get_pedestrian_color(row['Count']), icon='male', prefix='fa')
    ).add_to(marker_cluster)

# Add Legends for Traffic and Pedestrian
legend_html_traffic = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 140px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Traffic Count Legend</b><br>
    <i style="background-color:lightred; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (0-10)<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (11-20)<br>
    <i style="background-color:darkred; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (21+)<br>
</div>
"""

legend_html_pedestrian = """
<div style="position: fixed; 
            bottom: 30px; left: 300px; width: 250px; height: 140px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Pedestrian Count Legend</b><br>
    <i style="background-color:lightblue; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (0-5)<br>
    <i style="background-color:blue; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (6-10)<br>
    <i style="background-color:darkblue; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (11+)<br>
</div>
"""

# Add the legends to the map
m_clustered.get_root().html.add_child(folium.Element(legend_html_traffic))
m_clustered.get_root().html.add_child(folium.Element(legend_html_pedestrian))

# Save the clustered map
m_clustered.save('combined_clustered_map.html')

# Create the unclustered map
m_unclustered = folium.Map(location=[df_traffic['Latitude'].mean(), df_traffic['Longitude'].mean()], zoom_start=15)

# Add traffic markers to unclustered map
for idx, row in df_traffic.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Traffic Count: {row['Count']}<br>Coordinates: {row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=get_traffic_color(row['Count']), icon='car', prefix='fa')
    ).add_to(m_unclustered)

# Add pedestrian markers to unclustered map
for idx, row in df_pedestrian.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Pedestrian Count: {row['Count']}<br>Coordinates: {row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=get_pedestrian_color(row['Count']), icon='male', prefix='fa')
    ).add_to(m_unclustered)

# Save the unclustered map
m_unclustered.save('combined_unclustered_map.html')

# Print completion message
print("Maps have been saved as 'combined_clustered_map.html' and 'combined_unclustered_map.html'.")
