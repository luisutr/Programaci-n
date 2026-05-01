#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

byte borrado[8] = {
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000
};

void setup() {
  Serial.begin(115200);
  lcd.init();
  lcd.createChar(2, borrado);
  lcd.backlight();
  lcd.setCursor(0,0);
  lcd.print("Examen");
  delay(3000);
  lcd.clear();
}


void loop() {
  String envio;
  envio = leerTrama('\n');
  String opcion;
  int inic, fin, *columna_origen, *fila_origen, *fila_destino, *columna_destino  ;
  opcion = cortaTrozo(envio, inic, &fin, '-', true);
  inic = fin;
  fila_origen = obtenListaEnteros(envio, inic, &fin, ',', true, 1);
  inic = fin;
  columna_origen = obtenListaEnteros(envio, inic, &fin, '-', true, 1);
  inic = fin;
  fila_destino = obtenListaEnteros(envio, inic, &fin, ',', true, 1);
  inic = fin;
  columna_destino = obtenListaEnteros(envio, inic, &fin, ' ', true, 1);
  if (opcion == "DL") {
    for (int k=fila_origen[0];k<=fila_destino[0];k++) {
      for(int j=columna_origen[0];j<=columna_destino[0];j++) {
            lcd.setCursor(j,k);
            lcd.print("X");
            }
      }
    String ACK = "ACK";
    Serial.println(ACK);  
    }
 if (opcion == "BL") {
  for (int k=fila_origen[0];k<=fila_destino[0];k++) {
      for(int j=columna_origen[0];j<=columna_destino[0];j++) {
            lcd.setCursor(j,k);
            lcd.write(byte(2));
            }
      }
    String ACK = "ACK";
    Serial.println(ACK);   
 }  
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

String leerTrama(char c){
        while(Serial.available() < 1){
        delay(1);
        }
 return Serial.readStringUntil(c);
}
