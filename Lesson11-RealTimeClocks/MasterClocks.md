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

>[PWM](https://www.arduino.cc/en/Tutorial/Foundations/PWM)  can also effect the sound of your motors. It's more efficient to use PWM compared to, say, a resistor in series, as a lot power is dissipated through the resistor. It's also much easier to output a PWM pulse and is typically built into microcontroller's hardware nowadays. [Marple, J. (2015, July 31). Electric Motor Speed Control - PWM vs analog voltage? Robotics Stack Exchange.](https://robotics.stackexchange.com/questions/7778/electric-motor-speed-control-pwm-vs-analog-voltage/7779#7779)

## References

[Elliott, R. (2021, February 1). Driving Slave Clocks With Arduino. Elliot Sound Products.](https://sound-au.com/clocks/arduino.html)

[Christensen, J. (2020, September 7). Arduino Library for Maxim Integrated DS3232 and DS3231 Real-Time Clocks. GitHub.](https://github.com/JChristensen/DS3232RTC)

[Servo, T. (2017, June 20). How to get millisecond resolution from DS3231 RTC. Stack Overflow.](https://stackoverflow.com/questions/44644383/how-to-get-millisecond-resolution-from-ds3231-rtc)

[Heath, J. (2018, November 6). PWM: Pulse Width Modulation: What is it and how does it work? Analog IC Tips.](https://www.analogictips.com/pulse-width-modulation-pwm/)

[Arduino AG. (n.d.). Arduino Nano technical specification. Arduino Online Shop.](https://store-usa.arduino.cc/products/arduino-nano)

[Chinese Nano Clone Chipsets](https://www.instructables.com/A-solution-to-avrdude-stk500getsync-not-in-syn/)

[Daga, A. (2019, July 12). AVR Microcontroller : All You Need To Know. Engineers Garage.](https://www.engineersgarage.com/avr-microcontroller-all-you-need-to-know-part-1-46/)

[Ardunio AG. (n.d.-c). Style guide. Ardunio.](https://www.arduino.cc/en/Reference/StyleGuide)

[Ardunio AG. (n.d.-b). Library tutorial. Ardunio.](https://www.arduino.cc/en/Hacking/libraryTutorial)

[Christensen, J. (2019, December 19). DS3232RTC Alarm Primer. GitHub](https://github.com/JChristensen/DS3232RTC/blob/master/alarm-primer.md)

[Ardunio AG. (n.d.). delay() - Arduino Reference. Ardunio.](https://www.arduino.cc/reference/en/language/functions/time/delay/)

[Ardunio AG. (2018, February 5). Blink without delay. Arduino.](https://www.arduino.cc/en/Tutorial/BuiltInExamples/BlinkWithoutDelay)

## Downloads

[Real Time Clock Technical Specification](https://datasheets.maximintegrated.com/en/ds/DS3231-DS3231S.pdf)
