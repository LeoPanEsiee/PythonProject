<<<<<<< HEAD
import json
import pandas as pd
import plotly.express as px
import numpy as np

#Loading Geojson
europe = json.load(open("europe_countries.json","r"))

#Creating ids for Geojson's europe countries
country_id_map = {}
i = 0
for feature in europe['features']:
    feature['id'] = i
    country_id_map[feature['properties']['name']] = feature['id']
    i = i+1

#Loading csv
df = pd.read_csv("Attacked.csv", delim_whitespace=True, header=13)

#Removing anwsers
df = df[df.answer != 'No']

#Removing not found countries
for country in df['CountryCode'].unique():
    if country not in country_id_map.keys():
        df = df[df.CountryCode != country]

#Binding the DataFrame's country ids
df['id'] = df['CountryCode'].apply(lambda x : country_id_map[x])
#print(df.head())

"""
#Creating choropleth map
fig = px.choropleth(df,title = "A été physiquement ou sexuellement attacké dans ces 5 dernieres années", 
    locations='id', geojson=europe, color='percentage',
    color_continuous_scale=px.colors.sequential.Blues, 
    scope='europe',
    hover_name='CountryCode',
    hover_data=['percentage'])
#fig.update_geos(visible = False) 
fig.show()
"""

fig = px.choropleth_mapbox(df,title = "A été physiquement ou sexuellement attacké dans ces 5 dernieres années", 
    locations='id', geojson=europe, color='percentage',
    color_continuous_scale=px.colors.sequential.Blues, 
    hover_name='CountryCode',
    hover_data=['percentage'],
    mapbox_style="carto-positron",
    center={'lat' : 56.7, 'lon' : 10},
    zoom = 2.1,
    opacity=0.7
    )
fig.show()

=======
import json
import pandas as pd
import plotly.express as px
import numpy as np

#Loading Geojson
europe = json.load(open("europe_countries.json","r"))

#Creating ids for Geojson's europe countries
country_id_map = {}
i = 0
for feature in europe['features']:
    feature['id'] = i
    country_id_map[feature['properties']['name']] = feature['id']
    i = i+1

#Loading csv
df = pd.read_csv("Attacked.csv", delim_whitespace=True, header=13)

#Removing anwsers
df = df[df.answer != 'No']

#Removing not found countries
for country in df['CountryCode'].unique():
    if country not in country_id_map.keys():
        df = df[df.CountryCode != country]

#Binding the DataFrame's country ids
df['id'] = df['CountryCode'].apply(lambda x : country_id_map[x])
#print(df.head())

"""
#Creating choropleth map
fig = px.choropleth(df,title = "A été physiquement ou sexuellement attacké dans ces 5 dernieres années", 
    locations='id', geojson=europe, color='percentage',
    color_continuous_scale=px.colors.sequential.Blues, 
    scope='europe',
    hover_name='CountryCode',
    hover_data=['percentage'])
#fig.update_geos(visible = False) 
fig.show()
"""

fig = px.choropleth_mapbox(df,title = "A été physiquement ou sexuellement attacké dans ces 5 dernieres années", 
    locations='id', geojson=europe, color='percentage',
    color_continuous_scale=px.colors.sequential.Blues, 
    hover_name='CountryCode',
    hover_data=['percentage'],
    mapbox_style="carto-positron",
    center={'lat' : 56.7, 'lon' : 10},
    zoom = 2.1,
    opacity=0.7
    )
fig.show()

>>>>>>> 9315f29689950c89d55bda4a6334b94e9180fe9a
#A faire : meilleurs couleurs,