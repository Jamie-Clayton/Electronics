# Weather Underground Publishing observations

## Setup Instructions

On the Raspberry PI, please follow these steps to ensure we have the components required for the weather station.

```bash
# Determine the version of python are installed. E.g. v2.7.16 or 3.9.4
python --version
python3 --version

# Confirm the python 3.7 directory exists on your raspberry (newer versions may be available via the operating system updates)
cd /usr/bin/
ls python*
# copy down the highest version of python3 available 

# Change the raspberry pi default python version to v3.7 (or higher)
ls --all
cd ~/
ls --all

# Using Visual Code via SSH 
# Press Ctrl Key
# Click on the .bashrc file in the terminal ouput to open the file in the editor.
# Add the following line to the end of the file and save that file
alias python='/usr/bin/python3.7'

# Confirm the version of the Python package manager is installed 
# pip --version
pip3 --version

# Upgrade Python package manager to the latest version available.
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip
sudo pip3 install --upgrade pip

# Install the parts need for Adafruit BME280
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade adafruit_python-shell

# Install the Web Service code needed to publish to the weather underground.
# pip3 install requests
python3 -m pip install --upgrade requests

# restart Pi after all the installations
reboot
```

## Weather Station - Temperature Humidity and Pressure

Wiring up the Adafruit BME280 sensor to work with I2C is critical to retrieving the data. The lettering and instructions on the sensor and pi requires a few integration checks.

```bash
# Show what is running on the pi 
ps aux | grep python

# Turn on I2C interface
sudo raspi-config

# Confirm the Adafruit BME280 is correctly wired - 77 should be displayed in the grid if your wired correctly
sudo i2cdetect -y 1
```

The integration test for the sensor and the raspberry pi used the following python 3 script. Saving this to the /home/pi/Documents/ folder and will generate a log file. Logging the data from the sensor for a few days will enable a further understanding of the behaviour of the sensor and your code. Running the script in Thorny IDE and via Bash will results in incorrect values getting return.

```python
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

```

Once we have sensor wiring and code operating, we want to ensure that any power interruptions result in the sensor restarting on the Pi reboot. There are a number of ways to achieve this.

```bash 
sudo nano /etc/rc.local
# Add the following line
sudo python3 /home/pi/Documents/WeatherStation-temp-pressure-humidity.py
reboot
# confirm the script is running 
ps aux | grep python

# confirm the log file is getting updated every minute.
mousepad /home/pi/Documents/Weather.lo
```

## Keyboard shortcuts

Exit python prompt

> Ctrl + Z -> Enter
> Ctrl + C -> Enter

## References

[Python Editions Running](https://raspberry-valley.azurewebsites.net/Python-Default-Version/)
[Changing to Python 3 on Raspberry Pi](https://linuxconfig.org/how-to-change-from-default-to-alternative-python-version-on-debian-linux)
[How to install Python requests code](https://stackoverflow.com/questions/23283045/importerror-no-module-named-requests-python-3-4-0/23283081)
[Pip warning - 9859](https://github.com/pypa/pip/issues/9859)