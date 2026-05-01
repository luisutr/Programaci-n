#include <IRremoteESP8266.h>
#include <Arduino.h>
#include <IRrecv.h>

#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#define DEBUG(a) Serial.println(a);

LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
  0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
  0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,
  0xFF52AD};

String valor[21] = {"+", "-", "*", "/", "PREV", "SALIR",
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
  lcd.print(" Calculadora :"); // Muestra el menu
  lcd.setCursor(0,1); // Situa el cursor en 2ª Fila
  lcd.print("+suma -resta *mult. /divide"); // Muestra el menu
}

void loop() {
    String opc;
    do{
        //introduce el primer numero
        String s1;
        while (s1==("")){
            delay (100);
            if (irrecv.decode(&results)){
                s1=getValor(results.value);
            }
        }
        lcd.setCursor(0,1);
        lcd.print(s1);
        irrecv.resume();
        //introduce la operacion
        String operacion;
        while (operacion==("")){
            delay (100);
            if (irrecv.decode(&results)){
                operacion=getValor(results.value);
            }
        }
        if(operacion=="+") {  //La suma
            lcd.setCursor(1,1);
            lcd.print(operacion);
        }
        if(operacion=="-") {  //La suma
            lcd.setCursor(1,1);
            lcd.print(operacion);
        }
        if(operacion=="*") {  //La suma
            lcd.setCursor(1,1);
            lcd.print(operacion);
        }
        if(operacion=="/") {  //La suma
            lcd.setCursor(1,1);
            lcd.print(operacion);
        }
        irrecv.resume();
        // Recibir el siguiente valor
        String s2;
        while (s2==("")){
            delay (100);
            if (irrecv.decode(&results)){
                s2=getValor(results.value);
            }
        }
        lcd.setCursor(2,1);
        lcd.print(s2);

        lcd.setCursor(3,1); // Coloca el cursor con el igual
        lcd.print("=");
        delay(200); // Retardo para evitar rebote
        //Calcula el resultado
        int ints1, ints2;
        ints1= s1.toInt();
        ints2= s2.toInt();
        int resultado;
        if operacion == "+"{
            resultado= ints1+ints2;
        }
        if operacion == "-"{
            resultado= ints1-ints2;
        }
        if operacion == "*"{
            resultado= ints1*ints2;
        }
        if operacion == "/"{
            (float)resultado= ints1/ints2;
        }
        char char_resultado[5];
        sprintf(char_resultado,"%d",resultado);
        lcd.setCursor(4,1);
        lcd.print(char_resultado);
        delay(2000);
        lcd.clear();

        lcd.setCursor(0,0); // Situa el cursor en 1ª Fila
        lcd.print("¿Quiere salir? 1. Si 2. No"); // Muestra el menu
        lcd.setCursor(0,1); // Situa el cursor en 2ª Fila
        delay(100);
        if (irrecv.decode(&results)) { // Si se ha recibido alguna señal
            opc = getValor(results.value); // Recoge cadena desde código
        }
        lcd.print(opc)
        delay(500);
    } while(opc!="1");
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Fin");
    delay(500);
} //El del loop


String getValor(unsigned long c) {
  byte i;
  i=0;
  while( (i<21) && (claves[i]!=c) ) {
    i++;
  }
  if (i==21) return String("");
  else return String(valor[i]);
}

