
String leerLinea() {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil('\n');
}

int leerEntero() {
  String r;
  r = leerLinea();
  return r.toInt(); 
}

void rellenaVectorEnteroAleatorio(int v[], int tam) {
  int i;
  // Inicializa el vector v con valores aleatorios
  for(i=0; i<tam; i++) {
    v[i] = random(0,10);
  }
}
