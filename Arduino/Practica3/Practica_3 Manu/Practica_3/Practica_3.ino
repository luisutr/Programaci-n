#include <IRremoteESP8266.h>
#include <IRrecv.h>

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,
0xFF52AD};

String valor[21] = {"CH-", "CH", "CH+", "PREV", "NEXT", "PLAY/PAUSE",
"-", "+", "EQ", "0", "100+", "200+", "1", "2", "3", "4", "5", "6", "7", "8",
"9"};


int RECV_PIN = 2; // pin del receptor IR al pin D4 del nodeMCU

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv'
decode_results results; // Crea objeto de 'decode_results'
int contador = 0;
String letras = "ABCDEFGHIJK";
String numeros="123456789";
String sel ;
String lectura ="";
String digitos ="";
void setup() {
        Serial.begin(115200);
        irrecv.enableIRIn(); // Inicializa el receptor
        lcd.init();
        lcd.backlight();
        lcd.setCursor(0,0); // 
        lcd.print("Emmanuel");// Autor
        lcd.setCursor(0,1);
        lcd.print("Practica III");
        delay(4000);
        lcd.clear(); 
}


void loop() {
      lcd.setCursor(0,0);
      lcd.print("1#Lectu 2#Letras");
      lcd.setCursor(0,1);
      lcd.print("3#Digitos");
      delay(2000);
      lcd.clear();
      if (irrecv.decode(&results)){
          sel=getValor(results.value);
          irrecv.resume();
      if (sel =="1") {
          String boton = "1";
            while (boton !="0") {
              delay(200);
              if (irrecv.decode(&results)){
                 boton=getValor(results.value);
                 irrecv.resume();
                 lectura=boton+lectura;
              }
          escribeLCD_lectura(lectura);
          delay(200);        
          }
      }
      if (sel =="2") {
        for(int i=0; i<lectura.length(); i++){ 
            for(int j=0; j<letras.length(); j++){
                  if (lectura[i] == letras[j]){
                    contador ++;
                  } 
            }
        }
      escribeLCD_letras(String(contador)); 
      delay(6000);
      contador=0;
      }
      if (sel=="3"){
              for (int i=0;i<lectura.length();i++){  
                  for (int j=0;j<numeros.length();j++){
                      if (lectura[i] == numeros[j]){
                          digitos = digitos + lectura[i];    
                      }
                  } 
              }
      escribeLCD_digitos(digitos);
      delay(6000);
      digitos="";    
      }               
      }
}


void escribeLCD_lectura(String s) {
  lcd.clear(); // 
  if(s!="") {
  lcd.setCursor(0,0); // 
  lcd.print("Lectura:");
  lcd.setCursor(0,1); 
  lcd.print(s); 
  delay(200); 
  }
}

void escribeLCD_letras(String s) {
  lcd.clear(); 
  if(s!="") {
  lcd.setCursor(0,0); 
  lcd.print("N'Letras:");
  lcd.setCursor(0,1); 
  lcd.print(s); 
  delay(200); 
  }
}

void escribeLCD_digitos(String s) {
  lcd.clear(); 
  if(s!="") {
  lcd.setCursor(0,0); 
  lcd.print("Digitos:" );
  lcd.setCursor(0,1); 
  lcd.print(s); 
  delay(200); 
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
