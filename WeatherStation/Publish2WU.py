import requests
import json 

# Documentation
# https://docs.python.org/3/library/json.html
# https://docs.python-requests.org/en/master/
# https://docs.google.com/document/d/1eKCnKXI9xnoMGRRzOL1xPCBihNV2rOet08qpE_gArAY/edit
# https://code.visualstudio.com/docs/remote/ssh#_getting-started 
# https://docs.python.org/3/library/time.html

# python3 -m pip install --upgrade requests

# Retrieve from https://www.wunderground.com/dashboard/pws
StationID = ''
StationApiKey = ''

# Fixed location details.
StationCountryCode = 'AU'
StationLatitude = -27.53513
StationLongitude = 152.933376
StationNeighbourhood = 'Jindalee'
StationUnits = 'm' # Metric
StationElevation = '20' # Meters above sea level.

# Generic code to enable the weather data to be converted to Javascript Object Notation structure required by the Weather Underground (IBM) apis.
class Object:
    def toJSON(self):
        return json.dumps(self,default=lambda o: o.__dict__, sort_keys=True, indent=4)

WeatherURL = f'https://api.weather.com/v2/pws/observations/current?stationId={StationID}&format=json&units={StationUnits}&apiKey={StationApiKey}'

headers = {'user-agent': 'RaspberryPiPython/0.0.1',
            'Accept-Encoding': 'gzip'}

data = Object()
data.observations = Object()
data.observations.metric = Object()

# Geographic location
data.observations.stationID = StationID
data.observations.country = StationCountryCode
data.observations.neighborhood = StationNeighbourhood
data.observations.lon = StationLongitude
data.observations.lat = StationLatitude
# Software source and quality and frequency in minutes.
data.observations.softwareType = 'Python Script'
data.observations.qcStatus = 1
data.observations.realtimeFrequency = 3

# Date and Time of the weather observation.
data.observations.obsTimeUtc = ''
data.observations.obsTimeLocal = '' 
data.observations.epoch = ''

# Metric Observations at that time.
data.observations.metric.elev = 20
data.observations.temp = 24

print(data.toJSON())

# Publish your weather station observations to the weather underground.
response = requests.post(WeatherURL, headers=headers, json=data.toJSON())

if response.status_code != 200:
    print(f'POST {WeatherURL} {response.status_code}')  
    print(f'{response.content}') 
if response.status_code == 200:  
    print(f'Published weather observation for {StationID}')

# Review the API calls and the associated success
# https://www.wunderground.com/member/api-keys