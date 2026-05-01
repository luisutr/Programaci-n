#include <IRremoteESP8266.h>
#include <IRrecv.h>

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,
0xFF52AD};

String valor[21] = {"a", "e", "i", "o", "u", "PLAY/PAUSE",
"-", "+", ".", "0", "//", ":", "1", "2", "3", "4", "5", "6", "7", "8",
"9"};

int RECV_PIN = 2; // pin del receptor IR al pin D4 del nodeMCU

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv'
decode_results results; // Crea objeto de 'decode_results'

void setup() {
        Serial.begin(115200);
        irrecv.enableIRIn(); // Inicializa el receptor
        lcd.init();
        lcd.backlight();
        lcd.setCursor(0,0); // 
        lcd.print("Emmanuel");// Autor
        lcd.setCursor(0,1);
        lcd.print("Examen_Abril");
        delay(4000);
        lcd.clear(); 
}

void loop() {
        lcd.setCursor(0,0);
        lcd.print("1-Incre 2-Decre");
        lcd.setCursor(0,1);
        lcd.print("3-Lista 4-List.D");
        delay(4000);
        lcd.clear();
        String sec, opc;
        int inic, fin;
        sec = leerHastaRetorno();
        Serial.println(sec);
        opc = cortaTrozo(sec, inic, &fin, ':', true);
        if (opc == "1") {
          String resultado;
          resultado = leerTrama('\n');
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Incremento:");
          lcd.setCursor(0,1);
          lcd.print(resultado);
          delay(10000);
          lcd.clear(); 
          }
        if (opc == "2") {
          String resultado;
          resultado = leerTrama('\n');
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Decremento:");
          lcd.setCursor(0,1);
          lcd.print(resultado);
          delay(10000);
          lcd.clear(); 
          }
        if (opc == "3") {
          String resultado;
          resultado = leerTrama('\n');
          String conf = "ACK";
          Serial.println(conf);
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("Lista:");
          lcd.setCursor(0,1);
          lcd.print(resultado);
          delay(10000);
          lcd.clear();
          }
        if (opc == "4") {
          int inic, fin, N;
          float *v_float, *v_float2;
          String lista_d, lista_c, n;
          n = leerTrama('\n');
          N = n.toInt();
          lista_d = leerTrama('\n');
          lista_c = leerTrama('\n');
          v_float = obtenListaFloat(lista_d, inic, &fin, ':', true, N);
          v_float2 = obtenListaFloat(lista_c, inic, &fin, ':', true, 2*N);
          int sum = 0;
          for (int i=0;i<N;i++) {
            for (int j=N;j<2*N;j++){
              if(v_float[i] == v_float2[j]) {
                sum += 1;
                lcd.clear();  //Para ver la comparacion numero a numero de las listas en el lcd//
                lcd.setCursor(0,0);
                lcd.print(String(v_float[i]));
                lcd.setCursor(0,1);
                lcd.print(String(v_float2[j]));
                delay(2000);
                lcd.clear();
                }
              }
            }
          if (sum == N) {
            String conf = "OK";
            Serial.println(conf);  
          }
          if (sum != N) {
            String conf = "KO";
            Serial.println(conf);
          }
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


String cortaTrozo(String s, int inic, int *fin, char car, bool corta) {
    int pos_car;
    pos_car = s.indexOf(car,inic); // posicion de car empezando en inic
    *fin = pos_car + 1; // fin se asigna a donde comienza el siguiente campo
    if (pos_car!=-1) return s.substring(inic,pos_car); // Entre inic y fin
    else if (corta) return s.substring(inic); // Desde inic al final
    else return String("-1"); // Error, devuelve el String "-1"
}


int *obtenListaEnteros(String linea, int inic, int *fin, char car, bool c, int N) {
    int *v_int, i;
    String s;
    v_int = (int *) malloc(sizeof(int)*N); // Reserva de memoria
    for(i=0;i<N;i++) { // Para cada trozo
        s = cortaTrozo(linea, inic, fin, car, c); // s = v_i como String
        inic=*fin; // Apuntamos al principio del siguiente campo
        v_int[i] = s.toInt(); // s se convierte a entero y se almacena
    }
    return v_int; // Devolución del vector
    }


float *obtenListaFloat(String linea, int inic, int *fin, char car, bool c, int N) {
    float *v_float;
    int i;
    String s;
    v_float = (float *) malloc(sizeof(float)*N);
    for(i=0;i<N;i++) { // Para cada trozo
          s = cortaTrozo(linea, inic, fin, car, c); // s = v_i como String
          inic=*fin; // Apuntamos al principio del siguiente campo
          v_float[i] = s.toFloat(); // s se convierte a float y se almacena
    }
    return v_float; // Devolución del vector
}


float incrementaListaEn(float v[], int tam, float M) {
      int i;
      for(i=0;i<tam;i++) {
      v[i] += M;
      }
 return M;
}


String leerTrama(char c){
        while(Serial.available() < 1){
        delay(1);
        }
 return Serial.readStringUntil(c);
}  


String leerHastaRetorno() {
      bool b = false;
      String r="", s;
      while(!b) {
            if (irrecv.decode(&results)) { // Si alguna señal
                  // Lee el código pulsado y envía a programa python
                  s = getValor(results.value);
                  lcd.print(s);
                  if(s!="//") {
                        // Enviar identificador pulsado a python
                        if(s==":") r = r + String(":");
                        else r = r + s;
            } else {
                    b = true; // completada cadena
            }
            irrecv.resume(); // Recibir el siguiente valor
            }
            //Necesario para evitar el problema del "Soft WDT reset"
            // caused by watchdog timer.
            delay(1); 
      }
      return String(r);
}


void escribeLCD(String s) {
  lcd.clear();
  if(s!="") {
    lcd.setCursor(0,0); // Coloca el cursor en la fila 0
    lcd.print(s);
  } else {
    lcd.setCursor(0,1); // Coloca cursor en fila 1
    lcd.print( "--- Rebote ---"); // Muestra mensaje rebote
  }
  delay(200); // Retardo para evitar rebote
}
