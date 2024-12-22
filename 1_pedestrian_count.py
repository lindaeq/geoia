import pandas as pd
import folium

# Step 1: Create the DataFrame with pedestrian data
pedestrian_data = {
    "Data collection location": ["Stop #1 Lansdowne Park"] * 13,
    "Pedestrian count #1": [5, 14, 4, 6, 3, 3, 6, 2, 7, 2, 4, 18, 6],
    "Longitude": [-75.68570327, -75.68608501, -75.68573379, -75.685212,
                  -75.68517646, -75.67992822, -75.68485444, -75.68461947,
                  -75.68473223, -75.68447114, -75.68381162, -75.6856984,
                  -75.6809709],
    "Latitude": [45.3994541, 45.39946985, 45.39958372, 45.400013,
                 45.39968338, 45.39987131, 45.3999348, 45.40002635,
                 45.39998241, 45.40001867, 45.40034716, 45.3988238,
                 45.4022448]
}

df_pedestrian = pd.DataFrame(pedestrian_data)

# Step 2: Create the map centered around the average latitude and longitude, with a wider zoom level
map_pedestrian = folium.Map(location=[df_pedestrian['Latitude'].mean(), df_pedestrian['Longitude'].mean()], zoom_start=14)

# Step 3: Add markers to the map with pedestrian count as popup and person icon
for idx, row in df_pedestrian.iterrows():
    pedestrian_count = row['Pedestrian count #1']
    color = 'green' if pedestrian_count < 5 else 'orange' if pedestrian_count < 10 else 'red'  # Color based on pedestrian count
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>Pedestrian Count:</b> {pedestrian_count}<br>{row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=color, icon='male', prefix='fa')  # Use Font Awesome 'male' icon for pedestrians
    ).add_to(map_pedestrian)

# Step 4: Add a custom legend for the map
legend_html_pedestrian = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 120px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Pedestrian Count Legend</b><br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (0-4)<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (5-9)<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (10+)<br>
</div>
"""

# Add the legend to the map
map_pedestrian.get_root().html.add_child(folium.Element(legend_html_pedestrian))

# Step 5: Save the map to an HTML file
map_pedestrian.save('pedestrian_count_map_no_clustering_wider_view.html')

# Print a message to indicate that the map has been saved
print("Map has been saved as 'pedestrian_count_map_no_clustering_wider_view.html'.")
