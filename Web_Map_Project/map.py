import folium
from folium.map import Icon, Marker, Popup
map = folium.Map(location = [42.3617864056339, -71.05954930389359], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[42.3617864056339, -71.05954930389359],[42.3503488063098, -71.10555066643477]]:
    fg.add_child(folium.Marker(location=coordinates, popup="The best city in the world", icon=folium.Icon(color = 'green')))

map.add_child(fg)
map.save("Boston.html")