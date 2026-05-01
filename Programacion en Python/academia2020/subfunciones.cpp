//------------------ SUBFUNCIONES NECESARIAS -------------------

int *trozo_entre_min_max(int v[], int tam, int *posminpri, int* posminseg){
  int *pm, *sm;
  pm = reservar(tam/2)
  sm = reservar(tam/2)
  pm = cogeprimeramitad(v, tam)
  sm = cogesegundamitad(v, tam)
  *posminpri = calculaposmin(pm, tam/2)
  *posminseg = calculaposmin(sm, tam/2)
  // Nos queda cortar el trozo del vectar v entre esas dos posiciones 
  // y devolverlo 
  return 0;
}


int *reservar(int tam) {
  return (int *)malloc(sizeof(int)*tam);
}

void liberar(int *v) {
  free(v);
}

void rellenaVectorEnteroAleatorioEntre(int v[], int tam, int a, int b) {
  int i;
  // Inicializa el vector v con valores aleatorios
  for (i = 0; i < tam; i++) {
    v[i] = random(a, b);
  }
}

void mostrar(int *v,int tam) {
  int i;

  Serial.print("[");
  for(i=0;i<tam;i++) {
    if (i<(tam-1)) Serial.print( String(v[i]) + ", " );
    else Serial.print( String(v[i]) );
  }
  Serial.println("]");
}
String leerLinea() {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil('\n');
}

int leerEntero(String s) {
  String r;
  Serial.println(s);
  r = leerLinea();
  return r.toInt(); 
}