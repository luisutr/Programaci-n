#define FIL 3
#define COL 4

void setup() {
  Serial.begin(115200);
}

void loop() {
  String mensaje, s;
  char matriz[FIL][COL], elem;
  int inic, x, y; // Se accede con los índices del 0 al TAM-1

  // Lee el mensaje enviado desde el PC
  mensaje = leerLinea();

  // Obtiene la columna a procesar
  inic = 0;
  s = cortaTrozo(mensaje, inic, &inic, ':', true); // s recibe la columna como String
  elem = s[0]; // convierte a char
  mensaje = mensaje.substring(inic); // quita la columna y el ':' de mensaje

  // Función que genera la matriz de caracteres de 3*4
  // desde el mensaje recibido
  // El parametro matriz recoge la matriz y el parametro
  // mensaje le pasa el mensaje
  generarMatrizCharDesdeMensaje(mensaje, matriz);
  
  // Busca elemento en la matriz
  coordenadas(matriz, elem, &x, &y);
  // mostrar vector
  Serial.println( String(x) + "," + String(y) );
}

// Función que devuelve una columna de una matriz
// mediante los parámetros por referencia *x e *y
void coordenadas(char M[FIL][COL], char elem, int *x, int *y) {
  int i, j;
  bool ya_lo_tengo = false;
  for(i=0; i<FIL; i++) {
    for(j=0; j<COL; j++) {
      if (elem==M[i][j]) {
        *x = i;
        *y = j;
        ya_lo_tengo = true;
      }
      if (ya_lo_tengo) break;
    }
  }
}

