import pandas as pd
from geopy.distance import geodesic
import folium
from folium import plugins

# Full file paths for your data
pedestrian_file = r'C:\Users\liliu\python crap\geo ia\pedestrian count 2.csv'
vegetation_file = r'C:\Users\liliu\python crap\geo ia\vegetation index 2.csv'

# Read the data
pedestrian_df = pd.read_csv(pedestrian_file)
vegetation_df = pd.read_csv(vegetation_file)

# Drop rows with missing values in latitude and longitude
pedestrian_df = pedestrian_df.dropna(subset=['latitude', 'longitude'])
vegetation_df = vegetation_df.dropna(subset=['latitude', 'longitude'])

# Define function to find the closest vegetation point for each pedestrian
def get_closest_vegetation(pedestrian_row, vegetation_df):
    pedestrian_coords = (pedestrian_row['latitude'], pedestrian_row['longitude'])
    
    # Initialize minimum distance to a large value
    min_distance = float('inf')
    closest_veg_index = None
    
    for idx, vegetation_row in vegetation_df.iterrows():
        vegetation_coords = (vegetation_row['latitude'], vegetation_row['longitude'])
        distance = geodesic(pedestrian_coords, vegetation_coords).meters
        
        if distance < min_distance:
            min_distance = distance
            closest_veg_index = idx  # Storing the index of the closest vegetation
    
    return closest_veg_index, min_distance

# Apply the function to find the closest vegetation index for each pedestrian and its distance
pedestrian_df[['closest_veg_index', 'distance_to_veg']] = pd.DataFrame(
    pedestrian_df.apply(get_closest_vegetation, axis=1, vegetation_df=vegetation_df).tolist(),
    index=pedestrian_df.index
)

# Now identify the vegetation rows that have no corresponding pedestrian
vegetation_df['closest_pedestrian'] = vegetation_df.apply(
    lambda x: pedestrian_df[pedestrian_df['closest_veg_index'] == x.name].shape[0] > 0, axis=1
)

# Filter out vegetation points with no matching pedestrian
unmatched_vegetation = vegetation_df[vegetation_df['closest_pedestrian'] == False]

# Create a map and mark both pedestrians and vegetation (use folium for visualization)
m = folium.Map(location=[pedestrian_df['latitude'].mean(), pedestrian_df['longitude'].mean()], zoom_start=13)

# Add pedestrian locations to the map with a person icon
for idx, row in pedestrian_df.iterrows():
    folium.Marker([row['latitude'], row['longitude']], 
                  popup=f"Pedestrian Count: {row['pedestrian count']}",
                  icon=folium.Icon(icon='fa-user', prefix='fa', color='blue')).add_to(m)

# Add vegetation locations to the map with a tree icon and connect to closest pedestrian
for idx, row in vegetation_df.iterrows():
    # For vegetation that has a matching pedestrian, draw a line connecting
    if pd.notna(row['closest_pedestrian']) and row['closest_pedestrian']:
        # Get the closest pedestrian
        closest_pedestrian = pedestrian_df.loc[pedestrian_df['closest_veg_index'] == idx]
        if not closest_pedestrian.empty:
            # Draw line connecting the closest pedestrian to the vegetation
            folium.PolyLine(
                locations=[
                    [closest_pedestrian['latitude'].values[0], closest_pedestrian['longitude'].values[0]],
                    [row['latitude'], row['longitude']]
                ],
                color="black", weight=2.5, opacity=1
            ).add_to(m)
            
    # Mark vegetation as a tree icon (if connected)
    if pd.notna(row['closest_pedestrian']) and row['closest_pedestrian']:
        folium.Marker([row['latitude'], row['longitude']],
                      popup=f"Vegetation Index: {row['vegetation index']}",
                      icon=folium.Icon(icon='fa-tree', prefix='fa', color='green')).add_to(m)
    
    # Mark unmatched vegetation as grey filled dots
    if not row['closest_pedestrian']:
        folium.CircleMarker([row['latitude'], row['longitude']], radius=6, color="gray", fill=True, fill_color="gray", fill_opacity=0.5).add_to(m)

# Show the map
m.save('geo_map_with_icons.html')

# Prepare table with closest coordinates and their values
closest_info = []
for idx, row in pedestrian_df.iterrows():
    closest_veg_idx = row['closest_veg_index']
    closest_veg = vegetation_df.loc[closest_veg_idx]
    
    closest_info.append({
        'pedestrian_lat': row['latitude'],
        'pedestrian_lon': row['longitude'],
        'pedestrian_count': row['pedestrian count'],
        'vegetation_lat': closest_veg['latitude'],
        'vegetation_lon': closest_veg['longitude'],
        'vegetation_index': closest_veg['vegetation index']
    })

# Convert the list of closest pairs into a DataFrame
closest_info_df = pd.DataFrame(closest_info)

# Print the table with closest coordinates
print("Table of closest pedestrian and vegetation coordinates with their values:")
print(closest_info_df)

# Print unmatched vegetation coordinates
print("\nUnmatched vegetation coordinates (no corresponding pedestrian):")
print(unmatched_vegetation[['latitude', 'longitude']])
