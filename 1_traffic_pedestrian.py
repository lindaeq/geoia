import pandas as pd
import folium
from folium.plugins import MarkerCluster

# Step 1: Create the DataFrames
traffic_data = {
    "Type": ["Traffic"] * 12,
    "Count": [61, 24, 11, 9, 17, 5, 28, 9, 1, 14, 25, 15],
    "Longitude": [-75.68580531, -75.68068081, -75.68610983, -75.68449478,
                  -75.6796243, -75.68421071, -75.6780816, -75.67975324,
                  -75.68355528, -75.68651711, -75.6783432, -75.67955396],
    "Latitude": [45.3987385, 45.39891803, 45.39938252, 45.39934569,
                 45.3979209, 45.40008528, 45.4005321, 45.40002445,
                 45.40011895, 45.39976627, 45.4016608, 45.40077915]
}

pedestrian_data = {
    "Type": ["Pedestrian"] * 13,
    "Count": [5, 14, 4, 6, 3, 3, 6, 2, 7, 2, 4, 18, 6],
    "Longitude": [-75.68570327, -75.68608501, -75.68573379, -75.685212,
                  -75.68517646, -75.67992822, -75.68485444, -75.68461947,
                  -75.68473223, -75.68447114, -75.68381162, -75.6856984,
                  -75.6809709],
    "Latitude": [45.3994541, 45.39946985, 45.39958372, 45.400013,
                 45.39968338, 45.39987131, 45.3999348, 45.40002635,
                 45.39998241, 45.40001867, 45.40034716, 45.3988238,
                 45.4022448]
}

# Combine data into a single DataFrame
df_combined = pd.concat([pd.DataFrame(traffic_data), pd.DataFrame(pedestrian_data)], ignore_index=True)

# Step 2: Create the clustered map
clustered_map = folium.Map(location=[df_combined['Latitude'].mean(), df_combined['Longitude'].mean()], zoom_start=14)
marker_cluster = MarkerCluster().add_to(clustered_map)

# Add markers with clustering
for idx, row in df_combined.iterrows():
    count = row['Count']
    color = 'green' if count < 10 else 'orange' if count < 20 else 'red'
    icon = 'car' if row['Type'] == 'Traffic' else 'male'
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Type']} Count:</b> {count}<br>{row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=color, icon=icon, prefix='fa')
    ).add_to(marker_cluster)

# Step 3: Create the unclustered map
unclustered_map = folium.Map(location=[df_combined['Latitude'].mean(), df_combined['Longitude'].mean()], zoom_start=14)

# Add markers without clustering
for idx, row in df_combined.iterrows():
    count = row['Count']
    color = 'green' if count < 10 else 'orange' if count < 20 else 'red'
    icon = 'car' if row['Type'] == 'Traffic' else 'male'
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>{row['Type']} Count:</b> {count}<br>{row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=color, icon=icon, prefix='fa')
    ).add_to(unclustered_map)

# Step 4: Add a legend to both maps
legend_html = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 150px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Legend</b><br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (0-9)<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (10-19)<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (20+)<br>
    <i class="fa fa-car" style="font-size: 18px; margin-right: 10px;"></i> Traffic Data<br>
    <i class="fa fa-male" style="font-size: 18px; margin-right: 10px;"></i> Pedestrian Data<br>
</div>
"""
clustered_map.get_root().html.add_child(folium.Element(legend_html))
unclustered_map.get_root().html.add_child(folium.Element(legend_html))

# Step 5: Save both maps
clustered_map.save('combined_clustered_map.html')
unclustered_map.save('combined_unclustered_map.html')

# Print a message to indicate maps have been saved
print("Maps have been saved as 'combined_clustered_map.html' and 'combined_unclustered_map.html'.")
