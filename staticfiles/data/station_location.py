import pygmt
import json

# Load station metadata from JSON file
with open("stations.json") as f:
    stations = json.load(f)

def plot_station_map(station):
    station_code = station["fields"]["code"]
    lon, lat = float(station["fields"]["longitude"]), float(station["fields"]["latitude"])
    
    # Define region (Indonesia bounding box)
    region = [90, 150, -15, 10]  # Approximate Indonesia boundary
    
    # Create a new figure
    fig = pygmt.Figure()
    
    # Plot the base map with coastline and country borders
    fig.basemap(region=region, projection="M6i", frame=["a", "WSne"])
    fig.coast(land="gray", water="lightblue", borders=[1], resolution="i")
    
    # Plot the station as a red triangle
    fig.plot(x=[lon], y=[lat], style="t0.3c", fill="red", pen="black")
    
    # Add station code as text
    fig.text(x=lon, y=lat + 0.5, text=station_code, font="10p,Helvetica-Bold,black", justify="CM")
    
    # Save the figure
    output_file = f"{station_code}_map.png"
    fig.savefig(output_file, dpi=300)
    print(f"Saved: {output_file}")

# Loop through each station and generate a map
for station in stations:
    plot_station_map(station)
