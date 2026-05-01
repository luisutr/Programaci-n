void media (int v[], int tam, float *x){
  int i;
  *x = 0;
  for (i = 0 ; i < tam ; i++){
    *x += v[i];
   }  
   *x = (float) *x / tam ;
    
 }
void setup() {
  Serial.begin(115200);
  

}

void loop() {
  int n,*vect;
  float medianum;
  n = leerEntero("Dime una longitud para el vector");
  vect=reservar(n);
  rellenaVectorEntero(vect, n);
  Serial.println("Calculo media "+String(n)+"-"+String(vect[n-1]));
  media(vect, n, &medianum);
  Serial.println("La media es " + String(medianum));
  liberar(vect);
}
