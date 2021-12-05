# File:     WU-upload.py
# Date:     27 Feb 2021
# Author:   GEN
# Brief:    Capture data from Raspberry Pi inputs and push on to Weather underground server


import RPi.GPIO as gpio
import time
import requests
import board
import digitalio
import busio
import adafruit_bme280

# gpio.setwarnings(False)
# Define constants
RAIN_GPIO = 17
WIND_SPEED_GPIO = 18
RAIN_INC_INCHES = 11/1000  # 1 trigger event corresponds to 11 points of rain
WIND_SPEED_CONV = 1.5 # mph each sec

# Define global variables
rain = 0
rainfall = 10/1000
wind_speed = 0
wind_gust = 0
wind_average = 180.0
wind_event_time = 0
last_time = 0
humidity = 0
ambient_temp = 23.4
pressure = 1067
ground_temp = 16.3
update_flag = 2

# Set-up Raspberry-Pi ports
gpio.setmode(gpio.BCM)
gpio.setup(RAIN_GPIO, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(WIND_SPEED_GPIO, gpio.IN, pull_up_down=gpio.PUD_UP)

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

# create a string to hold the first part of the URL
WUurl = "https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?"
WU_station_id = "" # Replace XXXX with your PWS ID
WU_station_pwd = "" # Replace YYYY with your Password
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
action_str = "&action=updateraw"

# define a threaded callback function  
# this will run in another thread when a rain event is triggered  
def rain_callback(channel):  
    global rainfall
    rainfall = rainfall + RAIN_INC_INCHES 


# this will run in another thread when a wind speed event is triggered  
def wind_callback(channel):
    global wind_event_time
    wind_event_time = time.time()
    

def getWindSpeed ():    
    global last_time
#    global wind_event_time
    elapsed_time = (wind_event_time - last_time)/100000  
    if elapsed_time > 0:
        wind_speed = 1.5 / elapsed_time # calculate windspeed in mph
    else: 
        wind_speed = 0
    last_time = wind_event_time # update the wind_time variable for use next time function is called
    return 1.5 #wind_speed

def getHumidity ():
    humidity = bme280.relative_humidity
    return humidity

def getTemp ():
    tempc = bme280.temperature
    tempf = 9 * tempc / 5 + 32
    return tempf

def getPressure ():
    pressure = bme280.pressure
    pressure_in = pressure/33.8638864
    return pressure_in

def getWindGust ():
    global wind_gust
    if wind_speed > wind_gust:
        wind_gust = wind_speed
    return wind_gust

def getWindDir ():
    return wind_average

def getRainfall ():
    return 0.05 #rainfall

def publishData ():
    date_str = "&dateutc=now"
    humidity_str = "{0:.2f}".format(getHumidity())
    pressure_str = "{0:.2f}".format(getPressure())
    wind_speed_mph_str = "{0:.2f}".format(getWindSpeed())
    wind_gust_mph_str = "{0:.2f}".format(getWindGust())
    ambient_temp_str = "{0:.2f}".format(getTemp())
    rainfall_str = "{0:.2f}".format(getRainfall())
    wind_average_str = "{0:.2f}".format(getWindDir())
    r = requests.get(WUurl + WUcreds + date_str +
        "&humidity=" + humidity_str +
        "&baromin=" + pressure_str +
        "&windspeedmph=" + wind_speed_mph_str +
        "&windgustmph=" + wind_gust_mph_str +
        "&tempf=" + ambient_temp_str +
        "&rainin=" + rainfall_str +
        "winddir=" + wind_average_str +
        action_str)
    print("Received " + str(r.status_code) + " " + str(r.text))
    
    
def main():

    # When a falling edge is detected on RAIN_GPIO, regardless of whatever   
    # else is happening in the program, the function rain_callback will be run  
    gpio.add_event_detect(RAIN_GPIO, gpio.FALLING, callback=rain_callback, bouncetime=200) 
    # When a falling edge is detected on WIND_SPEED_GPIO, regardless of whatever   
    # else is happening in the program, the function wind_callback will be run  
    gpio.add_event_detect(WIND_SPEED_GPIO, gpio.FALLING, callback=wind_callback, bouncetime=100) 

    while True:
        print (ambient_temp)
        print (update_flag)
        if update_flag == 2:
#            getData ()
            publishData ()
        print (getTemp())
        current_time = time.localtime() # return day
        print (current_time)
        time.sleep(300)
 
if (__name__ == "__main__"):
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

