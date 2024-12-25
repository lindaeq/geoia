import folium

# Vandalism data with EQI and coordinates
vandalism_data = [
    [4, -75.68586922, 45.39944435],
    [4, -75.68592109, 45.39939864],
    [4, -75.68571464, 45.39960785],
    [4, -75.68234008, 45.39933537],
    [4, -75.68515097, 45.39982319],
    [4, -75.68489261, 45.39985753],
    [4, -75.68509217, 45.3992538],
    [4, -75.68459744, 45.39993484],
    [4, -75.68457694, 45.39999504],
    [4, -75.68282804, 45.39877252],
    [4, -75.68458709, 45.39998822],
    [4, -75.68371286, 45.40021977],
    [4, -75.68337955, 45.40031548],
    [2, -75.68592689, 45.39897974],
    [4, -75.68344306, 45.40028264],
    [4, -75.68484985, 45.39944534],
    [4, -75.68332923, 45.40032289],
    [4, -75.6838183, 45.3989052],
    [2, -75.68984009, 45.41728294],
    [3, -75.69011449, 45.41764679],
    [3, -75.69039024, 45.41804497],
    [4, -75.69075739, 45.4183096],
    [0, -75.68696921, 45.41381336],
    [2, -75.69051415, 45.4183073],
    [4, -75.69116424, 45.41867741],
    [3, -75.68724678, 45.41418354],
    [3, -75.69196531, 45.41949627],
    [0, -75.68747957, 45.41460257],
    [3, -75.69182895, 45.41975993],
    [2, -75.68888343, 45.41634842],
    [3, -75.69284656, 45.42054151],
    [0, -75.68853469, 45.41566551],
    [3, -75.69287593, 45.42062315],
    [4, -75.69531088, 45.42811153],
    [0, -75.69482803, 45.42837139],
    [1, -75.69204082, 45.42760752],
    [0, -75.6947106, 45.4284627],
    [3, -75.69457057, 45.42841054],
    [3, -75.6935884, 45.4288994],
    [4, -75.69299896, 45.42909527],
    [4, -75.69142176, 45.42739276],
    [1, -75.69237468, 45.42937749],
    [1, -75.692165, 45.429576],
    [3, -75.69201876, 45.4272214],
    [3, -75.69336042, 45.42815716],
    [4, -75.692582, 45.427138],
    [0, -75.69216362, 45.42778123],
    [4, -75.68181058, 45.40073499],
    [2, -75.68868365, 45.41519014],
    [4, -75.68877886, 45.41591398],
    [4, -75.68269932, 45.39861921],
    [4, -75.68199122, 45.39806356],
    [3, -75.68973244, 45.41719457],
    [4, -75.68954177, 45.41694955],
    [4, -75.68923698, 45.41660741],
    [3, -75.68908561, 45.41641953],
    [1, -75.68886323, 45.41617315],
    [3, -75.68855489, 45.41583022],
    [4, -75.69179274, 45.42718919],
    [4, -75.69097383, 45.42766104],
    [3, -75.69130578, 45.42753145],
    [2, -75.69156122, 45.42733677],
    [4, -75.6919456, 45.42711951],
    [4, -75.69256164, 45.42688991]
]

# Step 1: Create the map centered around the average coordinates
map_vandalism = folium.Map(location=[45.399, -75.686], zoom_start=14)

# Step 2: Define a function to get color based on vandalism level
def get_vandalism_color(vandalism_value):
    if vandalism_value == 0:
        return 'gray'
    elif vandalism_value == 1:
        return 'red'
    elif vandalism_value == 2:
        return 'orange'
    elif vandalism_value == 3:
        return 'green'
    else:
        return 'darkgreen'

# Step 3: Add markers to the map for each vandalism data point
for vandalism_value, lon, lat in vandalism_data:
    color = get_vandalism_color(vandalism_value)
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Vandalism Level:</b> {vandalism_value}<br>{lat}, {lon}",
        icon=folium.Icon(color=color, icon='tag', prefix='fa')
    ).add_to(map_vandalism)

# Step 4: Add custom legend to the map
legend_html_vandalism = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 160px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Vandalism/Graffiti Legend</b><br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 0 - A lot of vandalism/graffiti<br>
    <i style="background-color:lightred; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 1 - Vandalism / graffiti present<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 2 - Vandalism / graffiti present (less)<br>
    <i style="background-color:yellow; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 3 - Very little vandalism / graffiti<br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 4 - No vandalism / graffiti<br>
</div>
"""

# Add the legend to the map
map_vandalism.get_root().html.add_child(folium.Element(legend_html_vandalism))

# Step 5: Save the map as an HTML file
map_vandalism.save('vandalism_graffiti_map.html')

# Print a message indicating the map is saved
print("Map has been saved as 'vandalism_graffiti_map.html'.")
