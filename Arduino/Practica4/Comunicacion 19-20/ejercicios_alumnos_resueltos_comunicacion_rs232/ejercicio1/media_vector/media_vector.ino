void setup() {
  Serial.begin(115200);
}

void loop() {
  float r;
  int *v, tam; // Se accede con los índices del 0 al TAM-1

  // Lee el vector de enteros desde el Puerto RS-232
  // El parametro v recoge el vector y el parametro
  // por referencia recibe el tamaño
  v = generarVectorEnterosDesdeMensaje(&tam);
  // Calcula la media devolviendo en valor en r
  r = media(v, tam);
  // Envía la media obtenida al PC
  Serial.println( String(r) );
  // Libera la memoria reservada para el vector
  // por la función generarVectorEnterosDesdeMensaje
  free(v);
}

// Calcula la media de los elementos de un vector
float media(int v[], int tam) {
  int i;
  float r;
  for(i=0; i<tam; i++) r += v[i];
  return r/tam;
}
