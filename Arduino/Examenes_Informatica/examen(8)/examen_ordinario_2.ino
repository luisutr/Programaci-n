#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

byte b[8] = {
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
  lcd.createChar(5, b);
  lcd.setCursor(0,0);
  lcd.print("EXAMEN_ORD");
  delay(4000);
  lcd.clear();
}


void loop() {
  String mensaje, opc, n;
  int inic, fin;
  mensaje = leerTrama('\n');
  opc = cortaTrozo(mensaje, inic, &fin, '|', true);
  inic = fin;
  n = cortaTrozo(mensaje, inic, &fin, '|', true);
  inic = fin;
  int N;
  N = n.toInt();
  if (opc == "E") {
    int sum = 0;
    while (sum<=N) {
      sum = sum + 1;
      String fila, columna;
      int columna_i, fila_i;
      fila = cortaTrozo(mensaje, inic, &fin, ',', true);
      inic = fin;
      columna = cortaTrozo(mensaje, inic, &fin, '|', true);
      fila_i =fila.toInt();
      inic = fin;
      columna_i = columna.toInt();
      lcd.setCursor(columna_i,fila_i);
      lcd.print("*");
    }
   String ok = "OK";
   Serial.println(ok); 
  }
 if (opc == "B") {
    int sum = 0;
    while (sum<=N) {
      sum = sum + 1;
      String fila, columna;
      int columna_i, fila_i;
      fila = cortaTrozo(mensaje, inic, &fin, ',', true);
      inic = fin;
      columna = cortaTrozo(mensaje, inic, &fin, '|', true);
      inic = fin;
      fila_i =fila.toInt();
      columna_i = columna.toInt();
      lcd.setCursor(columna_i,fila_i);
      lcd.write(byte(5));
    }
   String ok = "OK";
   Serial.println(ok);  
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
