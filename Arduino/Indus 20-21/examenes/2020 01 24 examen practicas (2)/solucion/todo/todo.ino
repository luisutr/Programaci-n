#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#define FIL 4
#define COL 3

LiquidCrystal_I2C lcd(0x27, 16, 2);

int fila = 0; // Indica fila a usar
int pos = 0; // Posicion dentro de la fila

void setup() { 
  Serial.begin(115200);
  Wire.begin(5, 4); // Pines del nodeMCU a usar
  lcd.setBacklight(HIGH); 
  lcd.begin(16,2);
  lcd.home();
  lcd.setCursor(pos, fila); // Posicion inicial del cursor
  lcd.print(""); // Mensaje inicial
}

void loop() {
  int inic;
  String opc, mensaje;

  // Lee el mensaje enviado desde el PC
  mensaje = leerLinea();
  
  // Obtiene la opción y la deja en el String opc
  inic = 0;
  opc = cortaTrozo(mensaje, inic, &inic, ':', true); // s recibe la opción como String
  mensaje = mensaje.substring(inic); // quita el tamaño y el ':' de mensaje

  // Selección de opciones
  if (opc=="1") solucion_ejercicio1(opc, mensaje);
  else if (opc=="2") solucion_ejercicio2(opc, mensaje);
  else if (opc=="3") solucion_ejercicio3(opc, mensaje);
}
