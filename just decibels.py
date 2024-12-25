import folium

# Sample data: Decibel readings along with coordinates
data = [
    [64.8, -75.68607551, 45.39950376],
    [61.4, -75.685485, 45.399294],
    [58.85, -75.685485, 45.399294],
    [61.775, -75.6840382, 45.3998534],
    [63.3, -75.68586963, 45.3995553],
    [58.975, -75.685485, 45.399294],
    [63.675, -75.68327214, 45.40149973],
    [61.825, -75.68573375, 45.39956858],
    [63.075, -75.6842269, 45.3996538],
    [61.275, -75.684409, 45.399757],
    [61.675, -75.685485, 45.399294],
    [63.975, -75.68507748, 45.3998149],
    [61.325, -75.6846017, 45.3988245],
    [56.375, -75.684089, 45.400485],
    [59.925, -75.68401096, 45.4001816],
    [57.65, -75.684593, 45.399135],
    [65.275, -75.6860014, 45.3989872],
    [63.325, -75.68499931, 45.39930391],
    [62.45, -75.6858507, 45.3983931],
    [69.1, -75.6897981, 45.41712066],
    [71.175, -75.68989514, 45.41726258]
    # Add more data points as needed
]

# Step 1: Create the map centered on the average coordinates of your data
map_decibels = folium.Map(location=[45.399, -75.686], zoom_start=14)

# Step 2: Define a function to determine color based on decibel levels
def get_color(decibel):
    if decibel < 60:
        return 'green'
    elif 60 <= decibel < 65:
        return 'orange'
    else:
        return 'red'

# Step 3: Add markers to the map based on decibel readings
for decibel, lon, lat in data:
    color = get_color(decibel)
    print(f"Adding marker at ({lat}, {lon}) with decibel: {decibel}")  # Debugging line
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Decibel:</b> {decibel} dB<br>{lat}, {lon}",
        icon=folium.Icon(color=color, icon='volume-up', prefix='fa')
    ).add_to(map_decibels)

# Step 4: Add a custom legend to the map
legend_html_decibels = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 120px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Decibel Legend</b><br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Low (below 60 dB)<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> Medium (60 - 64 dB)<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> High (65+ dB)<br>
</div>
"""

# Add the legend to the map
map_decibels.get_root().html.add_child(folium.Element(legend_html_decibels))

# Step 5: Save the map to an HTML file
map_decibels.save('decibel_reading_map.html')

# Print a message to indicate that the map has been saved
print("Map has been saved as 'decibel_reading_map.html'.")
