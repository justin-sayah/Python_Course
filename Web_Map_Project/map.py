from os import read
import folium, pandas
from folium.map import Icon, Marker, Popup

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elev):
    if elev <1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [42.3617864056339, -71.05954930389359], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")

for lt,ln,el in zip(lat,lon,elev):
    fgv.add_child(folium.Marker(location=[lt,ln], popup=str(el) + "m", icon=folium.Icon(color = color_producer(el), icon='thumb-tack', prefix = 'fa')))

fgp.add_child(folium.GeoJson(data = open("world.json", 'r', encoding='utf-8-sig').read(), 
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")