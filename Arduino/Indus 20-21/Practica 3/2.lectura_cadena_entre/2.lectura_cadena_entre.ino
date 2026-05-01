/*
 * Conecta keypad utilizando el i2c. Es necesaria la libreria Keypad_I2C.
 * Se debe bajar la libreria Keypad_I2C de la direccion https://github.com/joeyoung/arduino_keypads
 * y copiar en la carpeta libraries de Arduino con el nombre de carpera "Keypad_I2C". 
 * La libreria keypad se instala haciendo clic en"Programa/Incluir libreria/Gestor librerias",
 * entonces se busca "keypad" y se instala la de "Mark Stanley, Alexander Brevig"
 */
/*
 * Conexiones:
 *    SDA -> D2
 *    SCL -> D1
 *    VCC -> 3.3V
 *    GND -> GND
 */

#include <Keypad_I2C.h>
#include <Keypad.h>        // GDY120705
// la librería comunica el nodeMCU (o arduino) con 
// dispositivos que usan el protocolo I2C/TWI
#include <Wire.h> 
#define I2CADDR 0x20

const byte ROWS = 4; // Cuatro filas
const byte COLS = 4; // Cuatro columnas
// Define los simbolos de los botones del keypad
char hexaKeys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte colPins[COLS] = {3, 2, 1, 0}; // Conecta a los pinouts de la fila del keypad
byte rowPins[ROWS] = {7, 6, 5, 4}; // Conecta a los pinouts de la columna del keypad

// Inicializa una instancia de la clase Keypad_I2C
Keypad_I2C customKeypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS, I2CADDR); 

void setup(){
  customKeypad.begin( ); // GDY120705
  Serial.begin(115200);
}

void loop(){
  Serial.println( "Introduce una cadena que comience y acabe en '#' y '*' respectivamente" );
  Serial.println( leer_cadena_entre("#", "*") );
}

char leerTeclaKeypad() {
  char customKey = customKeypad.getKey();

  while (customKey == NO_KEY) {
    customKey = customKeypad.getKey();
    delay(10);
  }
  return customKey;
}

String leer_cadena_entre(String inicio, String fin) {
  String r="", s;

  // Lee hasta que se lee el inicio de la cadena
  do {
    s = leerTeclaKeypad(); 
  } while (s!=inicio);
  // Lee la cadena
  do {
    s = leerTeclaKeypad();
    if (s!=fin) {
      r += s; 
    }
  } while (s!=fin);
  return String(r);
}

