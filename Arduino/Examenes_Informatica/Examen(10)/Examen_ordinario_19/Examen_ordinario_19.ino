#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

byte apagado[8] = {
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
  lcd.backlight();
  lcd.createChar(0, apagado);
  lcd.setCursor(0,0);
  lcd.print("Emmanuel");// Autor
  lcd.setCursor(0,1);
  lcd.print("Examen Ordinario");// Ejercicio
  delay(3000);
  lcd.clear();
}
void loop() {
  String sec, opc, fila_o, columna_o, fila_d, columna_d;
  int inic, fin, f_o, c_o, f_d, c_d;
  sec = leerTrama('\n');
  opc = cortaTrozo(sec, inic, &fin, '-', true);
  inic = fin;
  fila_o = cortaTrozo(sec, inic, &fin, ',', true);
  inic = fin;
  columna_o = cortaTrozo(sec, inic, &fin, '-', true);
  inic = fin;
  fila_d = cortaTrozo(sec, inic, &fin, ',', true);
  inic = fin;
  columna_d = cortaTrozo(sec, inic, &fin, ' ',true);

  f_o = fila_o.toInt();
  c_o = columna_o.toInt();
  f_d = fila_d.toInt();
  c_d = columna_d.toInt();
  
  if (opc == "DL") {
    for (int i=f_o;i<=f_d;i++) {
      for(int j=c_o;j<=c_d;j++) {
        lcd.setCursor(j,i);
        lcd.print("X");
      }
    }
  String conf = "ACK";
  Serial.println(conf);  
  }
 if (opc == "BL") {
  for (int i=f_o;i<=f_d;i++) {
      for(int j=c_o;j<=c_d;j++) {
        lcd.setCursor(j,i);
        lcd.write(byte(0));
      }
    }
 String conf = "ACK";
 Serial.println(conf);   
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
  
