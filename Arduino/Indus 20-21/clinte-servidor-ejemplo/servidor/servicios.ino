// Devuelve la suma de los valores enteros en el vector v
int sumaListaEnteros(int v[], int tam) {
  int i, r = 0;
  for(i=0;i<tam;i++) {
    r += v[i];
  }
  return r;
}
// Incrementa cada valor del vector v en f
float incrementaListaEn(float v[], int tam, float f) {
  int i;
  for(i=0;i<tam;i++) {
    v[i] += f;
  }
}

