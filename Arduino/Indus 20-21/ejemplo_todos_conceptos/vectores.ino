
// Reserva memoria para entero
int *reservar(int tam) {
  return (int *) malloc(sizeof(int)*tam);
}

// Libera memoria asignada a un entero
void liberar(int *v) {
  free(v);
}

void enviarVectorEntero(int v[], int tam) {
  int i;
  String s="";
  s = String(tam) + ":";
  for(i=0; i<tam; i++) {
    if (i!=tam-1) s += String(v[i]) + ","; // si no es el último
    else s += String(v[i]); // el último envía sin ", "
  }
  Serial.println( s );
}
