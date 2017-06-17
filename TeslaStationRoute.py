
# coding: utf-8

# 1. Find route between two Tesla Supercharging Stations "55 Parsonage Rd. & 150th Ave and 147th St" -- Google Maps API
# 
# In order to use the Google Maps - Directions API, you need to create an account with Google and get your API key, go to: https://developers.google.com/maps/documentation/directions/ and then go to "get a key".

# In[12]:

# first import all the important packages 
import plotly.plotly as py

py.sign_in("aakashparwani", "ob2ncx7bg1")

from plotly.graph_objs import *
import mapbox
import numpy as np
import requests
import copy
import googlemaps
mapbox_access_token = 'pk.eyJ1IjoiYWFrYXNocGFyd2FuaSIsImEiOiJjaXZzdnN2MHIwM3FwMnlvMXVtdDc1MWh0In0.kyKt29LCvJC8UjEPUvPl4w'


# In[13]:

#now request all the Tesla Supercharging Stations present in USA from the Tesla website.
r = requests.get('https://www.tesla.com/findus?redirect=no#/bounds/49.38,-66.94,25.82,-124.38999999999999?search=supercharger,&name=United%20States')
r_copy = copy.deepcopy(r.text)
supercharger_locations = {}
#look for particular country data.
valid_countries = ['United States','Canada']

# define the parameters that will be used to locate the stations on google maps.
params_for_locations = ['postal_code":"', 'country":"', 'latitude":"', 'longitude":"']

# now traverse the fetched stations data and copy it in supercharger_locations dictionary that will be used in coming steps.
while True:
    # add address line to the dictionary
    index = r_copy.find('address_line_1":"')
    if index == -1:
        break
    index += len('address_line_1":"')

    index_end = index
    while r_copy[index_end] != '"':
        index_end += 1
    address_line_1 = r_copy[index:index_end]
    address_line_1 = str(address_line_1)
    supercharger_locations[address_line_1] = {}

    for param in params_for_locations:
        index = r_copy.find(param)
        if index == -1:
            break
        index += len(param)

        index_end = index
        while r_copy[index_end] != '"':
            index_end += 1
        supercharger_locations[address_line_1][param[0:-3]] = r_copy[index:index_end]

    r_copy = r_copy[index_end:len(r.text)]  # slice off the traversed code

#clean all the data which has important parameters "postal code & country" missing.     
all_keys = list(supercharger_locations.keys())
for key in all_keys:
    if '\\' in supercharger_locations[key] or supercharger_locations[key] == '' or supercharger_locations[key]['postal_code'] == '' or supercharger_locations[key]['country'] not in valid_countries:
        del supercharger_locations[key]


# In[14]:

#let us check data of start address
for v in supercharger_locations.keys():
    if v=='55 Parsonage Rd.':
         print (supercharger_locations[v]['latitude'], supercharger_locations[v]['longitude'],
               supercharger_locations[v]['postal_code'], supercharger_locations[v]['country'])


# In[15]:

#let us check data of end address
for v in supercharger_locations.keys():
    if v=='150th Ave and 147th St':
         print (supercharger_locations[v]['latitude'], supercharger_locations[v]['longitude'],
               supercharger_locations[v]['postal_code'], supercharger_locations[v]['country'])


# In[16]:

# define function that will take "start address & end address" as input and will draw route between them.
def plot_route_between_tesla_stations(address_start, address_end, zoom=3, endpt_size=6):
    start = (supercharger_locations[address_start]['latitude'], supercharger_locations[address_start]['longitude'])
    end = (supercharger_locations[address_end]['latitude'], supercharger_locations[address_end]['longitude'])
    
    directions = gmaps.directions(start, end)
    steps = []
    steps.append(start)  # add starting coordinate to trip
    
    for index in range(len(directions[0]['legs'][0]['steps'])):
        start_coords = directions[0]['legs'][0]['steps'][index]['start_location']
        steps.append((start_coords['lat'], start_coords['lng']))

        if index == len(directions[0]['legs'][0]['steps']) - 1:
            end_coords = directions[0]['legs'][0]['steps'][index]['end_location']
            steps.append((end_coords['lat'], end_coords['lng']))

    steps.append(end)  # add ending coordinate to trip
    data = Data([
        Scattermapbox(
            lat=[item_x[0] for item_x in steps],
            lon=[item_y[1] for item_y in steps],
            mode='markers+lines',
            marker=Marker(
                size=[endpt_size] + [4 for j in range(len(steps) - 2)] + [endpt_size]
            ),
        )
    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            style='streets',
            center=dict(
                lat=np.mean([float(step[0]) for step in steps]),
                lon=np.mean([float(step[1]) for step in steps]),
            ),
            pitch=0,
            zoom=zoom
        ),
    )

    fig = dict(data=data, layout=layout)
    return fig

# get the google map api key in order to call the Google API.
gmap_api_key = 'AIzaSyDzrUYQwoyb4I0i2bhl3CzALP031n4yLac'

gmaps = googlemaps.Client(gmap_api_key)

# define start address
address_start = '55 Parsonage Rd.'
# define end address
address_end = '150th Ave and 147th St'
zoom=12.2
endpt_size=20

fig = plot_route_between_tesla_stations(address_start, address_end, zoom=9, endpt_size=20)
# plot route between stations
py.iplot(fig, filename='tesla-driving-directions-between-superchargers')







##############################NEED TO WORK: MAP BOX DIRECTION API CODE#################

def plot_route1_between_tesla_stations(address_start, address_end, zoom=3, endpt_size=6):
    start = (supercharger_locations[address_start]['latitude'], supercharger_locations[address_start]['longitude'])
    end = (supercharger_locations[address_end]['latitude'], supercharger_locations[address_end]['longitude'])
    
    startv = round(float(start[0]), 5)
    startv1 = round(float(start[1]), 5)
    endv = round(float(end[0]), 5)
    endv1 = round(float(end[1]), 5)

    
    points = [{
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "Point",
        "coordinates": [
            startv,
            startv1]}}, {
    "type": "Feature",
    "properties": {},
    "geometry": {
        "type": "Point",
        "coordinates": [
            endv,
            endv1]}}]

    directions = mapbox.Directions(access_token=mapbox_access_token).directions(points)
    
    steps = []
    steps.append(start)  # add starting coordinate to trip
    
    for index in range(len(directions[0]['legs'][0]['steps'])):
        start_coords = directions[0]['legs'][0]['steps'][index]['start_location']
        steps.append((start_coords['lat'], start_coords['lng']))

        if index == len(directions[0]['legs'][0]['steps']) - 1:
            end_coords = directions[0]['legs'][0]['steps'][index]['end_location']
            steps.append((end_coords['lat'], end_coords['lng']))

    steps.append(end)  # add ending coordinate to trip
    data = Data([
        Scattermapbox(
            lat=[item_x[0] for item_x in steps],
            lon=[item_y[1] for item_y in steps],
            mode='markers+lines',
            marker=Marker(
                size=[endpt_size] + [4 for j in range(len(steps) - 2)] + [endpt_size]
            ),
        )
    ])
    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            style='streets',
            center=dict(
                lat=np.mean([float(step[0]) for step in steps]),
                lon=np.mean([float(step[1]) for step in steps]),
            ),
            pitch=0,
            zoom=zoom
        ),
    )

    fig = dict(data=data, layout=layout)
    return fig

# define start address
address_start = '55 Parsonage Rd.'
# define end address
address_end = '150th Ave and 147th St'
zoom=12.2
endpt_size=20

fig = plot_route1_between_tesla_stations(address_start, address_end, zoom=9, endpt_size=20)
#py.iplot(fig, filename='tesla-driving-directions-between-superchargers_mapbox')