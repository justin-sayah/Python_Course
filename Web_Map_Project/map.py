import folium

map = folium.Map(location = [42.3617864056339, -71.05954930389359], zoom_start=6, tiles="Stamen Terrain")
map.add_child(folium.Marker())

map.save("Boston.html")
