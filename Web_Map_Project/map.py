import folium, pandas
from folium.map import Icon, Marker, Popup

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location = [42.3617864056339, -71.05954930389359], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt,ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt,ln], popup="Temp", icon=folium.Icon(color = 'green')))

map.add_child(fg)
map.save("map.html")