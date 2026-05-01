#define LED 5 // pin D1 del nodeMCU
#include <IRremoteESP8266.h>
#include <IRrecv.h>

unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,0xFF52AD};
String valor[21] = {"ON/OFF", "MODE", "VolOFF", "PLAY/PAUSE", "PREV", "NEXT",
"EQ", "-", "+", "0", "LOOP", "U/SD", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
int RECV_PIN = 2; // pin 1 del receptor IR al pin 2 de Arduino
IRrecv irrecv(RECV_PIN); // Crea objeto de ’irrecv’
decode_results results; // Crea objeto de ’decode_results’
void setup() {
pinMode(LED, OUTPUT); // LED como salida
Serial.begin(115200);
irrecv.enableIRIn(); // Inicializa el receptor
}
void loop() {
String s, r = "";
if (irrecv.decode(&results)) { // Si alguna señal recibida
// enciende el LED
digitalWrite(LED, HIGH);
// Lee el código pulsado y envía a programa python
s = leerHastaRetorno();
Serial.println( s );
// Recibir respuesta
r = leerLinea(); // recibe info hasta ’\n’
// Envía lo recibido terminado en "\n"
Serial.println( r ); // devolver respuesta
// apaga el LED
digitalWrite(LED, LOW);
}
}
// Lee pulsaciones del mando hasta que se pulsa "U/SD"
String leerHastaRetorno() {
bool b = false;
String r="", s;
while(!b) {
if (irrecv.decode(&results)) { // Si alguna señal
// Lee el código pulsado y envía a programa python
s = getValor(results.value);
if(s!="U/SD") {
// Enviar identificador pulsado a python
if(s=="LOOP") r = r + String(":");
else r = r + s;
} else {
b = true; // completada cadena
}
irrecv.resume(); // Recibir el siguiente valor
}
// Necesario para evitar el problema del "Soft WDT reset"
// caused by watchdog timer.
delay(1); //
}
return String(r);
}
String leerLinea() {
// Espera hasta que haya algo que leer
// BUCLE TOTALMENTE NECESARIO
while(Serial.available() < 1) {
delay(1);
}
return Serial.readStringUntil('\n'); // Recibe info hasta ’\n’
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
