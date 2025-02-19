import csv
import json

csv_file = 'stations.csv'
json_file = 'stations.json'

# Read CSV data
csv_data = []
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert empty string to None for float fields
        for field in ['latitude', 'longitude']:  # latitude and longitude should be floats
            if row.get(field) == '':
                row[field] = None

        # Handle elevation specifically if empty
        if row.get('elevation') == '':
            row['elevation'] = None

        csv_data.append(row)

# Convert to Django JSON fixture format
json_data = []
for idx, row in enumerate(csv_data, start=1):
    json_data.append({
        "model": "seismic.station",
        "pk": idx,
        "fields": row
    })

# Save as a JSON file
with open(json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)

print(f"JSON fixture has been written to {json_file}")
