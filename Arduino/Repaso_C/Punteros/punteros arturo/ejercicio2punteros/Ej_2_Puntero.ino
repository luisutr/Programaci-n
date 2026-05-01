void setup() {
  Serial.begin(115200);

}

void loop() {
  int n, *vect, *vec_pares, *numero_pares, num_pares;
  n = leerEntero("Dime una longitud para el vector");
  vect = reservar(n);
  rellenaVectorEntero(vect,n);
  Serial.println("Hasta aqui bien");
  mostrar(vect,n);
  vec_pares = pares(vect,n,&num_pares);
  Serial.println("Y aqui tambien<");
  mostrar(vec_pares,num_pares);
  liberar(vect);
  liberar(vec_pares); 
}

int* pares(int v[], int tam, int *elementos){
  int i, *numero_pares;
  *elementos = 0;
  for (int j = 0; j < tam; j++){
    if (j % 2 ==0){
      (*elementos)++;
    }
  }
  numero_pares = reservar((*elementos));
  int pos = 0;
  for (i = 0; i < tam ; i++){
    if (v[i]%2==0){
    numero_pares[pos] = v[i];
    pos++;
  }}
  return numero_pares;
}
