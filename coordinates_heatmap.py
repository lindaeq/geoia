import folium
from folium.plugins import HeatMap

# Remove any coordinates that could be out of range or invalid
coordinates = [
    [-75.68496487, 45.3990971],
    [-75.68613185, 45.39945279],
    [-75.68625419, 45.39935236],
    [-75.6848485, 45.3992055],
  
]

# Create a base map centered around the first coordinate (Ottawa)
m = folium.Map(location=[45.4215, -75.6972], zoom_start=13)

# Add a heatmap to the map
HeatMap(coordinates).add_to(m)

# Save the map as an HTML file
m.save('heatmap.html')

# If running in Jupyter or a compatible environment, you can view it inline
m
