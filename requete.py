# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 13:23:32 2022

@author: delas
"""
import os
from dotenv import load_dotenv
import requests
from meteofrance_api import MeteoFranceClient
message = {
  "username": "Mr.météo",
  "avatar_url": "",
  "content": "Bonne journée les golems :))",
  "embeds": [
    {
      "color": 8933607,
      "timestamp": "",
      "author": { "name": "Météo du jour :"},
      "image": {},
      "thumbnail": {},
      "footer": {},
      "fields": [
        {
          "name": "Température :",
          "value": "temperature = 10"
        },
        {
          "name": "Temps global :",
          "value": "Annonce = 10"
        }
      ]
    }
  ],
  "components": []
}
#r = requests.get('https://rpcache-aa.meteofrance.com/internet2018client/2.0/forecast')
#print(r.text)
#message = {"content": "test"}
#requests.post('https://discord.com/api/webhooks/1039875501147291688/qTzf_ssvS2Zg_DIEgwckRiUz-6OYnVZNPa2P7OHoWfc5YavzjClhwG4ZHqDdEs7pr7Z2', json= message);

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

message['embeds'][0]['fields'][0]['value']= f"min {temp_min} - max {temp_max} "
message['embeds'][0]['fields'][1]['value']= f" {temps}"


load_dotenv()
requests.post(os.getenv("webhook"), json= message);

