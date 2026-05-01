// Calcula la media de los elementos de v y
// devuelve el resultado por referencia en r
void media(int v[], int tam, float *r) {
  int i;

  *r = 0;
  for(i=0;i<tam;i++) {
    *r += v[i];
  }
  *r = (float) *r/tam;
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  float result;
  int n, *p;  // int p[n] 

  n = leerEntero("Dame el número de valores a almacenar");
  p = reservar(n); 
  // Rellena el vector entero
  rellenaVectorEntero(p, n);
  // Devuelve la media en result
  media(p, n, &result);
  // Mostrar resultado
  Serial.println( "Vector leido: " );
  mostrar(p, n);
  Serial.println( "La media del vector es: " + String(result) );
  // liberar memoria vector
  liberar(p);
}
