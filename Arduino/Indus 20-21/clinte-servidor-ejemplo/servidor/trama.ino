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

// Función que devuelve un vector de tam enteros a partir de la trama comenzando en la posición "inic"
int *obtenListaEnteros(String linea, int inic, int *fin, char car, bool corta_si_no_esta, int tam) {
  int *v_int, i;
  String s;
  v_int = (int *) malloc(sizeof(int)*tam); // Reserva de memoria
  for(i=0;i<tam;i++) { // Para cada trozo
      s = cortaTrozo(linea, inic, fin, car, corta_si_no_esta); // s recibe el entero v_i como String 
      inic=*fin; // Apuntamos al principio del siguiente campo de la trama
      v_int[i] = s.toInt(); // s se convierte a entero y se almacena en v_int[i]
  }
  return v_int; // Devolución del vector
}
// Función que devuelve un vector de tam float a partir de la trama comenzando en la posición "inic"
float *obtenListaFloat(String linea, int inic, int *fin, char car, bool corta_si_no_esta, int tam) {
  float *v_float;
  int i;
  String s;
  v_float = (float *) malloc(sizeof(float)*tam);
  for(i=0;i<tam;i++) { // Para cada trozo
    s = cortaTrozo(linea, inic, fin, car, corta_si_no_esta); // s recibe el entero v_i como String 
    inic=*fin; // Apuntamos al principio del siguiente campo de la trama
    v_float[i] = s.toFloat(); // s se convierte a float y se almacena en v_float
  }
  return v_float; // Devolución del vector
}

