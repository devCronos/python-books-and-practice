#! python3
__author__ = 'Cronos'

import sys
import requests
import json

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
url ='http://api.openweathermap.org/data/2.5/forecast/city?id=%s&APPID={1720febf7b78111c598e22d82924325d}' % (location ID)
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])