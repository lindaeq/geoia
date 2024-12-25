import folium

# Sample data: Litter EQI along with coordinates
litter_data = [
    [4, -75.6848485, 45.3992055],
    [4, -75.685894, 45.3994701],
    [4, -75.6855739, 45.3996189],
    [3, -75.68234008, 45.39933537],
    [4, -75.6856098, 45.3993908],
    [3, -75.68503669, 45.39914389],
    [4, -75.6854216, 45.3995292],
    [0, -75.6852141, 45.3996979],
    [4, -75.68282804, 45.39877252],
    [0, -75.68557786, 45.39883958],
    [4, -75.6850445, 45.3997115],
    [4, -75.6836138, 45.3997994],
    [3, -75.684698, 45.3998667],
    [3, -75.68465257, 45.3994944],
    [4, -75.6843779, 45.4000221],
    [3, -75.6838183, 45.3989052],
    [3, -75.6889024, 45.4168112],
    [2, -75.6896055, 45.4170477],
    [3, -75.68701026, 45.41355937],
    [3, -75.6898825, 45.4172032],
    [3, -75.6900364, 45.4173471],
    [2, -75.6869686, 45.41382424],
    [4, -75.68971511, 45.41751849],
    [4, -75.68739197, 45.41431823],
    [3, -75.68971511, 45.41751849],
    [4, -75.6903494, 45.4178823],
    [0, -75.68772515, 45.41455229],
    [4, -75.6904256, 45.4180104],
    [2, -75.68888343, 45.41634842],
    [4, -75.6904876, 45.4181049],
    [4, -75.6929573, 45.4204157],
    [2, -75.68864389, 45.41566688],
    [4, -75.6930508, 45.4212206],
    [4, -75.6951585, 45.4281173],
    [3, -75.69239318, 45.42720186],
    [4, -75.6953279, 45.4280842],
    [4, -75.6945142, 45.4282966],
    [4, -75.6944406, 45.4283456],
    [1, -75.70777173, 45.37671213],
    [3, -75.69142176, 45.42739276],
    [3, -75.6940321, 45.4284423],
    [3, -75.6939506, 45.4284405],
    [4, -75.69334034, 45.42812933],
    [3, -75.69201876, 45.4272214],
    [3, -75.692582, 45.427138],
    [3, -75.69200162, 45.4272006],
    [3, -75.68181058, 45.40073499],
    [2, -75.68868365, 45.41519014],
    [2, -75.68877886, 45.41591398],
    [3, -75.68269932, 45.39861921],
    [3, -75.68199122, 45.39806356],
    [2, -75.68973244, 45.41719457],
    [4, -75.68954177, 45.41694955],
    [4, -75.68923698, 45.41660741],
    [3, -75.68908561, 45.41641953],
    [4, -75.68886323, 45.41617315],
    [3, -75.68855489, 45.41583022],
    [3, -75.69179274, 45.42718919],
    [3, -75.69097383, 45.42766104],
    [3, -75.69130578, 45.42753145],
    [3, -75.69156122, 45.42733677],
    [3, -75.6919456, 45.42711951],
    [3, -75.69256164, 45.42688991],
    [1, -75.699938, 45.419925]
]

# Step 1: Create the map centered on the average coordinates of your data
map_litter = folium.Map(location=[45.399, -75.686], zoom_start=14)

# Step 2: Define a function to determine color based on litter EQI
def get_litter_color(litter_value):
    if litter_value == 0:
        return 'grey'
    elif litter_value == 1:
        return 'red'
    elif litter_value == 2:
        return 'orange'
    elif litter_value == 3:
        return 'green'
    else:
        return 'darkgreen'

# Step 3: Add markers to the map based on litter EQI readings
for litter_value, lon, lat in litter_data:
    color = get_litter_color(litter_value)
    print(f"Adding marker at ({lat}, {lon}) with litter value: {litter_value}")  # Debugging line
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>Litter EQI:</b> {litter_value}<br>{lat}, {lon}",
        icon=folium.Icon(color=color, icon='trash', prefix='fa')
    ).add_to(map_litter)

# Step 4: Add a custom legend to the map
legend_html_litter = """
<div style="position: fixed; 
            bottom: 30px; left: 30px; width: 250px; height: 160px; 
            background-color: white; border:2px solid grey; z-index:9999;
            font-size: 16px; font-family: 'Helvetica', sans-serif; padding: 10px;">
    <b>Litter EQI Legend</b><br>
    <i style="background-color:grey; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 0 - A lot of litter<br>
    <i style="background-color:red; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 1 - Litter over 25% of the area<br>
    <i style="background-color:lightred; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 2 - Litter over 10% of the area<br>
    <i style="background-color:lightgreen; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 3 - Very little litter<br>
    <i style="background-color:green; width: 18px; height: 18px; float: left; margin-right: 10px;"></i> 4 - No litter<br>
</div>
"""

# Add the legend to the map
map_litter.get_root().html.add_child(folium.Element(legend_html_litter))

# Step 5: Save the map to an HTML file
map_litter.save('litter_eqi_map.html')

# Print a message to indicate that the map has been saved
print("Map has been saved as 'litter_eqi_map.html'.")
