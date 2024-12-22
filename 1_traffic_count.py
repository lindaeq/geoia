import pandas as pd
import folium

# Step 1: Create the DataFrame with traffic data
traffic_data = {
    "Location": ["Stop #1 Lansdowne Park"] * 12,
    "Traffic Count": [61, 24, 11, 9, 17, 5, 28, 9, 1, 14, 25, 15],
    "Longitude": [-75.68580531, -75.68068081, -75.68610983, -75.68449478,
                  -75.6796243, -75.68421071, -75.6780816, -75.67975324,
                  -75.68355528, -75.68651711, -75.6783432, -75.67955396],
    "Latitude": [45.3987385, 45.39891803, 45.39938252, 45.39934569,
                 45.3979209, 45.40008528, 45.4005321, 45.40002445,
                 45.40011895, 45.39976627, 45.4016608, 45.40077915]
}

df_traffic = pd.DataFrame(traffic_data)

# Step 2: Create the map centered around the average latitude and longitude, with a wider zoom level
map_traffic = folium.Map(location=[df_traffic['Latitude'].mean(), df_traffic['Longitude'].mean()], zoom_start=14)

# Step 3: Add markers to the map with traffic count as popup and color coding
for idx, row in df_traffic.iterrows():
    traffic_count = row['Traffic Count']
    color = 'green' if traffic_count < 10 else 'orange' if traffic_count < 20 else 'red'  # Color based on traffic count
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"<b>Traffic Count:</b> {traffic_count}<br>{row['Latitude']}, {row['Longitude']}",
        icon=folium.Icon(color=color, icon='car', prefix='fa')  # Use Font Awesome 'car' icon for traffic
    ).add_to(map_traffic)

# Step 4: Add a custom legend for the map
legend_html_traffic = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 120px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Traffic Count Legend</b><br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (0-9)<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (10-19)<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (20+)<br>
</div>
"""

# Add the legend to the map
map_traffic.get_root().html.add_child(folium.Element(legend_html_traffic))

# Step 5: Save the map to an HTML file
map_traffic.save('traffic_count_map_no_clustering_wider_view.html')

# Print a message to indicate that the map has been saved
print("Map has been saved as 'traffic_count_map_no_clustering_wider_view.html'.")
