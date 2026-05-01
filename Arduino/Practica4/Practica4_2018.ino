#include <IRremote.h>
#include <LiquidCrystal.h>
#define LED 5 // pin D1 del nodeMCU, muestra mientras atiende petición


LiquidCrystal lcd(7, 8, 9, 10, 11 , 12);//Pines que conectan el LCD con Arduino
int RECV_PIN = 0; // pin del receptor IR al pin 0 del nodeMCU
IRrecv irrecv(RECV_PIN); // Crea objeto de irrecv
decode_results results; // Crea objeto de decode_results

unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
  0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
  0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,
  0xFF52AD};

String valor[21] = {"+", "-", "*", "/", "PREV", "SALIR",
  "EQ", "#", "&", "0", "LOOP", "U/SD", "1", "2", "3", "4", "5", "6", "7", "8",
  "9"};


void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn(); // Inicializa el receptor
  lcd.begin(16, 2); // Inicia LCD
  lcd.setCursor(0,1); // Situa el cursor en 2da Fila
  lcd.write("Practica IV"); // Muestra mensaje inicial
}

void loop() {
  //Definimos variables 
  String entrada;

  String s, trama; // trama tendrá la trama recibida
  int inic, fin, opc, i, N, sol;
  int *v_int; // puntero que apunta al vector de enteros
  float *v_float, f; // puntero que apunta al vector de enteros
  trama = leerTrama('\n'); // lee la trama
  digitalWrite(LED, HIGH); // Se enciende mientras procesa
  s = cortaTrozo(trama, 0, &fin, ':', true); // s (String) recibe la opcion
  inic=fin; // Apuntamos al principio del siguiente campo de la trama
  opc = s.toInt(); // La opción (s) se convierte a entero
  // OBTENER N
  s = cortaTrozo(trama, inic, &fin, ':', true); // s recibe N como String
  inic=fin; // Apuntamos al principio del siguiente campo de la trama
  N = s.toInt(); // N (s) se convierte a entero
  // Estudio de cada petición
  if (opc==1) {
          // v_int contiene el vector de N enteros
          v_int = obtenListaEnteros(trama, inic, &fin, ':', true, N);
          sol = sumaListaEnteros(v_int, N); // devuelve la suma N enteros
          Serial.println( String(sol) ); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
          
  } 
  if (opc==2) {
    // v_float contiene el vector de N float
    v_float = obtenListaFloat(trama, inic, &fin, ':', true, N);
    inic = fin; // Apuntamos al principio del siguiente campo
    // s recibe el float a sumar
    s = cortaTrozo(trama, inic, &fin, ':', true);
    inic=fin; // Apuntamos al principio del siguiente campo
    f = s.toFloat(); // s se convierte a float y se almacena en f
    incrementaListaEn(v_float, N, f); // aumenta cada valor de v_float
    s = String(""); // s contendrá la trama a enviar a Python
    for(i=0;i<N;i++) {
      s += String(v_float[i]);
      if (i!=N-1) s += String(':');
    }
    Serial.println( s ); // Se envía la trama a Python
    free(v_float); // IMPORTANTE: Libera la memoria de v_float
  }
  
  if(opc==3){
    //Elegimos la columna sobre la que queremos escribir y la rellenamos
  }
  if(opc==4){
      float resultado = 0.00;
      Serial.write("Resultado"); 
      lcd.clear();
      char char_resultado[5];
      sprintf(char_resultado,"%d",resultado);
      lcd.print(char_resultado);
      delay(2000);
  }
 if(opc==5){
      Serial.write("Resultado");    
  }
  if(opc==6){
    Serial.write("Resultado"); 
  }
  digitalWrite(LED, LOW); // Se apaga al terminar de procesar
}


// Funcion que devuelve como String el contenido entre dos "car" (carácter)
// comenzando en "inic" y hasta que se encuentra un "car", fin tendrá el
// índice donde comienza el siguiente campo

String cortaTrozo(String s, int inic, int *fin, char car, bool corta) {
  int pos_car;
  pos_car = s.indexOf(car,inic); // posicion de car empezando en inic
  *fin = pos_car + 1; // fin se asigna a donde comienza el siguiente campo
  if (pos_car!=-1) return s.substring(inic,pos_car); // Entre inic y fin
  else if (corta) return s.substring(inic); // Desde inic al final
  else return String("-1"); // Error, devuelve el String "-1"
}

// Devuelve un vector de N enteros a partir de la trama comenzando en "inic"
int *obtenListaEnteros(String linea, int inic, int *fin, char car, bool c, int N) {
  int *v_int, i;
  String s;
  v_int = (int *) malloc(sizeof(int)*N); // Reserva de memoria
  for(i=0;i<N;i++) { // Para cada trozo
    s = cortaTrozo(linea, inic, fin, car, c); // s = v_i como String
    inic=*fin; // Apuntamos al principio del siguiente campo
    v_int[i] = s.toInt(); // s se convierte a entero y se almacena
  }
  return v_int; // Devolución del vector
}
// Devuelve un vector de tam float a partir de la trama comenzando en "inic"
float *obtenListaFloat(String linea, int inic, int *fin, char car, bool c, int N) {
  float *v_float;
  int i;
  String s;
  v_float = (float *) malloc(sizeof(float)*N);
  for(i=0;i<N;i++) { // Para cada trozo
    s = cortaTrozo(linea, inic, fin, car, c); // s = v_i como String
    inic=*fin; // Apuntamos al principio del siguiente campo
    v_float[i] = s.toFloat(); // s se convierte a float y se almacena
  }
  return v_float; // Devolución del vector
}

// Devuelve la suma de los valores enteros en el vector v
int sumaListaEnteros(int v[], int tam) {
  int i, r = 0;
  for(i=0;i<tam;i++) {
    r += v[i];
  }
  return r;
}
// Incrementa cada valor del vector v en f
float incrementaListaEn(float v[], int tam, float M) {
  int i;
  for(i=0;i<tam;i++) {
    v[i] += M;
  }
  return M;
}
// Función que lee una trama terminada en car

String leerTrama(char c) {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil(c); // Recibe info hasta '\n'
}

String getValor(unsigned long c) {
  byte i;
  i=0;
  while( (i<21) && (claves[i]!=c) ) {
    i++;
  }
  if (i==21) return String("");
  else return String(valor[i]);
}

String funcion_escanear(){
  String var;
  do{
    delay (100);
    if (irrecv.decode(&results)) { // Si se ha recibido alguna sennal
      var = getValor(results.value); // Recoge cadena desde código
      irrecv.resume(); // Recibir el siguiente valor
    }
  }while (var==(""));
}
/*
String leerLinea() {
  // Espera hasta que haya algo que leer
  // BUCLE TOTALMENTE NECESARIO
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil("\n"); // Recibe info hasta ’\n’
}

*/

// FUNCIONES PRACTICA 2

int sumatorio (int a, int b){
  int sum=0;
  for(a;a<=b;a++){
    sum+=a;
  }
  return sum;
}

int *cuadrados(int v[],int n){
  int *cuadrados;
  for (int i=0; i<n;i++){
    cuadrados[i]=(v[i])*(v[i]);
  } 
  return cuadrados;
}

int *vecesletra(String texto, char letras[], int n){
  int *vecesletras;
  int len = texto.length();
  for (int i=0;i<=len;i++){
    for (int j=0; j<n;j++){
      if (texto[i]==letras[j]){
        vecesletras[j]++;
      }
    }  
  }
  return vecesletras;
}


