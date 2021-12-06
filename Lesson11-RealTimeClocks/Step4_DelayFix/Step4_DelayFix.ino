#include <DS3232RTC.h>

// Real Time Clock Hardware Library :- https://github.com/JChristensen/DS3232RTC
// Sub Second resolutions for DS3231 RTC: https://stackoverflow.com/questions/44644383/how-to-get-millisecond-resolution-from-ds3231-rtc

DS3232RTC myRTC(false);     // tell constructor not to initialize the I2C bus (Wiring option)
unsigned long myTime;       // Enable us to monitor milli seconds. Generally, you should use "unsigned long" for variables that hold time as it will 
bool sentSignal = false;

const int relay1 = 7;
const unsigned long relayOnTimeInMilliseconds = 100;   

void setup() {
  Serial.begin(9600); // open the serial port at 9600 bps:
  
  // put your setup code here, to run once:
  myRTC.begin(); 

  //  Manually Set the ardunio board time - Allow about 15 second for the compile and upload process.
  //  22h00m00s on 5Dec2021
  setTime(22, 00, 00, 05, 12, 2021);
  
  // following line sets the RTC to the date & time from the ardunio
  // RTC do not function correctly until you set the date and time.
  myRTC.set(now());

  //  Setup the ardunio board pin for the relay.
  pinMode(relay1, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tmElements_t tm;  
  myRTC.read(tm);
  unsigned long currentMillis = millis();
  
//  Serial.print("Real Time: ");
//  Serial.print(tm.Minute);
//  Serial.print(":");
//  Serial.print(tm.Second);
//  Serial.print(" ");
//  Serial.print(currentMillis); 
//  Serial.println("ms"); 
  
  // Record the top and bottom of a second hand passing the 0/360 degree and 180 degree of the rotation through the circle.
  if(tm.Second == 30 || tm.Second == 0){   
    if (!sentSignal){
      SetRelay(relay1,HIGH);
      sentSignal = true;
      
      //   Delay is bad and using the ardunio board time not the RTC.
      delay(relayOnTimeInMilliseconds);
    }
    
    // Logic to switch the Relay pulse off as long as the relayOnTimeInMilliseconds has also been exceeded
    if (sentSignal && digitalRead(relay1)== HIGH){             
      SetRelay(relay1,LOW);
    }      
  }
  
  if(tm.Second != 30 && tm.Second != 0)
  {
    //  Reset the signal after once out time moves to the next second.
    sentSignal = false;  
    
    //  In the rare case something has gone wrong, lets fix it.
    if (digitalRead(relay1)== HIGH){             
      SetRelay(relay1,LOW);
    }      
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
