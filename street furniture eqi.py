import folium

# Data for street furniture with EQI and coordinates
street_furniture_data = [
    [4, -75.68496487, 45.3990971],
    [4, -75.6858149, 45.399905],
    [4, -75.68234008, 45.39933537],
    [4, -75.68484974, 45.39900302],
    [4, -75.6852277, 45.3998167],
    [4, -75.6848155, 45.3999518],
    [4, -75.68282804, 45.39877252],
    [3, -75.68578656, 45.39885696],
    [4, -75.68439516, 45.39894949],
    [3, -75.6840749, 45.4001159],
    [4, -75.6830748, 45.4004479],
    [3, -75.6830331, 45.4005281],
    [4, -75.68441808, 45.39948131],
    [4, -75.68381541, 45.40023009],
    [4, -75.6838183, 45.3989052],
    [0, -75.6820282, 45.400017],
    [3, -75.6908569, 45.4176516],
    [0, -75.68706558, 45.4139203],
    [3, -75.6910971, 45.4180258],
    [2, -75.68724484, 45.41413216],
    [3, -75.68775886, 45.41478365],
    [4, -75.6922975, 45.4197597],
    [2, -75.68888343, 45.41634842],
    [3, -75.68855435, 45.41576795],
    [3, -75.6931683, 45.4207158],
    [3, -75.6946731, 45.4283539],
    [2, -75.69274727, 45.42811291],
    [4, -75.6935884, 45.4288994],
    [3, -75.69142176, 45.42739276],
    [0, -75.69327322, 45.42816729],
    [3, -75.692165, 45.429576],
    [3, -75.69201876, 45.4272214],
    [3, -75.69170731, 45.42741692],
    [4, -75.68181058, 45.40073499],
    [3, -75.68868365, 45.41519014],
    [3, -75.68877886, 45.41591398],
    [4, -75.68269932, 45.39861921],
    [4, -75.68199122, 45.39806356],
    [3, -75.68973244, 45.41719457],
    [4, -75.68954177, 45.41694955],
    [4, -75.68923698, 45.41660741],
    [3, -75.68908561, 45.41641953],
    [3, -75.68886323, 45.41617315],
    [4, -75.68855489, 45.41583022],
    [3, -75.69179274, 45.42718919],
    [3, -75.69097383, 45.42766104],
    [4, -75.69130578, 45.42753145],
    [3, -75.69156122, 45.42733677],
    [4, -75.6919456, 45.42711951],
    [3, -75.69256164, 45.42688991]
]

# Step 1: Create the map centered around the average coordinates
map_street_furniture = folium.Map(location=[45.399, -75.686], zoom_start=14)

# Step 2: Define a function to get color based on street furniture condition
def get_street_furniture_color(furniture_value):
    if furniture_value == 0:
        return 'gray'
    elif furniture_value == 1:
        return 'red'
    elif furniture_value == 2:
        return 'orange'
    elif furniture_value == 3:
        return 'green'
    else:
        return 'darkgreen'

# Step 3: Add markers to the map for each street furniture data point
for furniture_value, lon, lat in street_furniture_data:
    color = get_street_furniture_color(furniture_value)
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Street Furniture Condition:</b> {furniture_value}<br>{lat}, {lon}",
        icon=folium.Icon(color=color, icon='tag', prefix='fa')
    ).add_to(map_street_furniture)

# Step 4: Add custom legend to the map
legend_html_street_furniture = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 160px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Street Furniture Condition Legend</b><br>
    <i style="background-color:gray; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 0 - Street furniture not present<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 1 - Street furniture in poor condition<br>
    <i style="background-color:orange; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 2 - About 25% of street furniture<br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 3 - Less than 10% of street furniture<br>
    <i style="background-color:darkgreen; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 4 - Street furniture is well maintained<br>
</div>
"""

# Add the legend to the map
map_street_furniture.get_root().html.add_child(folium.Element(legend_html_street_furniture))

# Step 5: Save the map as an HTML file
map_street_furniture.save('street_furniture_map.html')

# Print a message indicating the map is saved
print("Map has been saved as 'street_furniture_map.html'.")
