#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    Serial.begin(115200);
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print("Emmanuel");// Autor
    lcd.setCursor(0,1);
    lcd.print("Examen(1)");// Ejercicio
    delay(3000);
    lcd.clear(); 
}

void loop() {
  String opc;
  int *v_int, inic, fin;
  float *v_float;
  lcd.setCursor(0,0);
  lcd.print("1-Cuadr 2-Media ");
  lcd.setCursor(0,1);
  lcd.print("3-Pares 4-Lista ");
  opc = leerTrama('\n'); 
  
  if (opc == "1"){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Ha elegido:");
    lcd.setCursor(0,1);
    lcd.print("1-Cuad");
    delay(3000);
    lcd.clear();
    String n, numeros;
    n = leerTrama('\n');
    int N;
    N = n.toInt();
    numeros = leerTrama('\n');
    v_int = obtenListaEnteros(numeros, inic, &fin, ':', true, N);
    int resultado;
    resultado = cuadrados (v_int, N);
    Serial.println(String(resultado));
    lcd.setCursor(0,0);
    lcd.print("Resultado:");
    lcd.setCursor(0,1);
    lcd.print(resultado);
    delay(4000);
    free(v_int);
    }

  if (opc == "2"){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Ha elegido:");
    lcd.setCursor(0,1);
    lcd.print("2-Media");
    delay(3000);
    lcd.clear();
    String n, numeros;
    n = leerTrama('\n');
    int N;
    N = n.toInt();
    numeros = leerTrama('\n');
    v_float = obtenListaFloat(numeros, inic, &fin, ':', true, N);
    float resultado;
    resultado = (maximo (v_float, N) - minimo(v_float, N))/2;
    Serial.println(String(resultado));
    lcd.setCursor(0,0);
    lcd.print("Resultado:");
    lcd.setCursor(0,1);
    lcd.print(resultado);
    delay(4000);
    free(v_float);
  }

  if (opc == "3"){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Ha elegido:");
    lcd.setCursor(0,1);
    lcd.print("3-Pares");
    delay(3000);
    lcd.clear();
    String cadena;
    String resultado;
    String pares= "02468";
    cadena = leerTrama('\n');
    for (int i=0;i<cadena.length();i++){
      for(int j=0;j<pares.length();j++){
        if (cadena[i] == pares[j]){
          resultado = resultado + cadena[i];
        }
      }
    }
    Serial.println(String(resultado));
    lcd.setCursor(0,0);
    lcd.print("Resultado:");
    lcd.setCursor(0,1);
    lcd.print(resultado);
    delay(4000);
    lcd.clear();
    String ACK;
    ACK = leerTrama('\n');
    lcd.setCursor(0,0);
    lcd.print(ACK);
    delay(4000);
  }
  if (opc=="4"){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Ha elegido:");
    lcd.setCursor(0,1);
    lcd.print("4-S.Lista");
    delay(4000);
    lcd.clear();
    int inic, fin, N_1, N_2, i;
    String sec;
    sec = leerTrama('\n');
    String n;
    n = cortaTrozo(sec, inic, &fin, ':', true);
    inic=fin;
    String n_1;
    n_1 = cortaTrozo(sec, inic, &fin, ':', true);
    inic=fin;
    String n_2;
    n_2 = cortaTrozo(sec, inic, &fin, ':', true);
    N_1 = n_1.toInt();
    N_2 = n_2.toInt();
    String lista;
    if (N_1 >= N_2){
      for(i=N_2;i<=N_1;i++){
        lista = lista + i;
        if(i<N_1){
          lista = lista + ";";
        }
      }
      Serial.println(lista);
      lcd.setCursor(0,0);
      lcd.print("Lista:");
      lcd.setCursor(0,1);
      lcd.print(lista);
      delay(4000);
      lcd.clear();
     }
    if (N_2 >= N_1){
      for(int j =N_1;j<=N_2;j++){
        lista = lista + j;
        if(j<N_2){
          lista = lista + ";";
        }
      }
     Serial.println(lista);
      lcd.setCursor(0,0);
      lcd.print("Lista:");
      lcd.setCursor(0,1);
      lcd.print(lista);
      delay(4000);
      lcd.clear(); 
    }
    String suma;
    suma = leerTrama('\n');
    lcd.setCursor(0,0);
    lcd.print("Sumatorio:");
    lcd.setCursor(0,1);
    lcd.print(suma);
    delay(4000);
    lcd.clear();
    String conf = "ACK";
    Serial.println(conf);
  }
} 


String cortaTrozo(String s, int inic, int *fin, char car, bool corta) {
    int pos_car;
    pos_car = s.indexOf(car,inic); // posicion de car empezando en inic
    *fin = pos_car + 1; // fin se asigna a donde comienza el siguiente campo
    if (pos_car!=-1) return s.substring(inic,pos_car); // Entre inic y fin
    else if (corta) return s.substring(inic); // Desde inic al final
    else return String("-1"); // Error, devuelve el String "-1"
}


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


float incrementaListaEn(float v[], int tam, float M) {
      int i;
      for(i=0;i<tam;i++) {
      v[i] += M;
      }
 return M;
}


String leerTrama(char c){
        while(Serial.available() < 1){
        delay(1);
        }
 return Serial.readStringUntil(c);
}


int cuadrados(int v[], int tam) {
  int i, result = 0;
  for(i=0;i<tam;i++){
    result = result + 2*((v[i])*(v[i]));
  }
  return result;
}


float minimo(float v[], int tam) {
  int i=0;
  float minimo = v[i];
  float aux;
  for (i=0;i<tam;i++){
    aux = v[i];
    if (minimo>aux){
      minimo = aux;
      }
  }
  return minimo;
}

float maximo(float v[],int tam){
  int i=0;
  float maximo = v[i];
  float aux;
  for (i=0;i<tam;i++){
    aux = v[i];
    if (maximo<aux){
      maximo = aux;
    }
  }
  return maximo;
}
