
// El orden en los índices es el natural, A->0, B->1, .... G->7
int pines[7] = {12, 14, 2, 5, 4, 13, 15}; 
int codigos[11][7] = {
  {1,1,1,1,1,1,0},  // escribe 0
  {0,1,1,0,0,0,0},  // escribe 1
  {1,1,0,1,1,0,1},  // escribe 2
  {1,1,1,1,0,0,1},  // escribe 3
  {0,1,1,0,0,1,1},  // escribe 4
  {1,0,1,1,0,1,1},  // escribe 5
  {1,0,1,1,1,1,1},  // escribe 6
  {1,1,1,0,0,0,0},  // escribe 7
  {1,1,1,1,1,1,1},  // escribe 8
  {1,1,1,0,0,1,1},  // escribe 9
  {0,0,0,0,0,0,0} // borra el display
};

void setup() {
  int i;
  for(i=0; i<7; i++) {
    pinMode(pines[i], OUTPUT);
  }
  Serial.begin(115200); 
}

int leerEntero(String s) {
  String r;
  Serial.println(s);
  r = leerLinea();
  if (esEntero(r)) {
    return r.toInt(); 
  }
  return -32768; // Un código que no usara el loop
}

bool esEntero(String s) {
  int i, p=0;
  if ((s[0]=='+') or (s[0]=='-')) {
    p = 1;
  }
  for(i=p; i<s.length(); i++) {
    if (not isDigit(s[i])  ) {
      Serial.println( "Valor no entero: " + s );
      return false;
    }
  }
  return true;
}

String leerLinea() {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil('\n'); // Recibe info hasta '\n'
}

void display(int v[7]) {
  int i;
  for(i=0; i<7; i++) {
    digitalWrite(pines[i],v[i]);
  }
}
 
// Dependiendo de cada dígito, se envía a la función display
// los estados (0 y 1) a cada uno de los segmentos
void loop() {
  int n;
  n = leerEntero("Dame un valor para el display entre 0 y 9, -1 para borrar");
  Serial.println( String(n) );
  if( (n>=0) && (n<=9) ) {
    display(codigos[n]);
  }
  if (n==-1) {
    display(codigos[10]);
  }
}
