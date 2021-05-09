# Overview

https://bit.ly/33rlhK6

This is combination project, using multiple sensors including. We have included links and code from other garage projects, to help you customise the project.

* rgb LED
* Buzzer
* Ultra Sonic Distance Sensor (2 - 400 cm)
* Raspberry Pi
* Python programming language
* Breadboard

## Python Knowledge
> \#! 
>
> Shebang
>
> The first line in this file is the "shebang" line.  When you execute a file from the shell, the shell tries to run the file using the command specified on the shebang line.

## Ultra Sonic Distance Sensor

[Source Code](https://github.com/adeept/Adeept_Ultimate_Starter_Kit_Python_Code_for_RPi/blob/master/14_distance.py)
[Instruction](../Ultimate_Sensor_Kit_RPi_Guidebook_Last.pdf)

### Configuration

| Pin | Layout | Sensor Name                | Name | Action       | Sensor Pin |
| --- | ------ | -------------------------- | ---- | ------------ | ---------- |
| 2   | 5V     | Ultrasonic Distance Sensor | Vcc  | 5 volt power | 1          |
| 6   | Ground | Ultrasonic Distance Sensor | GND  | Ground       | 4          |
| 16  | GPIO23 | Ultrasonic Distance Sensor | Trig | Input        | 2          |
| 18  | GPIO24 | Ultrasonic Distance Sensor | Echo | Output       | 3          |

![Layout](../assets/raspberry_pi_Raspberry-Pi-GPIO-Layout-Model-B-Plus.png =200x655)

```python
#! /usr/bin/python
import RPi.GPIO as GPIO
import time

TRIG = 16
ECHO = 18

def checkdist():
	GPIO.output(TRIG, GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(TRIG, GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	t2 = time.time()
	return (t2-t1)*340/2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ECHO,GPIO.IN)
time.sleep(2)
try:
	while True:
        distance = checkdist()
		print ('Distance: %0.2f m' %distance)
		time.sleep(0.5)
        # Add Garage Parking light commands   
except KeyboardInterrupt:
	GPIO.cleanup()
```

## Parking Sensor Alarm

The sensor code has been adapted to work with 3 leds and a buzzer.

[Instructions](https://www.hackster.io/342470/parking-sensor-alarm-ddd8d5)

```python
#import the libraries used
import time
import pigpio
import RPi.GPIO as GPIO

#create an instance of the pigpio library
pi = pigpio.pi()

#define the pin used by the Buzzer
#this pin will be used by the pigpio library
#which takes the pins in GPIO forms
#we will use GPIO18, which is pin 12

buzzer = 18

#set the pin used by the buzzer as OUTPUT
pi.set_mode(buzzer, pigpio.OUTPUT)
GPIO.setmode(GPIO.BOARD)

#define the pins used by the ultrasonic module
trig = 16
echo = 13
redled = 36
greenled = 38
blueled = 40

#set the trigger pin as OUTPUT and the echo as INPUT
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

#set the pins for the led as OUTPUT
GPIO.setup(redled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)
GPIO.setup(blueled, GPIO.OUT)

def calculate_distance():
    #set the trigger to HIGH
    GPIO.output(trig, GPIO.HIGH)
    #sleep 0.00001 s and the set the trigger to LOW
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)
    #save the start and stop times
    start = time.time()
    stop = time.time()
    #modify the start time to be the last time until
    #the echo becomes HIGH
    while GPIO.input(echo) == 0:
        start = time.time()
    #modify the stop time to be the last time until
    #the echo becomes LOW
    while GPIO.input(echo) == 1:
        stop = time.time()
    #get the duration of the echo pin as HIGH
    duration = stop - start
    #calculate the distance
    distance = 34300/2 * duration
    if distance < 0.5 and distance > 400:
        return 0
    else:
        #return the distance
        return distance
try:
    while True:
        if calculate_distance() < 10:
            #turn on the buzzer at a frequency of
            #500Hz for 50 ms
            pi.hardware_PWM(buzzer, 500, 200000)
            time.sleep(0.02)
            
            #turn off the buzzer and wait 50 ms
            #pi.hardware_PWM(buzzer, 0, 0)
            #time.sleep(0.05)

            #the next 4 instructions are used
            #to create the flashing effect
            #turn on the red Led and wait 35 ms
            GPIO.output(redled, GPIO.HIGH)
            time.sleep(0.035)
            #turn off the red Led and wait 35 ms
            GPIO.output(redled, GPIO.LOW)
            time.sleep(0.025)

            #turn off the buzzer and wait 50 ms
                        pi.hardware_PWM(buzzer, 0, 0)
                        time.sleep(0.05)


        elif calculate_distance() > 10 and calculate_distance() < 25:
            #turn on the green Led and wait 300 ms
                 GPIO.output(greenled, GPIO.HIGH)
                     time.sleep(0.3)

                     #turn off the green Led and wait 200 ms
                 GPIO.output(greenled, GPIO.LOW)
                 time.sleep(0.2)
        elif calculate_distance() > 25:
             #turn on the blue Led and wait 300 ms
             GPIO.output(blueled, GPIO.HIGH)
             time.sleep(0.5)
             #turn off the blue Led and wait 200 ms
             GPIO.output(blueled, GPIO.LOW)
             time.sleep(0.2)
        else:
            #turn off the buzzer
            pi.hardware_PWM(buzzer, 0, 0)
            #wait 100 ms before the next run
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
#turn off the buzzer
pi.write(buzzer, 0)
#stop the connection with the daemon
pi.stop()
#clean all the used ports
GPIO.cleanup()
```

## RGB LED

[Source Code](https://github.com/adeept/Adeept_Ultimate_Starter_Kit_Python_Code_for_RPi/blob/master/08_rgbLed.py)

```python
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF, 0X6F00D2, 0xFF5809]

R = 11
G = 12
B = 13

def setup(Rpin, Gpin, Bpin):
	global pins
	global p_R, p_G, p_B
	pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	for i in pins:
		GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
		GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led
	
	p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
	p_G = GPIO.PWM(pins['pin_G'], 1999)
	p_B = GPIO.PWM(pins['pin_B'], 5000)
	
	p_R.start(100)      # Initial duty Cycle = 100(leds off)
	p_G.start(100)
	p_B.start(100)

def map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def off():
	for i in pins:
		GPIO.output(pins[i], GPIO.HIGH)    # Turn off all leds

def setColor(col):   # For example : col = 0x112233
	R_val = (col & 0xff0000) >> 16
	G_val = (col & 0x00ff00) >> 8
	B_val = (col & 0x0000ff) >> 0

	R_val = map(R_val, 0, 255, 0, 100)
	G_val = map(G_val, 0, 255, 0, 100)
	B_val = map(B_val, 0, 255, 0, 100)
	
	p_R.ChangeDutyCycle(100-R_val)     # Change duty cycle
	p_G.ChangeDutyCycle(100-G_val)
	p_B.ChangeDutyCycle(100-B_val)

def loop():
	while True:
		for col in colors:
			setColor(col)
			time.sleep(0.5)

def destroy():
	p_R.stop()
	p_G.stop()
	p_B.stop()
	off()
	GPIO.cleanup()

if __name__ == "__main__":
	try:
		setup(R, G, B)
		loop()
	except KeyboardInterrupt:
		destroy()
```