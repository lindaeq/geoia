import folium
from folium.plugins import HeatMap

# Coordinates for the heatmap (same as the previous ones)
coordinates = [
    (-75.68598998, 45.3993471),
    (-75.68504322, 45.39983201),
    (-75.68418909, 45.40019666),
    (-75.6851941, 45.3978694),
    (-75.70777173, 45.37671213),
    (-75.6849731, 45.3990165),
    (-75.68469976, 45.399926),
    (-75.68657874, 45.41529579),
    (-75.69000014, 45.41743525),
    (-75.6887961, 45.4160652),
    (-75.68987252, 45.41737817),
    (-75.68779272, 45.41527702),
    (-75.68901959, 45.41646855),
    (-75.69073209, 45.41811772),
    (-75.69036878, 45.41771403),
    (-75.68818156, 45.41586523),
    (-75.6884273, 45.4157928),
    (-75.69115298, 45.41886274),
    (-75.69008699, 45.4174835),
    (-75.69141602, 45.41905811),
    (-75.69523811, 45.42822252),
    (-75.69534506, 45.42808166),
    (-75.69502512, 45.42807899),
    (-75.6926678, 45.4273578),
    (-75.69419718, 45.42850909),
    (-75.69431242, 45.42848439),
    (-75.69365306, 45.42868656),
    (-75.6926905, 45.42810224),
    (-75.69431975, 45.42843863),
    (-75.6944276, 45.428548),
    (-75.69226823, 45.42767069),
    (-75.69297033, 45.42907781),
    (-75.69108116, 45.42654176)
]

# EQI data for litter, vandalism, street furniture, and green space (from 0-2)
litter = [
    (0, -75.6852141, 45.3996979),
    (0, -75.68557786, 45.39883958),
    (2, -75.6896055, 45.4170477),
    (2, -75.6869686, 45.41382424),
    (0, -75.68772515, 45.41455229),
    (2, -75.68888343, 45.41634842),
    (2, -75.68864389, 45.41566688),
    (1, -75.70777173, 45.37671213),
    (2, -75.68868365, 45.41519014),
    (2, -75.68877886, 45.41591398),
    (2, -75.68973244, 45.41719457),
    (1, -75.699938, 45.419925)
]

vandalism = [
    (2, -75.68592689, 45.39897974),
    (2, -75.68984009, 45.41728294),
    (0, -75.68696921, 45.41381336),
    (2, -75.69051415, 45.4183073),
    (0, -75.68747957, 45.41460257),
    (2, -75.68888343, 45.41634842),
    (0, -75.68853469, 45.41566551),
    (0, -75.69482803, 45.42837139),
    (1, -75.69204082, 45.42760752),
    (0, -75.6947106, 45.4284627),
    (1, -75.69237468, 45.42937749),
    (1, -75.692165, 45.429576),
    (0, -75.69216362, 45.42778123),
    (2, -75.68868365, 45.41519014),
    (1, -75.68886323, 45.41617315),
    (2, -75.69156122, 45.42733677)
]

street_furniture = [
    (0, -75.6820282, 45.400017),
    (0, -75.68706558, 45.4139203),
    (2, -75.68724484, 45.41413216),
    (2, -75.68888343, 45.41634842),
    (2, -75.69274727, 45.42811291),
    (0, -75.69327322, 45.42816729)
]

green_space = [
    (1, -75.68622499, 45.39911921),
    (2, -75.68585674, 45.39969703),
    (2, -75.68574057, 45.39966012),
    (2, -75.68510765, 45.39987948),
    (2, -75.68476209, 45.39981327),
    (2, -75.6847127, 45.3997665),
    (2, -75.68438771, 45.40002007),
    (1, -75.68999764, 45.41743509),
    (1, -75.6901345, 45.41788684),
    (2, -75.69064387, 45.41819682),
    (2, -75.6835407, 45.39995022),
    (2, -75.69435247, 45.42862136),
    (0, -75.70777173, 45.37671213),
    (0, -75.69201876, 45.4272214),
    (0, -75.70777173, 45.37671213),
    (0, -75.692582, 45.427138),
    (0, -75.68868365, 45.41519014),
    (1, -75.68877886, 45.41591398)
]

# Create a map centered around the average latitude and longitude of the coordinates
map_heatmap = folium.Map(location=[sum([lat for lon, lat in coordinates]) / len(coordinates),
                                  sum([lon for lon, lat in coordinates]) / len(coordinates)],
                         zoom_start=14)

# Prepare heatmap data (just coordinates)
heat_data = [[lat, lon] for lon, lat in coordinates]

# Add the heatmap layer to the map
HeatMap(heat_data).add_to(map_heatmap)

# Add markers for EQI values (0-2 range) for litter, vandalism, street furniture, and green space
def add_eqi_markers(eqi_data, eqi_type, icon):
    for value, lon, lat in eqi_data:
        if value <= 2:
            folium.Marker(
                location=[lat, lon],
                popup=f"<b>{eqi_type.capitalize()} EQI:</b> {value}<br>{lat}, {lon}",
                icon=folium.Icon(color='black', icon=icon, prefix='fa')  # Black color for all markers
            ).add_to(map_heatmap)

# Add EQI markers for all categories
add_eqi_markers(litter, "litter", 'volume-up')  # Sound icon for litter
add_eqi_markers(vandalism, "vandalism", 'paint-brush')  # Graffiti/paintbrush icon for vandalism
add_eqi_markers(street_furniture, "street_furniture", 'cogs')  # Gear icon for street furniture
add_eqi_markers(green_space, "green_space", 'tree')  # Tree icon for green space

# Save the map with heatmap and EQI markers
map_heatmap.save('heatmap_with_eqi_markers.html')

# Print confirmation
print("Map with heatmap and EQI markers has been saved as 'heatmap_with_eqi_markers.html'.")
