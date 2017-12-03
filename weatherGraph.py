#!/usr/bin/env python3


import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


if __name__ == "__main__":
   conn = sqlite3.connect('weather.db')
   c = conn.cursor()
   pressure = c.execute ('select pressure from mtlWeather limit 30')
   pres = pressure.fetchall()
   estimate = c.execute('select pressure from estWeather limit 30')
   est = estimate.fetchall()

   plt.plot(pres)
   plt.savefig('/var/www/FlaskApp/FlaskApp/static/pres.png')
   conn.close()
