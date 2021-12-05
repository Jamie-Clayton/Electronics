#include <DS3232RTC.h>

// Real Time Clock Hardware Library :- https://github.com/hideakitai/DS323x

DS3232RTC myRTC(false);     // tell constructor not to initialize the I2C bus (Wiring option)
bool sentSignal = false;
const char* up = "↑";
const char* down = "↓";

void setup() {
  // put your setup code here, to run once:
  myRTC.begin(); 
  
  //  Manually Set the ardunio board time - Allow about 15 second for the compile and upload process.
  //  12h25m00s on 13Nov2021
  //setTime(12, 31, 30, 13, 11, 2021);
    
  //  Set the Real Time Clock to the same time as the board
  //myRTC.set(now());

  // Once the Real Time Clock has a battery and the time set, it's now the source of truth for your IOT device
  tmElements_t batteryClock;  
  myRTC.read(batteryClock);
  setTime(batteryClock.Hour, batteryClock.Minute, batteryClock.Second, batteryClock.Day , batteryClock.Month , batteryClock.Year )
}

void loop() {
  // put your main code here, to run repeatedly:
  tmElements_t tm;  
  myRTC.read(tm);
  
  // Record the top and bottom of a second hand passing the 0/360 degree and 180 degree of the rotation through the circle.
  if(tm.Second == 30 || tm.Second == 0){   
    
    if (!sentSignal){
      if (tm.Second == 30) {
        Serial.print(down);
      }else{
        Serial.print(up);
      }
      Serial.print(tm.Hour, DEC);
      Serial.print(':');
      if (tm.Minute < 10) Serial.print('0');
      Serial.print(tm.Minute, DEC);
      Serial.print(':');  
      if (tm.Second < 10) Serial.print('0');
      Serial.println(tm.Second,DEC);  
      sentSignal = true;
    }    
  }else if(tm.Second != 30 && tm.Second != 0)
  {
    sentSignal = false;
  }
  
}
