// Pisca o LED embutido (pin 13 no Leonardo)
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // acende
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);  // apaga
  delay(500);
}
