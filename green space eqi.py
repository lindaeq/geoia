import folium

# Data for green space / open space with condition values and coordinates
green_space_data = [
    [1, -75.68622499, 45.39911921],
    [2, -75.68585674, 45.39969703],
    [2, -75.68574057, 45.39966012],
    [4, -75.68234008, 45.39933537],
    [2, -75.68510765, 45.39987948],
    [2, -75.68476209, 45.39981327],
    [2, -75.6847127, 45.3997665],
    [2, -75.68438771, 45.40002007],
    [4, -75.68282804, 45.39877252],
    [3, -75.68450736, 45.39998714],
    [4, -75.68379236, 45.40042036],
    [4, -75.68352295, 45.40024106],
    [3, -75.68336544, 45.40033853],
    [2, 100.47396, 13.79162005],
    [4, -75.6838183, 45.3989052],
    [3, -75.6897876, 45.41727029],
    [1, -75.68999764, 45.41743509],
    [1, -75.6901345, 45.41788684],
    [2, -75.69064387, 45.41819682],
    [3, -75.69090005, 45.41860377],
    [2, -75.6835407, 45.39995022],
    [3, -75.69114011, 45.41886964],
    [4, -75.69169805, 45.4192357],
    [3, -75.69181686, 45.41967431],
    [3, -75.68888343, 45.41634842],
    [4, -75.69245665, 45.41994135],
    [4, -75.69243026, 45.42016778],
    [3, -75.69532922, 45.42815344],
    [4, -75.69522078, 45.42816141],
    [3, -75.69449595, 45.42841073],
    [2, -75.69435247, 45.42862136],
    [0, -75.70777173, 45.37671213],
    [3, -75.69183187, 45.42957647],
    [0, -75.69201876, 45.4272214],
    [0, -75.70777173, 45.37671213],
    [0, -75.692582, 45.427138],
    [4, -75.68181058, 45.40073499],
    [0, -75.68868365, 45.41519014],
    [1, -75.68877886, 45.41591398],
    [4, -75.68269932, 45.39861921],
    [4, -75.68199122, 45.39806356],
    [3, -75.68973244, 45.41719457],
    [3, -75.68908561, 45.41641953],
    [3, -75.69179274, 45.42718919]
]

# Step 1: Create the map centered around the average coordinates
map_green_space = folium.Map(location=[45.399, -75.686], zoom_start=14)

# Step 2: Define a function to get color based on green space condition
def get_green_space_color(space_value):
    if space_value == 0:
        return 'gray'
    elif space_value == 1:
        return 'red'
    elif space_value == 2:
        return 'orange'
    elif space_value == 3:
        return 'green'
    else:
        return 'darkgreen'

# Step 3: Add markers to the map for each green space data point
for space_value, lon, lat in green_space_data:
    color = get_green_space_color(space_value)
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Green Space Condition:</b> {space_value}<br>{lat}, {lon}",
        icon=folium.Icon(color=color, icon='leaf', prefix='fa')
    ).add_to(map_green_space)

# Step 4: Add custom legend to the map
legend_html_green_space = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 160px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Green Space Condition Legend</b><br>
    <i style="background-color:gray; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 0 - Green space not present<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 1 - Green space is small<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 2 - Green space is shared<br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 3 - Green space is shared<br>
    <i style="background-color:darkgreen; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 4 - Green space is well maintained<br>
</div>
"""

# Add the legend to the map
map_green_space.get_root().html.add_child(folium.Element(legend_html_green_space))

# Step 5: Save the map as an HTML file
map_green_space.save('green_space_map.html')

# Print a message indicating the map is saved
print("Map has been saved as 'green_space_map.html'.")
