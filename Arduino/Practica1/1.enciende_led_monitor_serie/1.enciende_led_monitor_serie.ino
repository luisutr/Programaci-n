
#define LED 5 // pin D1 del nodeMCU

void setup() {
  pinMode(LED, OUTPUT); // LED como salida
  Serial.begin(115200);
}

void loop() {
  String s;
  // Lee un valor entero del Monitor Serie
  Serial.println("Encender/apagar led, e para encender y a para apagar");
  s = leerLinea();
  if (s=="e") {
    digitalWrite(LED, HIGH);    // enciende el LED
  }
  if (s=="a") {
    digitalWrite(LED, LOW);   // apaga el LED
  }
}

String leerLinea() {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil('\n');
}
