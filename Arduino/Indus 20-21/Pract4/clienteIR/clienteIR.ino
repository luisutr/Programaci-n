// LCD
#include <LiquidCrystal_I2C.h> // Necesaria para el lcd
#include <Wire.h> // Permite conectar los pines del interfaz I2C

LiquidCrystal_I2C lcd(0x27, 16, 2); // Crea objeto para manejar el lcd (direccion del I2C, tamaño(16, 2))

#include <IRremoteESP8266.h> // Para el IR
#include <IRrecv.h>

// este vector de abajo es el vector que contiene el código que recibe el mandro infrarrojo
unsigned long claves[21] = {
  0xFFA25D, 0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD, 0xFFC23D, 0xFFE01F,
  0xFFA857, 0xFF906F, 0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF, 0xFF18E7,
  0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,0xFF52AD};

// cada uno de los codigos de arriba tiene su "valor" correspondiente en este vector de abajo segun lo que aparezca en el boton que corresponda 
String valor[21] = {
  "ON/OFF", "VOL+", "FUNC/STOP", "PREV", "PLAY/PAUSE", "NEXT", "DOWN", "VOL-", 
  "UP", "0", "EQ", "ST/REPT", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
  
int RECV_PIN = 0; // pin OUT del receptor IR a D3 de Arduino

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv', que es la variable que maneja el receptor IR
decode_results results;  // Crea objeto de 'decode_results', que es donde se almacenan los valores leidos por el IR

void setup() {
  Serial.begin(115200);
  // INICIALIZA EL RECEPTOR IR
  irrecv.enableIRIn(); 
  // INICIALIZA EL LCD
  Wire.begin(5, 4); // Conecta el I2C a pines 5 y 4
  lcd.setBacklight(HIGH); // Activa luz del fondo del lcd
  lcd.begin(16,2); // Inicia LCD indicando nº de columnas y filas
  lcd.home(); // Coloca el cursor en la esquina superior izquierda del lcd
  lcd.setCursor(0,0); // Posiciona el cursor en lcd (col 0 y fila 0)
  lcd.print("Evaluacion"); // Muestra texto en posicion actual del cursor
  lcd.setCursor(0,1); // Posiciona el cursor en lcd (col 0 y fila 1)
  lcd.print("logica"); // Muestra texto en posicion actual del cursor
}

void loop() {
  String mensaje, r = "";
  String cod, op1, op2, result;
  
  if (irrecv.decode(&results)) { // Si se ha recibido alguna señal

    // LEE EL CÓDIGO PULSADO
    mensaje = leerHastaRetorno();
    //+,2,3:5
    /* DECODIFICAR mensaje PARA OBTENER SUS COMPONENTES 
     *  OP1,COD, OP2 Y RESULT */
    decodifica(mensaje, &cod, &op1, &op2, &result);
    // cod = "+" op1 = "2" op2 = "3" y result="5"
    /*  ENVIAR EL MENSAJE CON EL FORMATO: OP1:COD:OP2 */
    Serial.println( op1 + ":" + cod + ":" + op2 );
    /* RECIBIR RESPUESTA DE PYTHON Y COMPARAR CON RESULT 
     * GENERARANDO LA SALIDA PARA EL LCD */
    r = leerLinea(); // recibe info hasta '\n'
    
    muestraTodoLCD(r, op1, cod, op2, result);
  }  
}
