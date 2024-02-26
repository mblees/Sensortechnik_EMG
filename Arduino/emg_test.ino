#include <Arduino.h>
#define emgInput A0

void setup() {
  Serial.begin(115200);
  pinMode(emgInput, INPUT);
}

void loop() {
  uint16_t input_value = analogRead(emgInput);
  Serial.print(input_value * 100);
  delay(10);
}
