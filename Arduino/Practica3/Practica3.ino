#include <IRremoteESP8266.h>
#include <IRrecv.h>

#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#define DEBUG(a) Serial.println(a);

LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
  0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
  0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,
  0xFF52AD};

String valor[21] = {"+", "-", "*", "/", "PREV", "NEXT",
  "EQ", "#", "&", "0", "LOOP", "U/SD", "1", "2", "3", "4", "5", "6", "7", "8",
  "9"};

int RECV_PIN = 0; // pin del receptor IR al pin 0 del nodeMCU

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv'
decode_results results; // Crea objeto de 'decode_results'


void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn(); // Inicializa el receptor
  Wire.begin(5, 4);
  lcd.setBacklight(HIGH); //Use predefined PINS consts
  lcd.begin(16,2);
  lcd.home();
  lcd.clear();
  lcd.setCursor(0,0); // Situa el cursor en 1ª Fila
  lcd.print(" +.SUMA -.RESTA"); // Muestra el menu
  lcd.setCursor(0,1); // Situa el cursor en 2ª Fila
  lcd.print(" *.MULTI /.DIV"); // Muestra el menu  
}

void loop() {
  String opc;
  if (irrecv.decode(&results)) { // Si se ha recibido alguna señal
    opc = getValor(results.value); // Recoge cadena desde código
    if(opc=="+") {  //La suma
      //Serial.println( "[" + s + "]" );          Esto para que coño vale??
      irrecv.resume(); // Recibir el siguiente valor
      escribeOpcion (opc);
      lcd.setCursor(1,0);
      lcd.print("Suma");
      String s1;
      if (irrecv.decode(&results)){
        s1=getValor(results.value);
        lcd.setCursor(1,1);
        lcd.print(s1);
      }
      String s2;
      irrecv.resume(); // Recibir el siguiente valor
      if (irrecv.decode(&results)){
        s2=getValor(results.value);
        lcd.setCursor(3,1);
        lcd.print(s2);
      }
        //---------------------------------------------------Falta el if de los resultados
      int ints1, ints2;
      ints1 = s1.toInt();
      DEBUG(ints1);
      ints2 = s2.toInt();
      DEBUG(ints2);      
      int resultado;
      resultado= ints1+ints2;
      String char_resultado;
      char_resultado=char(resultado);
      lcd.setCursor(5,1);
      lcd.print(char_resultado);
      irrecv.resume(); // Recibir el siguiente valor
    } else if (opc=="-"){ //La resta
      //Serial.println( "[" + s + "]" );          Esto para que coño vale??
      irrecv.resume(); // Recibir el siguiente valor
      escribeOpcion (opc);
      lcd.setCursor(1,0);
      lcd.print("Resta");
      String r1, r2;
      if (irrecv.decode(&results)){
        r1=getValor(results.value);
        lcd.setCursor(1,1);
        lcd.print(r1);
      }
      irrecv.resume(); // Recibir el siguiente valor
      if (irrecv.decode(&results)){
        r2=getValor(results.value);
        lcd.setCursor(3,1);
        lcd.print(r2);
      }
        //---------------------------------------------------Falta el if de los resultados
      irrecv.resume(); // Recibir el siguiente valor
    } else if (opc=="*"){ //La multiplicacion
      //Serial.println( "[" + s + "]" );          Esto para que coño vale??
      irrecv.resume(); // Recibir el siguiente valor
      escribeOpcion (opc);
      lcd.setCursor(1,0);
      lcd.print("Multiplicacion");
      String m1, m2;
      if (irrecv.decode(&results)){
        m1=getValor(results.value);
        lcd.setCursor(1,1);
        lcd.print(m1);
      }
      irrecv.resume(); // Recibir el siguiente valor
      if (irrecv.decode(&results)){
        m2=getValor(results.value);
        lcd.setCursor(3,1);
        lcd.print(m2);
      }
      //---------------------------------------------------Falta el if de los resultados
      irrecv.resume(); // Recibir el siguiente valor
    } else if (opc=="/"){ //La division
      //Serial.println( "[" + opc + "]" );          Esto para que coño vale??
      irrecv.resume(); // Recibir el siguiente valor
      escribeOpcion (opc);
      lcd.setCursor(1,0);
      lcd.print("Division");
      String d1, d2;
      if (irrecv.decode(&results)){
        d1=getValor(results.value);
        lcd.setCursor(1,1);
        lcd.print(d1);
      }
      irrecv.resume(); // Recibir el siguiente valor
      if (irrecv.decode(&results)){
        d2=getValor(results.value);
        lcd.setCursor(3,1);
        lcd.print(d2);
      }
        //---------------------------------------------------Falta el if de los resultados
      irrecv.resume(); // Recibir el siguiente valor
    }
  } //El de que ha recibido alguna señal
} //El del loop

void escribeOpcion(String opc) {
  lcd.clear();
  lcd.setCursor(2,1); // Coloca el cursor en la fila 0
  lcd.print(opc);
  lcd.setCursor(4,1);
  lcd.print("=");
  delay(200); // Retardo para evitar rebote
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

