import folium

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
    for _, row in data.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Name']} - {row['Elevation']}m",
            icon=folium.Icon(color=color_producer(row["Elevation"]))
        ).add_to(map)

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