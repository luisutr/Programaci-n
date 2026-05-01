void setup() {
  Serial.begin(115200);
}

void loop() {
  float r, *f;
  int tam, *v; // Se accede con los índices del 0 al TAM-1

  // Lee el vector de float desde el Puerto RS-232
  // El puntero f recoge el vector y el parametro tam
  // por referencia recibe el tamaño
  f = generarVectorFloatDesdeMensaje(&tam);
  // Redondea el vector f devolviendo en v el vector redondeado
  v = redondea_vector(f, tam);
  // Envía el vector redondeado con formato: tam:f0,f1,...ftam-1
  enviarVectorEntero(v, tam);
  // Envia el vector float con formato: tam:f0,f1,...ftam-1
  enviarVectorFloat(f, tam);
  // Libera la memoria reservada para el vector
  // por la función generarVectorEnterosDesdeMensaje
  free(v);
  free(f);
}

int *redondea_vector(float f[], int tam) {
  int i, *v;
  v = (int *) malloc(sizeof(int)*tam);
  for(i=0; i<tam; i++) {
    v[i] = (int) f[i];
  }
  return v;
}
