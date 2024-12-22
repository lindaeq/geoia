import folium

# Data for vegetation with coordinates and vegetation level
data_vegetation = [
    (1, -75.68613185, 45.39945279),
    (1, -75.68625419, 45.39935236),
    (1, -75.68606797, 45.39952191),
    (1, -75.68565578, 45.39956356),
    (1, -75.6855184, 45.39964106),
    (1, -75.68561574, 45.39959413),
    (2, -75.68237966, 45.39962719),
    (3, -75.68270503, 45.39954344),
    (1, -75.68554083, 45.39975489),
    (1, -75.68535441, 45.39969641),
    (2, -75.6828551, 45.3992291),
    (3, -75.68315675, 45.3997154),
    (1, -75.68523736, 45.39972366),
    (1, -75.68479749, 45.39984099),
    (4, -75.68220424, 45.39874983),
    (2, -75.68388974, 45.40010075),
    (1, -75.68514616, 45.39980276),
    (2, -75.6835228, 45.40026655),
    (1, -75.68523316, 45.39904569),
    (1, -75.6833814, 45.40072861),
    (1, -75.68418563, 45.40009964),
    (2, -75.67955396, 45.40077915),
    (1, -75.68597706, 45.39948261),
    (1, -75.68556336, 45.39968055),
    (1, -75.68538195, 45.39973718),
    (2, -75.68595844, 45.39934859),
    (1, -75.68563859, 45.39944785),
    (1, -75.68550569, 45.39954396),
    (1, -75.68509971, 45.39979407),
    (1, -75.68448107, 45.39994225),
    (0, -75.68362806, 45.40010625),
    (1, -75.68242241, 45.40059971),
    (1, -75.68479447, 45.39994539),
    (1, -75.68434807, 45.40016023),
    (0, -75.68363708, 45.40046189),
    (1, -75.685945, 45.39982),
    (1, -75.68863071, 45.41579986)
]

# Function to determine the color based on the vegetation level
def get_vegetation_color(level):
    # Updated color scheme to match acceptable Folium colors
    if level == 0:
        return 'gray'  # No vegetation visible
    elif level == 1:
        return 'red'  # Very little vegetation
    elif level == 2:
        return 'lightred'  # Little vegetation
    elif level == 3:
        return 'yellow'  # Moderate vegetation
    elif level == 4:
        return 'green'  # High vegetation (Park)
    else:
        return 'darkgreen'  # Very high vegetation

# Create a folium map centered around the same starting point (Lansdowne Park)
map_center = [45.39945279, -75.68613185]
m_vegetation = folium.Map(location=map_center, zoom_start=16)

# Iterate through the data and plot markers with different colors based on vegetation level
for entry in data_vegetation:
    level, lon, lat = entry
    color = get_vegetation_color(level)  # Get the color based on the vegetation level

    # Add a tree icon for vegetation with the determined color
    folium.Marker(
        [lat, lon],
        icon=folium.Icon(color=color, icon='tree', prefix='fa'),  # Tree icon for vegetation
        popup=f"Vegetation Level: {level}"
    ).add_to(m_vegetation)

# Add a legend to the map
legend_html = """
     <div style="position: fixed; 
                 bottom: 30px; left: 30px; width: 180px; height: 140px; 
                 background-color: white; border: 2px solid grey; z-index:9999; font-size:14px;
                 font-family: Arial;">
     <b>Vegetation Levels</b><br>
     <i style="background: gray; width: 20px; height: 20px; display: inline-block;"></i> 0: No Vegetation<br>
     <i style="background: red; width: 20px; height: 20px; display: inline-block;"></i> 1: Very Little Vegetation<br>
     <i style="background: lightred; width: 20px; height: 20px; display: inline-block;"></i> 2: Little Vegetation<br>
     <i style="background: yellow; width: 20px; height: 20px; display: inline-block;"></i> 3: Moderate Vegetation<br>
     <i style="background: green; width: 20px; height: 20px; display: inline-block;"></i> 4: High Vegetation (Park)<br>
     <i style="background: darkgreen; width: 20px; height: 20px; display: inline-block;"></i> 5: Very High Vegetation
     </div>
     """
m_vegetation.get_root().html.add_child(folium.Element(legend_html))

# Save the map to an HTML file
m_vegetation.save('vegetation_map_with_legend_and_labels.html')

# Print a message indicating the map has been saved
print("Vegetation map with tree icons and legend has been saved as 'vegetation_map_with_legend_and_labels.html'.")
