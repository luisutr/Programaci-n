// Reserva memoria para entero
int *reservar(int tam) {
  return (int *) malloc(sizeof(int)*tam);
}

// Libera memoria asignada a un entero
void liberar(int *v) {
  free(v);
}

// Muestra un vector de enteros de tamaño tam
void mostrar(int *v,int tam) {
  int i;

  Serial.print("[");
  for(i=0;i<tam;i++) {
    if (i<(tam-1)) Serial.print( String(v[i]) + ", " );
    else Serial.print( String(v[i]) );
  }
  Serial.println("]");
}

// Rellena vector de enteros de tamaño tam
void rellenaVectorEntero(int v[], int tam) {
  int i;
  // Inicializa el vector v con valores aleatorios
  for(i=0; i<tam; i++) {
    v[i] = leerEntero("Dame un entero");
    Serial.println( v[i] );
  }
}
