/*
  Blinking a Led

  In this program a Led is connected to ESP32 33 GPIO Pin.
  Turns an LED on for one second, then off for one second, repeatedly.

*/
int ledPin=33;
// the setup function runs once when you power the board
void setup() {
  // initialize digital pin ledPin as an output.
  pinMode(ledPin, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(ledPin, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(ledPin, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);                      // wait for a second
}
