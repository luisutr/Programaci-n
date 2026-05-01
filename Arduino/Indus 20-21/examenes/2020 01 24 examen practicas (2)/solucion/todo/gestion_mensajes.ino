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

// Función que devuelve un vector de tam float a partir de la trama comenzando en la posición "inic"
int *obtenListaEntero(String linea, int inic, int *fin, char car, bool corta_si_no_esta, int tam) {
  int *v_int;
  int i;
  String s;
  v_int = (int *) malloc(sizeof(int)*tam);
  for(i=0;i<tam;i++) { // Para cada trozo
    s = cortaTrozo(linea, inic, fin, car, corta_si_no_esta); // s recibe el entero v_i como String 
    inic=*fin; // Apuntamos al principio del siguiente campo de la trama
    v_int[i] = s.toInt(); // s se convierte a float y se almacena en v_float
  }
  return v_int; // Devolución del vector
}

void generarMatrizIntDesdeMensaje(String mensaje, int matriz[FIL][COL]) {
  String fila;
  int i, j, pos_car, inic;

  for(i=0; i<FIL; i++) {
    inic = 0;
    pos_car = mensaje.indexOf(':'); // localiza primera fila
    // fila recibe la fila sin ':'
    fila = mensaje.substring(0,pos_car);    
    pos = 0; // inicio dentro de fila, la primera posición
    for(j=0; j<COL; j++) {
      // matriz[i][j] recibe el entero v_i como String 
      // Se lee de caracter en caracter separados por comas, 
      matriz[i][j] = cortaTrozo(mensaje, inic, &inic, ',', true).toInt();
    }
    // Se quita la primera parte del mensaje ya procesada
    mensaje = mensaje.substring(pos_car+1);
  }
}

