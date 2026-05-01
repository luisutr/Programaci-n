// Reserva memoria para un vector char
char *reservarVectorChar(int tam) {
  return (char *) malloc(sizeof(char)*tam);
}

// Muestra un vector de char de tamaño tam
void mostrarVectorChar(char *v,int tam) {
  int i;

  Serial.print("[");
  for(i=0;i<tam;i++) {
    if (i<(tam-1)) Serial.print( String(v[i]) + ", " );
    else Serial.print( String(v[i]) );
  }
  Serial.println("]");
}

