#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int fila = 0; // Indica fila a usar
int pos = 0; // Posicion dentro de la fila

void setup() { 
  Wire.begin(5, 4); // Pines del nodeMCU a usar
  lcd.setBacklight(HIGH); 
  lcd.begin(16,2);
  lcd.home();
  lcd.setCursor(pos, fila); // Posicion inicial del cursor
  lcd.print(""); // Mensaje inicial
}

void loop() {
  lcd.clear(); // Limpia LCD
  if (fila==0) { // Si fila 0
    lcd.setCursor(pos,0); // posiciona cursor
    lcd.print("0"); // muestra un 0
    fila = 1; // Cambio a fila 1
  } else {
    lcd.setCursor(pos,1); // posiciona cursor
    lcd.print("1"); // muestra un 1
    fila = 0; // Cambio a fila 1
    pos = (pos+1) % 16; // Incrementa y si es 16 pasa a 0
  }  
  delay(1000); // Retardo para visualizar
}


