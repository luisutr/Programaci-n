#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

byte encendido[8] = {
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000
};

byte apagado[8] = {
0b11111,
0b11111,
0b11111,
0b11111,
0b11111,
0b11111,
0b11111,
0b11111
};

//1 apagado y 0 encendidos//

void setup() {
  Serial.begin(115200);
  lcd.init();
  lcd.backlight();
  lcd.createChar(0, encendido);
  lcd.createChar(1, apagado);
  lcd.setCursor(0,0);
  lcd.print("Emmanuel");// Autor
  lcd.setCursor(0,1);
  lcd.print("Examen Abril");// Ejercicio
  delay(3000);
  lcd.clear();
  for (int i=0;i<16;i++) {
      lcd.setCursor(i,0);
      lcd.write(byte(1));
      lcd.setCursor(i,1);
      lcd.write(byte(1));
      }
}

void loop() {
  String sec, opc;
  int inic, fin;
  sec = leerTrama('\n');
  opc = cortaTrozo(sec, inic, &fin, ':', true);
  inic = fin;
  if (opc == "1") {
    for (int i=0;i<16;i++) {
      lcd.setCursor(i,0);
      lcd.write(byte(1));
      lcd.setCursor(i,1);
      lcd.write(byte(1));
      }
    String resultado = "No hay ninguna columna encendida";
    Serial.println(resultado);  
    } 
  if (opc == "2") {
    String col;
    int columna;
    col = cortaTrozo(sec, inic, &fin, ':', true);
    columna = col.toInt();
    String res = "1 Columna encendida. Columna: " + col;
    for (int i=0;i<16;i++) {
    lcd.setCursor(i,0);
    lcd.write(byte(1));
    lcd.setCursor(i,1);
    lcd.write(byte(1));
    } 
    lcd.setCursor(columna,0);
    lcd.write(byte(0));
    lcd.setCursor(columna,1);
    lcd.write(byte(0));
    Serial.println(res);
    }
  if (opc == "3") {
    for (int i=0;i<16;i++) {
    lcd.setCursor(i,0);
    lcd.write(byte(1));
    lcd.setCursor(i,1);
    lcd.write(byte(1));
    }
    String n, lista="";
    int N, *v_int, columna;
    n = cortaTrozo(sec, inic, &fin, ':', true);
    N = n.toInt();
    inic = fin;
    v_int = obtenListaEnteros(sec, inic, &fin, ':', true, N);
    for (int i=0;i<N;i++) {
       columna = v_int[i];
       lcd.setCursor(columna,0);
       lcd.write(byte(0));
       lcd.setCursor(columna,1);
       lcd.write(byte(0));
       if (i<N-1) {
          lista = lista + String(v_int[i]) + ',';
       }else{
          lista = lista + String(v_int[i]);
          }
       }
    Serial.println(lista);
    String conf;
    conf = leerTrama('\n');
    delay(5000);
    lcd.setCursor(7,0);
    lcd.print(conf);  
    }
  if (opc == "4") {
    for (int i=0;i<16;i++) {
      lcd.setCursor(i,0);
      lcd.write(byte(1));
      lcd.setCursor(i,1);
      lcd.write(byte(1));
      }
    String n, lista;
    int N, ran;
    n = cortaTrozo(sec, inic, &fin, ':', true);
    lista = n + " columnas mostradas. Columnas: ";
    N = n.toInt();
    for (int i=0;i<N;i++){
      ran = random(0,15);
      lcd.setCursor(ran,0);
      lcd.write(byte(0));
      lcd.setCursor(ran,1);
      lcd.write(byte(0));
      if (i<N-1) {
          lista = lista + String(ran) + ',';
          }else{
          lista = lista + String(ran);
          } 
      }
    Serial.println(lista);
    String conf;
    conf = leerTrama('\n');
    delay(5000);
    lcd.setCursor(7,0);
    lcd.print(conf);  
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
