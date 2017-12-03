#!/usr/bin/env python3

import requests
import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

def create_table():
    c.execute ('''CREATE TABLE IF NOT EXISTS mtlWeather (date text, temp real, pressure real, windDeg real, windSpeed real)''')
    c.execute ('''CREATE TABLE IF NOT EXISTS estWeather (date text, temp real, pressure real, windDeg real, windSpeed real)''')


def write_weather():
    temp =  r.json()['main']['temp'] - 273.15
    pres = r.json()['main']['pressure']
    windDeg = r.json()['wind']['deg']
    windSpeed = r.json()['wind']['speed']
    currentTime = r.json()['dt']
    holder = (currentTime, temp, pres ,windDeg ,windSpeed)
    c.execute("INSERT INTO mtlWeather VALUES (?, ?, ? ,? ,?)", holder)
    conn.commit()

def write_estimate():
    temp =  r.json()['main']['temp'] - 273.15
    pres = r.json()['main']['pressure']
    windDeg = r.json()['wind']['deg']
    windSpeed = r.json()['wind']['speed']
    currentTime = r.json()['dt']
    holder = (currentTime, temp, pres ,windDeg ,windSpeed)
    c.execute("INSERT INTO estWeather VALUES (?, ?, ? ,? ,?)", holder)
    conn.commit()


if __name__ == "__main__":
   with open ('api.txt') as f:
       apikey = f.read().strip()

   apiRequest = ("http://api.openweathermap.org/data/2.5/weather?lat=45.51&lon=-73.59&APPID="+ apikey)
   r = requests.get(apiRequest)
   conn = sqlite3.connect('weather.db')
   c = conn.cursor()
   create_table()
   write_weather()
   r = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=45.51&lon=-75.59&APPID=99476ea06bd6bf3bc421363193d1e22f")
   write_estimate()
   conn.close()
