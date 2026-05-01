
void setup() {
  Serial.begin(115200);
}
void loop() {
  int n,*vect;
  float medianumref;
  n = leerEntero("Dime una longitud para el vector");
  vect=reservar(n);
  rellenaVectorEntero(vect, n);
  Serial.println("Calculo media "+String(n)+"-"+String(vect[n-1]));
  mediaref(vect, n, &medianumref);
  Serial.println("La media es " + String(medianum));
  liberar(vect);
}
void mediaref (int v[], int tam, float *med){
  int i;
  *med = 0;
  for (i = 0 ; i < tam ; i++){
    *med += v[i];
   }  
   *med = (float) *med / tam ;
    
 }