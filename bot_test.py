import os
from dotenv import load_dotenv
import requests
from meteofrance_api import MeteoFranceClient

client = MeteoFranceClient()
list_places = client.search_places('Lyon')
my_place = list_places[0]
weather_forecast = client.get_forecast_for_place(my_place)
my_place_daily_forecast = weather_forecast.daily_forecast
temp_max = my_place_daily_forecast[0]['T']['max']
temp_min =  my_place_daily_forecast[0]['T']['min']
temps =  my_place_daily_forecast[0]['weather12H']['desc']
pluie =  my_place_daily_forecast[0]['precipitation']['24h']
rain = client.get_rain(latitude= 45.764043, longitude=4.835659)

def habit(temps) :
  if temps == "Ensoleillé" :
   m = "Aimé prend ta combinaison !!!!!"
  else:
    m = ""
  return(m)

aime = habit(temps)
print(aime)