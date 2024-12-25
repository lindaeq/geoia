import folium

# Create a map centered at a known location (Ottawa)
m = folium.Map(location=[45.39979192333333, -75.68507409666667], zoom_start=18)

# Save the map as an HTML file
m.save("minimal_map.html")

print("Map saved as minimal_map.html. Open it in your browser.")
