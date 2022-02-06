# Introduction

Point, Evidence, Explain, Link

* Gotchas
  * Millisecond accurate time is hard.
  * Cables (Power vs Power & Data)
  * Microcontroller - registers and interrupts
  * Working with small electronics
* IDE Configuration for new users
* Evolving from a breadboard
  * Soldering
* Choosing a software library

## Master Clock Source Code
```c++
#include <DS3232RTC.h> // Real time clock library with most code examples
#include <stdio.h> // C++ library function sprintf
#include <limits.h> // Constants for variable sizes
DS3232RTC rtc(false);

const int relay1 = 7;
const int relayOnInMilliseconds = 100;

char seconds[2];
volatile bool sentSignal;
volatile bool relayOpen;
volatile unsigned long currentMillis;
volatile unsigned long relayStopAfterMillis;

void setup() {
  // Let this run for 1 hour to confirm there are 120 executions and the relay timing reports at approximately 100ms 
  Serial.begin(9600); // open the serial port at 9600
  rtc.begin();
  //  Setting the RTC clock is required if the power drops off.
  setTime(12, 45, 00, 06, 02, 2022);
  rtc.set(now());
  sentSignal = false;
  
  //  Setup the ardunio board pin for the relay.
  pinMode(relay1, OUTPUT);
}

void loop() {
  tmElements_t tm;  
  rtc.read(tm);
  if(tm.Second == 30 || tm.Second == 0){
    if (!sentSignal){     
      sprintf(seconds, "%02d", tm.Second);
      Serial.print("Reporting in ");        
      Serial.print(seconds);
      Serial.println(".");
      sentSignal = true;
      SetRelay(relay1,HIGH);
      relayStopAfterMillis = CalculateStopMillis(millis());      
      relayOpen = true;
    }
    
    // Monitor if relay has exceeded the time and can be closed.
    if (millis() >= relayStopAfterMillis && relayOpen)
    {
      //  Relay can close the circuit.
      SetRelay(relay1,LOW);
      relayOpen = false;
    }
    
  }
  if(tm.Second != 30 && tm.Second != 0){
    if (sentSignal){       
      //  Reset the signal after once out time moves to the next second.
      sentSignal = false; 
    }
  }
}

//  ASSUMPTION: We have the hardware reaching the maximum value
unsigned long CalculateStopMillis(unsigned long relayStartedAtMillis){    
  //   Calculated the millis value that should close the relay.
  if ((ULONG_MAX - relayOnInMilliseconds) > relayStartedAtMillis){
    //  Happy Path: millis will always be higher on the next call
    return relayStartedAtMillis + relayOnInMilliseconds;
  }else {
    //  Unlikely Path: millis is going to rollover back to zero.
    return relayOnInMilliseconds - (ULONG_MAX - relayStartedAtMillis);
  }        
}

void SetRelay(int relayControlPin, uint8_t highOrLow){
  if (highOrLow == HIGH || highOrLow == LOW){
    Serial.print("Relay on pin ");
    Serial.print(relayControlPin);
    if (highOrLow == HIGH){ 
      Serial.println(" on");
    }
    if (highOrLow == LOW){          
      Serial.println(" off");
    }
    digitalWrite(relayControlPin, highOrLow);  
  }  
}
```

>[PWM](https://www.arduino.cc/en/Tutorial/Foundations/PWM)  can also effect the sound of your motors. It's more efficient to use PWM compared to, say, a resistor in series, as a lot power is dissipated through the resistor. It's also much easier to output a PWM pulse and is typically built into microcontroller's hardware nowadays. [Marple, J. (2015, July 31). Electric Motor Speed Control - PWM vs analog voltage? Robotics Stack Exchange.](https://robotics.stackexchange.com/questions/7778/electric-motor-speed-control-pwm-vs-analog-voltage/7779#7779)

Resolving communications problems with the Ardunio Nano hardware was uncovered via the IDE verbose settings and search for explicit errors, uncovering the need for ATmega328P(Old bootloader) settings.

> I bought a cheap Arduino Nano clone from China which uses the CH340C USB chip instead of the chip found on the genuine Arduino. I fixed it by:
>
> 1) Installing the CH340 driver
> 2) Set processor to ATmega328P(Old bootloader)
> 3) Using Arduino IDE installed locally on my Win10 pc, NOT the online Arduino IDE.
>
> NB. If both the locally installed and online Arduino IDE are open at the same time they can generate a different error "avrdude: ser_open(): can't open device "\\.\COM8": Access is denied." Simply close the online Arduino IDE to fix this error.
> [B1268, M. (2017, October 28). Avrdude Stk500_getsync(): Not in Sync Resp=0x30 Error for Arduino. Instructables.](https://www.instructables.com/A-solution-to-avrdude-stk500getsync-not-in-syn/)

## References

[Arduino AG. (n.d.). Nano technical specification. Arduino.](https://store-usa.arduino.cc/products/arduino-nano)

[Ardunio AG. (n.d.-a). delay() reference. Ardunio.](https://www.arduino.cc/reference/en/language/functions/time/delay/)

[Ardunio AG. (n.d.-b). Library tutorial. Ardunio.](https://www.arduino.cc/en/Hacking/libraryTutorial)

[Ardunio AG. (n.d.-c). Style guide. Ardunio.](https://www.arduino.cc/en/Reference/StyleGuide)

[Ardunio AG. (2018, February 5). Blink without delay. Arduino.](https://www.arduino.cc/en/Tutorial/BuiltInExamples/BlinkWithoutDelay/)

[B1268, M. (2017, October 28). Avrdude Stk500_getsync(): Not in Sync Resp=0x30 Error for Arduino. Instructables.](https://www.instructables.com/A-solution-to-avrdude-stk500getsync-not-in-syn/)

[Christensen, J. (2019, December 19). DS3232RTC Alarm Primer. GitHub.](https://github.com/JChristensen/DS3232RTC/blob/master/alarm-primer.md)

[Christensen, J. (2020, September 7). Arduino Library for Maxim Integrated DS3232 and DS3231 Real-Time Clocks. GitHub.](https://github.com/JChristensen/DS3232RTC)

[Daga, A. (2019, July 12). AVR Microcontroller : All You Need To Know. Engineers Garage.](https://www.engineersgarage.com/avr-microcontroller-all-you-need-to-know-part-1-46/)

[Elliott, R. (2021, February 1). Driving Slave Clocks With Arduino. Elliot Sound Products.](https://sound-au.com/clocks/arduino.html)

[Heath, J. (2018, November 6). PWM: Pulse Width Modulation: What is it and how does it work? Analog IC Tips.](https://www.analogictips.com/pulse-width-modulation-pwm/)

[Marple, J. (2015, July 31). Electric Motor Speed Control - PWM vs analog voltage? Robotics Stack Exchange.](https://robotics.stackexchange.com/questions/7778/electric-motor-speed-control-pwm-vs-analog-voltage/7779#7779)

[Servo, T. (2017, June 20). How to get millisecond resolution from DS3231 RTC. Stack Overflow.](https://stackoverflow.com/questions/44644383/how-to-get-millisecond-resolution-from-ds3231-rtc)

## Downloads

[Real Time Clock Technical Specification](https://datasheets.maximintegrated.com/en/ds/DS3231-DS3231S.pdf)
