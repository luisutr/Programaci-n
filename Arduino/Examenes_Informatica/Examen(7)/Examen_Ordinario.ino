const int led_blanco = 2;
const int led_verde  = 15;
const int led_amarillo = 14;
const int led_rojo = 12;

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    Serial.begin(115200);
    pinMode(led_blanco, OUTPUT);
    pinMode(led_verde, OUTPUT);
    pinMode(led_amarillo, OUTPUT);
    pinMode(led_rojo, OUTPUT);
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0,0);
    lcd.print("Emmanuel");// Autor
    lcd.setCursor(0,1);
    lcd.print("Examen_Ordinario");// Ejercicio
    delay(3000);
    lcd.clear();
}

void loop() {
  String sec, opc, n;
  int inic, fin, *v_int, N;
  sec = leerTrama('\n');
  opc = cortaTrozo(sec, inic, &fin, ':', true); 
  inic = fin;
  if(opc == "1") {
    n = cortaTrozo(sec, inic, &fin, ':', true);
    inic = fin;
    N = n.toInt();
    v_int = obtenListaEnteros(sec, inic, &fin, ':', true, N);
    for (int i=0;i<N;i++){
      if( v_int[i] == 0 ){
        digitalWrite(led_blanco, HIGH);
      }
      if( v_int[i] == 1 ){
        digitalWrite(led_verde, HIGH);
      }
      if( v_int[i] == 2 ){
        digitalWrite(led_amarillo, HIGH);
      }
      if( v_int[i] == 3 ){
        digitalWrite(led_rojo, HIGH);
      }
    }
   String conf = "OK";
   Serial.println(conf);
   free (v_int);  
  }
 if(opc =="2") {
   digitalWrite(led_rojo, LOW);
   digitalWrite(led_amarillo, LOW);
   digitalWrite(led_verde, LOW);
   digitalWrite(led_blanco, LOW);
   String conf = "OK";
   Serial.println(conf);
  }
 if (opc =="3") {
    n = cortaTrozo(sec, inic, &fin, ':', true);
    inic = fin;
    N = n.toInt();
    v_int = obtenListaEnteros(sec, inic, &fin, ':', true, N);
    for (i 
  }
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

String cortaTrozo(String s, int inic, int *fin, char car, bool corta) {
    int pos_car;
    pos_car = s.indexOf(car,inic); // posicion de car empezando en inic
    *fin = pos_car + 1; // fin se asigna a donde comienza el siguiente campo
    if (pos_car!=-1) return s.substring(inic,pos_car); // Entre inic y fin
    else if (corta) return s.substring(inic); // Desde inic al final
    else return String("-1"); // Error, devuelve el String "-1"
}

String leerTrama(char c){
        while(Serial.available() < 1){
        delay(1);
        }
 return Serial.readStringUntil(c);
}
