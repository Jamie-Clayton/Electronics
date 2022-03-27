# https://docs.circuitpython.org/projects/bme280/en/latest/api.html

import RPi.GPIO as gpio
import board
from adafruit_bme280 import basic as adafruit_bme280
import time
from datetime import datetime
import csv

gpio.setmode(gpio.BCM)
i2c = board.I2C()   # uses board.SCL and board.SDA
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme.sea_level_pressure = 1013.25

current_minute = "00"


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    if (now.strftime("%S") == "00" and now.strftime("%M") != current_minute):
        current_minute = now.strftime("%M")
        print ("Time = ", current_time)
        print ("Temperature", end = ": ")
        print (bme.temperature)
        print ("Humidity", end = ": ")
        print (bme.relative_humidity)
        print ("Pressure", end = ": ")
        print (bme.pressure)
        print ("")
        data = [now.strftime("%Y-%m-%d %H:%M:%S %z"), bme.temperature, bme.relative_humidity, bme.pressure ]
        
        f = open("/home/pi/Documents/Weather.log","a")
        log = csv.writer(f)
        log.writerow(data)
        f.close()