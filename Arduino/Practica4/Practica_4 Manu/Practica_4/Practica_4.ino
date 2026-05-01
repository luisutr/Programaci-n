
#define LED 5 // pin D1 del nodeMCU, muestra mientras atiende petición

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);


void setup() {
        Serial.begin(115200);
        pinMode(LED, OUTPUT);
        lcd.init();
        lcd.backlight();
        lcd.setCursor(0,0); // 
        lcd.print("Emmanuel");// Autor
        lcd.setCursor(0,1);
        lcd.print("Practica IV");
        delay(4000);
        lcd.clear(); 
}

void loop() {        
        String s, trama; // trama tendrá la trama recibida
        int inic, fin, opc, i, N, sol;
        float sol_d;
        int *v_int; // puntero que apunta al vector de enteros
        float *v_float, f; // puntero que apunta al vector de enteros
        trama = leerTrama('\n'); // lee la trama
        digitalWrite(LED, HIGH); // Se enciende mientras procesa
        s = cortaTrozo(trama, 0, &fin, ':', true); // s (String) recibe la opcion
        inic=fin; // Apuntamos al principio del siguiente campo de la trama
        opc = s.toInt(); //


        if (opc==1) {
          v_int = obtenListaEnteros(trama, inic, &fin, ',', true, 2);
          sol = suma(v_int[0],v_int[1]); // devuelve la suma de los enteros
          Serial.println(String(sol)); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
          }
         
        if (opc==2) {
          v_int = obtenListaEnteros(trama, inic, &fin,',' , true, 2);
          sol = resta(v_int[0],v_int[1]); // devuelve la resta de los enteros
          Serial.println(String(sol)); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
          } 
          
        if (opc==3) {
          v_int = obtenListaEnteros(trama, inic, &fin,',' , true, 2);
          sol = multp(v_int[0],v_int[1]); // Devuelve la multiplicacion de los enteros
          Serial.println(String(sol)); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
          }  

        if (opc==4) {
          v_float = obtenListaFloat(trama, inic, &fin,',' , true, 2);
          sol_d = divid(v_float[0],v_float[1]); // Devuelve la división de los enteros en un float
          Serial.println(float(sol_d)); // Envia a Pyhton el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
          }
          
          digitalWrite(LED, LOW); // Se apaga al terminar de procesar
}


//Funciones utilizadas en el guion de la práctica//

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

//Funciones Suma,Resta,Multiplicacion,Division//
int suma ( int a, int b){
  int suma=0;
  suma = a + b;
  return suma;
}

int resta ( int a, int b){
  int resta=0;
  resta = a - b;
  return resta;
}

int multp ( int a, int b){
  int multp=0;
  multp = a * b;
  return multp;
}

float divid ( float a, float b){
  float divid=0;
  divid = a / b;
  return divid;
}



      
