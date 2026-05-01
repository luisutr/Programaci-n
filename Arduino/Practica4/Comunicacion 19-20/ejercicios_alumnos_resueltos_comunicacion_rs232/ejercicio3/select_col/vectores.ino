// Reserva memoria para un vector char
char *reservarVectorChar(int tam) {
  return (char *) malloc(sizeof(char)*tam);
}

// Genera un vector de char de tamaño tam 
// con el formato {v0,v1,...,vtam-1}
String generaVectorChar(char *v,int tam) {
  int i;
  String s;

  s = "{";
  for(i=0;i<tam;i++) {
    if (i<(tam-1)) s += String(v[i]) + ", ";
    else s += String(v[i]) + "}";
  }
  return s;
}

