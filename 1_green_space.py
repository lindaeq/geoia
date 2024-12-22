import folium

# Data for green spaces with environmental quality index and coordinates
data = [
    (1, -75.68622499, 45.39911921),
    (2, -75.68585674, 45.39969703),
    (2, -75.68574057, 45.39966012),
    (4, -75.68234008, 45.39933537),
    (2, -75.68510765, 45.39987948),
    (2, -75.68476209, 45.39981327),
    (2, -75.6847127, 45.3997665),
    (2, -75.68438771, 45.40002007),
    (4, -75.68282804, 45.39877252),
    (3, -75.68450736, 45.39998714),
    (4, -75.68379236, 45.40042036),
    (4, -75.68352295, 45.40024106),
    (3, -75.68336544, 45.40033853),
    (1, 100.47396, 13.79162005),
    (4, -75.68269932, 45.39861921),
    (4, -75.68199122, 45.39806356),
    (4, -75.6838183, 45.3989052)
]

# Function to determine the color based on the environmental quality index
def get_color(index):
    # Custom color scheme for EQI
    if index == 1:
        return 'red'  # Low green space
    elif index == 2:
        return 'lightcoral'  # Slightly more green space
    elif index == 3:
        return 'yellow'  # Medium green space
    elif index == 4:
        return 'green'  # High green space
    else:
        return 'darkgreen'  # Very high green space

# Create a folium map centered around a starting point (Ottawa coordinates)
map_center = [45.39911921, -75.68622499]
m = folium.Map(location=map_center, zoom_start=16)

# Iterate through the data and plot markers with different colors based on the environmental quality index
for entry in data:
    index, lon, lat = entry
    color = get_color(index)  # Get the color based on the environmental index

    # Add a circle marker with the determined color and display the EQI number
    folium.CircleMarker([lat, lon], radius=12, color=color, fill=True, fill_opacity=0.6, 
                        popup=f"EQI: {index}").add_to(m)

# Add a legend to the map
legend_html = """
     <div style="position: fixed; 
                 bottom: 30px; left: 30px; width: 180px; height: 140px; 
                 background-color: white; border: 2px solid grey; z-index:9999; font-size:14px;
                 font-family: Arial;">
     <b>Green Space Index</b><br>
     <i style="background: red; width: 20px; height: 20px; display: inline-block;"></i> 1: Low Green Space<br>
     <i style="background: lightcoral; width: 20px; height: 20px; display: inline-block;"></i> 2: Slight Green Space<br>
     <i style="background: yellow; width: 20px; height: 20px; display: inline-block;"></i> 3: Medium Green Space<br>
     <i style="background: green; width: 20px; height: 20px; display: inline-block;"></i> 4: High Green Space<br>
     <i style="background: darkgreen; width: 20px; height: 20px; display: inline-block;"></i> 5: Very High Green Space
     </div>
     """
m.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
m.save('green_spaces_map_with_legend_and_labels_updated_v2.html')

# Print a message indicating the map has been saved
print("Map with updated color scheme and legend has been saved as 'green_spaces_map_with_legend_and_labels_updated_v2.html'.")
