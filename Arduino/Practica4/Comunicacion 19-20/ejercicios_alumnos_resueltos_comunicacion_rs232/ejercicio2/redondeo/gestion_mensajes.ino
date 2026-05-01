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


float *generarVectorFloatDesdeMensaje(int *tam) {
  String mensaje, s;
  int inic, fin;
  mensaje = leerLinea();

  // Lee tam
  inic = 0;
  s = cortaTrozo(mensaje, inic, &inic, ':', true); // s recibe el entero v_i como String
  *tam = s.toInt(); // convierte a entero
  // Devuelve un vector de tamaño tam leído de mensaje utilizando car 
  // como separador entre elementos
  return obtenListaFloat(mensaje, inic, &fin, ',', true, *tam);
}

// Envia el vector entero con formato: tam:f0,f1,...ftam-1
void enviarVectorEntero(int v[], int tam) {
  int i;
  String s="";
  s = String(tam) + ":";
  for(i=0; i<tam; i++) {
    if (i!=tam-1) s += String(v[i]) + ","; // si no es el último
    else s += String(v[i]); // el último envía sin ", "
  }
  Serial.println( s );
}

// Envia el vector float con formato: tam:f0,f1,...ftam-1
void enviarVectorFloat(float v[], int tam) {
  int i;
  String s="";
  s = String(tam) + ":";
  for(i=0; i<tam; i++) {
    if (i!=tam-1) s += String(v[i]) + ","; // si no es el último
    else s += String(v[i]); // el último envía sin ", "
  }
  Serial.println( s );
}
