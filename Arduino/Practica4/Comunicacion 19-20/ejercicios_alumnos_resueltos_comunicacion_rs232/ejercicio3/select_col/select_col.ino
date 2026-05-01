#define FIL 3
#define COL 4

void setup() {
  Serial.begin(115200);
}

void loop() {
  String mensaje, s;
  char matriz[FIL][COL], *v;
  int inic, col, i; // Se accede con los índices del 0 al TAM-1

  // Lee el mensaje enviado desde el PC
  mensaje = leerLinea();

  // Obtiene la columna a procesar en col
  // Tambien actualiza el mensaje quitándole "col:"
  inic = 0;
  s = cortaTrozo(mensaje, inic, &inic, ':', true); // s recibe la columna como String
  col = s.toInt(); // convierte a entero
  mensaje = mensaje.substring(inic); // quita la columna y el ':' de mensaje

  // Genera la matriz de caracteres de 3*4 desde el mensaje recibido.
  // El parametro mensaje le pasa el mensaje a procesar y 
  // el parámetro matriz recoge la matriz leída y el parametro.
  generarMatrizCharDesdeMensaje(mensaje, matriz);
  
  // Obtiene los elementos de la columna en el puntero r
  v = columna(matriz, col);

  // Genera y envia el vector resultado por el RS-232
  Serial.println( generaVectorChar(v, FIL) );
  
  // Libera la memoria columna
  free(v);
}

// Funcion que devuelve una columna de una matriz
char* columna(char M[FIL][COL], int col) {
  int i;
  char *v;
  v = reservarVectorChar(FIL); 
  for(i=0; i<FIL; i++) {
    v[i] = M[i][col];
  }
  return v;
}

