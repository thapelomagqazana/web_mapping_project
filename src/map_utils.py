import folium
from folium.plugins import MarkerCluster, HeatMap

# Function to set color based on volcano elevation
def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# Function to add volcano markers to the map
def add_volcano_markers(map, data):
    # Initialize MarkerCluster
    marker_cluster = MarkerCluster().add_to(map)

    for _, row in data.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Name']} - Elevation: {row['Elevation']} m",
            icon=folium.Icon(color=color_producer(row["Elevation"]))
        ).add_to(marker_cluster)

# Function to add population layer to the map
def add_population_layer(map, population_data):
    folium.GeoJson(
        data=population_data,
        style_function=lambda feature: {
            "fillColor": "green" if feature["properties"]["POP2005"] < 10000000 else
            "orange" if feature["properties"]["POP2005"] < 20000000 else "red",
            "fillOpacity": 0.6,
            "color": "black"
        },
        name="Population"
    ).add_to(map)

# Function to add population density heatmap
def add_population_heatmap(map, population_data):
    # Extract population density points (latitude, longitude, and population as intensity)
    heat_data = [
        [feature["geometry"]["coordinates"][1], feature["geometry"]["coordinates"][0], feature["properties"]["POP2005"]]
        for feature in population_data["features"]
        if feature["geometry"]["type"] == "Point"  # Ensure we use only point coordinates
    ]
    # Add heatmap layer to the map
    HeatMap(heat_data, radius=15, max_zoom=6, blur=20, min_opacity=0.4).add_to(map)