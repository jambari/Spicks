import json
import csv

# Sample JSON data (from your provided data)
# Load JSON data from a file
with open("slmon.all.laststatus.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Prepare CSV data
csv_data = []

for feature in data['features']:
    # Extract properties
    properties = feature['properties']
    
    # Derive the 'name' field from 'location'
    location_parts = properties['location'].split(',')
    name = location_parts[0]  # Assuming the first part of the location is the name
    
    # Create a dictionary for each record to add to CSV
    csv_data.append({
        'code': properties['sta'],
        'network': properties['net'],
        'name': name,
        'latitude': feature['geometry']['coordinates'][1],
        'longitude': feature['geometry']['coordinates'][0],
        'elevation': None,  # No elevation in the JSON, leave as None or add if available
        'created_at': properties['time']
    })

# Step 2: Export data to CSV
csv_file = 'stations.csv'
fieldnames = ['code', 'network', 'name', 'latitude', 'longitude', 'elevation', 'created_at']

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(csv_data)

print(f"Data has been written to {csv_file}")
