Traffic Count Map with Interactive Legend
This project visualizes traffic count data on an interactive map using Python, Folium, and Pandas. The map includes markers for each data point, color-coded by traffic count, and features a custom interactive legend.

Features
Interactive Map: Displays markers for each traffic count data point.
Color-Coded Markers: Markers are color-coded based on traffic count:
Green: Low traffic (0-10 vehicles)
Yellow: Medium traffic (11-20 vehicles)
Red: High traffic (21+ vehicles)
Hover Popups: When hovering over a marker, a concise popup shows the traffic count in a single line.
Custom Legend: A fixed legend is placed in the bottom-left corner, explaining the color codes for traffic count.
Prerequisites
To run this project, you'll need to install the following libraries:

Pandas: For handling data.
Folium: For creating the interactive map.
You can install them using pip:

bash
Copy code
pip install pandas folium
How to Run
Clone or Download the repository.
Ensure you have the required libraries installed.
Place your traffic count data in the same structure as the provided dataset or modify the code accordingly.
Run the Python script:
bash
Copy code
python green_space_map.py
The script will generate a file called traffic_count_map_with_legend_enhanced.html.
Open the HTML file in a web browser to view the interactive map.
Customization
You can modify the following aspects of the map:

Data: Update the data dictionary to include your specific traffic count information.
Color Scheme: Adjust the colors for the traffic count categories by modifying the color logic in the script.
Legend: Customize the legend’s position, size, and content if necessary.
Example Map
Once the script runs, an HTML file will be generated and saved as traffic_count_map_with_legend_enhanced.html. Open this file in a web browser to view the interactive map.

