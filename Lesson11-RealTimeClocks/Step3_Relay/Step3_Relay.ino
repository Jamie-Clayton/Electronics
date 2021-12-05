#include <DS3232RTC.h>

// Real Time Clock Hardware Library :- https://github.com/hideakitai/DS323x

DS3232RTC myRTC(false);     // tell constructor not to initialize the I2C bus (Wiring option)
bool sentSignal = false;

int relay1 = 7;
int relay2 = 5;
int relayOnTimeInMilliseconds = 100;   

void setup() {
  Serial.begin(9600); // open the serial port at 9600 bps:
  
  // put your setup code here, to run once:
  myRTC.begin(); 
  
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  tmElements_t tm;  
  myRTC.read(tm);
  
  // Record the top and bottom of a second hand passing the 0/360 degree and 180 degree of the rotation through the circle.
  if(tm.Second == 30 || tm.Second == 0){   
    if (!sentSignal){
      if (tm.Second == 30) {
        Serial.println("Relay 1 on");
        digitalWrite(relay1, HIGH);
        delay(relayOnTimeInMilliseconds);
        digitalWrite(relay1, LOW);
        Serial.println("1 off");
      }else{
        Serial.println("Relay 2");
        digitalWrite(relay2, HIGH);
        delay(relayOnTimeInMilliseconds);
        digitalWrite(relay2, LOW);
        Serial.println("2 off");
      }
      sentSignal = true;
    }    
  }else if(tm.Second != 30 && tm.Second != 0)
  {
    //  Reset the signal after once out time moves to the next second.
    sentSignal = false;
    // digitalWrite(relay1, LOW);
    // digitalWrite(relay2, LOW);
  }
  
}
