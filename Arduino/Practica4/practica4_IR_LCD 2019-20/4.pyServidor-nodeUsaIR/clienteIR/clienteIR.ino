#include <IRremoteESP8266.h>
#include <IRrecv.h>

unsigned long claves[21] = {
  0xFFA25D, 0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD, 0xFFC23D, 0xFFE01F,
  0xFFA857, 0xFF906F, 0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF, 0xFF18E7,
  0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,0xFF52AD};
  
String valor[21] = {
  "ON/OFF", "MODE", "VolOFF", "PLAY/PAUSE", "PREV", "NEXT", "EQ", "-", 
  "+", "0", "LOOP", "U/SD", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

int RECV_PIN = 0; // pin OUT del receptor IR a D3 de Arduino

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv'
decode_results results;  // Crea objeto de 'decode_results'

void setup() {
  Serial.begin(115200);
  irrecv.enableIRIn(); // Inicializa el receptor
}

void loop() {
  String s, r = "";
  if (irrecv.decode(&results)) { // Si se ha recibido alguna señal

    // Lee el código pulsado y envía a programa python
    s = leerHastaRetorno();
    Serial.println( s );
    
    // Recibir respuesta
    r = leerLinea(); // recibe info hasta '\n'
    
    // Envía lo recibido, terminando en "\r\n", añadido por el println
    Serial.println( r ); // devolver respuesta 
  }  
}

