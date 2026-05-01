#include <IRremoteESP8266.h>
#include <IRrecv.h>

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long claves[21] = {
  0xFFA25D, 0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD, 0xFFC23D, 0xFFE01F,
  0xFFA857, 0xFF906F, 0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF, 0xFF18E7,
  0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,0xFF52AD};

String valor[21] = {
  "ON/OFF", "MODE", "VolOFF", "PLAY/PAUSE", "PREV", "NEXT", "EQ", "-", 
  "+", "0", "LOOP", "U/SD", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

int RECV_PIN = 0; // pin del receptor IR al pin 0 del nodeMCU

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv'
decode_results results;  // Crea objeto de 'decode_results'

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn(); // Inicializa el receptor
  Wire.begin(5, 4);
  lcd.setBacklight(HIGH); //Use predefined PINS consts
  lcd.begin(16,2);
  lcd.home();
  lcd.setCursor(0,1); // Situa el cursor en 2ª Fila
  lcd.print("Practicas II"); // Muestra mensaje inicial
}

void loop() {
  String s;
  if (irrecv.decode(&results)) { // Si se ha recibido alguna señal
    s = getValor(results.value); // Recoge cadena desde código
    if(s!="") {
      Serial.println( "[" + s + "]" );
      escribeLCD(s); // Escribo en LCD
    }    
    irrecv.resume(); // Recibir el siguiente valor
  }  
}

void escribeLCD(String s) {
  lcd.clear(); // Limpia el LCD
  if(s!="") {
    lcd.setCursor(0,0); // Coloca el cursor en la fila 0 
    lcd.print(s);
  } else { 
      lcd.setCursor(0,1); // Coloca cursor en fila 1
      lcd.print( "--- Rebote ---"); // Muestra mensaje rebote
  }
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

