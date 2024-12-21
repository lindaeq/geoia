import pandas as pd
from datetime import datetime

# Sample data for Stop #1 (Lansdowne Park) 
data = {
    'Time': ['08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00'],
    'Traffic Count #1': [21, 13, 11, 7, 6, 1, 12, 3, 1],
    'Traffic Count #2': [40, 11, 0, 2, 11, 4, 16, 6, 16],
    'Pedestrian Count #1': [3, 7, 4, 2, 2, 3, 3, 2, 3],
    'Pedestrian Count #2': [2, 7, 0, 4, 1, 3, 0, 4, 2]
}

# Create DataFrame
df = pd.DataFrame(data)

# Remove rows with NaN values
df.dropna(inplace=True)

# Define color ranges for traffic and pedestrian counts
def get_traffic_color(count):
    if count < 5:
        return 'lightgreen'
    elif count < 15:
        return 'yellow'
    elif count < 30:
        return 'orange'
    else:
        return 'red'

def get_pedestrian_color(count):
    if count < 5:
        return 'lightblue'
    elif count < 10:
        return 'blue'
    elif count < 20:
        return 'darkblue'
    else:
        return 'navy'

# Create HTML structure with a table
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lansdowne Park Stop #1 Counts</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        table { width: 100%; border-collapse: collapse; }
        table, th, td { border: 1px solid black; }
        th, td { padding: 10px; text-align: center; }
        th { background-color: #f2f2f2; }
        .legend { margin-top: 20px; }
    </style>
</head>
<body>
    <h2>Lansdowne Park Stop #1 Traffic and Pedestrian Counts</h2>
    <table>
        <tr>
            <th>Time</th>
            <th>Traffic Count #1</th>
            <th>Traffic Count #2</th>
            <th>Pedestrian Count #1</th>
            <th>Pedestrian Count #2</th>
        </tr>
"""

# Add data to the HTML table with color coding
for index, row in df.iterrows():
    html_content += f"""
        <tr>
            <td>{row['Time']}</td>
            <td style="background-color: {get_traffic_color(row['Traffic Count #1'])};">{row['Traffic Count #1']}</td>
            <td style="background-color: {get_traffic_color(row['Traffic Count #2'])};">{row['Traffic Count #2']}</td>
            <td style="background-color: {get_pedestrian_color(row['Pedestrian Count #1'])};">{row['Pedestrian Count #1']}</td>
            <td style="background-color: {get_pedestrian_color(row['Pedestrian Count #2'])};">{row['Pedestrian Count #2']}</td>
        </tr>
    """

html_content += """
    </table>

    <div class="legend">
        <h3>Legend</h3>
        <p><b>Traffic Count #1 and #2:</b></p>
        <p><span style="background-color: lightgreen;">&#9632;</span> Low (0-5)</p>
        <p><span style="background-color: yellow;">&#9632;</span> Moderate (6-14)</p>
        <p><span style="background-color: orange;">&#9632;</span> High (15-29)</p>
        <p><span style="background-color: red;">&#9632;</span> Very High (30+)</p>

        <p><b>Pedestrian Count #1 and #2:</b></p>
        <p><span style="background-color: lightblue;">&#9632;</span> Low (0-5)</p>
        <p><span style="background-color: blue;">&#9632;</span> Moderate (6-9)</p>
        <p><span style="background-color: darkblue;">&#9632;</span> High (10-19)</p>
        <p><span style="background-color: navy;">&#9632;</span> Very High (20+)</p>
    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open("lansdowne_park_stop_1.html", "w") as file:
    file.write(html_content)

print("HTML file 'lansdowne_park_stop_1.html' has been generated.")
