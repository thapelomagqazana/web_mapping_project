import folium
import pandas as pd
import json
from map_utils import add_volcano_markers, add_population_layer

# Create the map with attribution for the "Stamen Terrain" tile
map = folium.Map(
    location=[39.8283, -98.5795], 
    zoom_start=5,
    tiles="Stamen Terrain",
    attr="Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap contributors"
)
# Load volcano data
volcano_data = pd.read_csv("data/volcanoes.csv")
add_volcano_markers(map, volcano_data)

# Load population data and add population layer
with open("data/world_population.json", "r") as f:
    population_data = json.load(f)
add_population_layer(map, population_data)


# Save the map as an HTML file
map.save("maps/Population_Volcano_Map.html")