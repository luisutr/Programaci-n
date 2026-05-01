// Funcion que devuelve como String el contenido entre dos "car" (carácter)
// comenzando en "inic" y hasta que se encuentra un "car", fin tendrá el 
// índice donde comienza el siguiente campo 
String cortaTrozo(String s, int inic, int *fin, char car, bool corta_si_no_esta) {
  int pos_car;
  pos_car = s.indexOf(car,inic); // posicion de car empezando en inic
  *fin = pos_car + 1; // fin se asigna a donde comienza el siguiente campo
  if (pos_car!=-1) return s.substring(inic,pos_car); // Corta entre inic y fin
  else if (corta_si_no_esta) return s.substring(inic); // Corta desde inic al final
  else return String("-1"); // Error, devuelve el String "-1"
}

void generarMatrizCharDesdeMensaje(String mensaje, char matriz[FIL][COL]) {
  String fila;
  int i, j, pos_car, pos;

  for(i=0; i<FIL; i++) {
    pos_car = mensaje.indexOf('}'); // localiza primera ','
    // fila recibe la fila sin '{', '}' y ','
    fila = mensaje.substring(1,pos_car);
    // inicio dentro de fila, la primera posición
    pos = 0; 
    for(j=0; j<COL; j++) {
      // matriz[i][j] recibe el entero v_i como String 
      matriz[i][j] = fila[pos];
      // Se lee de caracter en caracter separados por comas, 
      // es decir, uno sí y uno no (el salto de dos en dos)
      pos += 2; 
    }
    // Se quita la primera parte del mensaje ya procesada
    mensaje = mensaje.substring(pos_car+2);
  }
}


