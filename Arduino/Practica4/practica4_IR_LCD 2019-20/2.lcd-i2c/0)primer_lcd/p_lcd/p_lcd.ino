#include <LiquidCrystal_I2C.h> // Necesaria para el lcd
#include <Wire.h> // Permite conectar los pines del interfaz I2C

LiquidCrystal_I2C lcd(0x27, 16, 2); // Crea objeto para lcd
//LiquidCrystal_I2C lcd(0x3F, 16, 2); // Crea objeto para lcd

byte turno; // Variable que selecciona fila a escribir

void setup() {
  turno = 1;
  Wire.begin(5, 4); // Use predefined PINS consts // conecta el I2C a pines 5 y 4
  lcd.setBacklight(HIGH); // Activa luz del fondo del lcd
  lcd.begin(16,2); // Inicia lcd indicando nº de columnas y filas
  lcd.home(); // Coloca el cursor en la esquina superior izquierda del lcd
  lcd.setCursor(0,1); // Posiciona el cursor en lcd (col 1 y fila 0)
  lcd.print("Mundo hola (1)"); // Muestra texto en posicion actual del cursor
}

void loop() {
  lcd.clear(); // limpia el lcd
  if (turno==1) {
    lcd.setCursor(0,1); // Posiciona el cursor en fila 1
    lcd.print("Mundo hola (1)"); // Muestra texto en posicion cursor
    turno = 0; // Actualizar variable de cambio de fila
  } else {
    lcd.setCursor(0,0); // Posiciona el cursor en fila 0
    lcd.print("Hola mundo (0)"); // Muestra texto en posicion cursor
    turno = 1; // Actualizar variable de cambio de fila
  }
  delay(2000);
}


