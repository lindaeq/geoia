import folium
from folium.plugins import HeatMap

# New coordinates provided
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

# Create a map centered around the average latitude and longitude of the coordinates
map_heatmap = folium.Map(location=[sum([lat for lon, lat in coordinates]) / len(coordinates),
                                  sum([lon for lon, lat in coordinates]) / len(coordinates)],
                         zoom_start=14)

# Prepare heatmap data (just coordinates, no specific count since it's not provided)
heat_data = [[lat, lon] for lon, lat in coordinates]

# Add the heatmap layer to the map
HeatMap(heat_data).add_to(map_heatmap)

# Save the map with heatmap to an HTML file
map_heatmap.save('heatmap_from_coordinates.html')

# Print confirmation
print("Heatmap has been saved as 'heatmap_from_coordinates.html'.")
