import folium
import webbrowser
import os
import tkinter
# Création de la carte centrée sur le monde
carte = folium.Map(location=[0, 0], zoom_start=2)

# Exemple de quelques points sur la carte (latitude, longitude)
points = [
    {"name": "New York", "location": [40.7128, -74.0060]},
    {"name": "Paris", "location": [48.8566, 2.3522]},
    {"name": "Tokyo", "location": [35.6895, 139.6917]},
    {"name": "Cape Town", "location": [-33.9249, 18.4241]},
    {"name": "Sydney", "location": [-33.8688, 151.2093]},
    {"name": "London", "location": [51.5072, -0.1275]},
]

# Ajout des points sur la carte
for point in points:
    folium.Marker(location=point["location"], popup=point["name"]).add_to(carte)

# Enregistrement de la carte sous forme de fichier HTML
fichier_html = "carte_monde.html"
carte.save(fichier_html)