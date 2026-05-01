String leerLinea() {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil('\n');
}

int leerEntero(String s) {
  String r;
  Serial.println(s);
  r = leerLinea();
  return r.toInt(); 
}
