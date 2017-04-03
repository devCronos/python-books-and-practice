#! python3
__author__ = 'Cronos'


import requests
import json
import pprint

url ='http://api.openweathermap.org/data/2.5/forecast/city?id=684039&APPID=1720febf7b78111c598e22d82924325d'
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)

w = weatherData['list']
print('Current weather in Botosani is:' )
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
