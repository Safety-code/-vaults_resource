
# quickWeather.py - Prints the weather for a location from the command line.

import json
from urllib import response
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quicWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Donwload the JSON data from openWeatherMap.org's API

#url  = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
#url = 'https://api.stormglass.io/v2/f389cc6a-2212-11ed-bfe0-0242ac130002-f389ccce-2212-11ed-bfe0-0242ac130002/point?lat=%s&lng=%s' % 
#(location)
url = "https://api.stormglass.io/v2/weather/point" % (location),
params={
    'lat': 58.7984,
    'lng': 17.8081,
    'params' : 'windspeed'
}, 
# Authenticating the API
headers = {'Authorization': 'f389cc6a-2212-11ed-bfe0-0242ac130002-f389ccce-2212-11ed-bfe0-0242ac130002'}



response = requests.get(url)
response.raise_for_status()
print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tommorow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])