#include <DS323x.h>
DS323x rtc;

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  rtc.attach(Wire);
  rtc.now(DateTime(2021, 11, 13, 07, 18, 00));
}

void loop() {
  // put your main code here, to run repeatedly:

  // Test the DS323x library
  DateTime now = rtc.now();
  Serial.println(now.timestamp());  
  // Delay is not as accurate as the realtime clock based methods.
  delay(30000);
}
