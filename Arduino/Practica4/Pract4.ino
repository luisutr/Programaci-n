void setup() {
  randomSeed(analogRead(0));
  Serial.begin(115200);
}

void loop() {
  int i, *p=NULL, *p1, *s;
  int tam;

  tam = random(0,10); // tamanno aleatorio
  Serial.println("Tamano: " + String(tam));

  p = reserva(tam); // reserva memoria primer vector
  rellenaAleatorio(p,tam); // Rellena aleatoriamente
  mostrar(p, tam); // Muestra primer vector

  p1 = reserva(tam); // reserva memoria segundo vector  
  rellenaAleatorio(p1,tam); // Rellena aleatoriamente
  mostrar(p1, tam); // Muestra segundo vector

  s = menores(p, p1, tam); // devuelve vector salida
  mostrar(s, tam); // Muestra resultado

  free(p); // Libera cuando ya no hace falta
  free(p1); // Libera cuando ya no hace falta
  free(s); // Libera cuando ya no hace falta
  delay(2000);
}

int *menores(int *v1, int *v2, int tam) {
  int i, *r;
  r = reserva(tam); // reserva memoria
  for(i=0;i<tam;i++) {
    if (v1[i]<v2[i]) {
      r[i]=v1[i];
    } else {
      r[i]=v2[i];
    }
  }
  return r;
}

int *reserva(int n) {
  int *p;
  p = (int *) malloc( sizeof(int) * n);
  return p;
}

void rellenaAleatorio(int p[], int tam) {
  int i; 
  for(i=0;i<tam;i++) {
    p[i] = random(0,10);
  }
}
void mostrar(int *p, int n) {
  int i;
  Serial.print(" = ");
  for(i=0;i<n;i++) {
    Serial.print(String(p[i]) +" ");
  }
  Serial.println("");
}
