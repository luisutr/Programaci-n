/*
 * Devuelve por referencia los componentes de la cadena de entrada COD,OP1,OP2:RESULT  
 * en los punteros a String (paso por referencia) cod, op1, op2 y result. Necesita la 
 * función cortaTrozo
 */
void  decodifica(String mensa, String *cod, String *op1, String *op2, String *result) {
    int inic = 0;
    // Copia hasta la primera coma (COD) desde el principio
    *cod = cortaTrozo(mensa, inic, &inic, ',', true); 
    // Copia hasta la segunda coma (OP1) desde donde se encontraba la primera coma (inic)
    *op1 = cortaTrozo(mensa, inic, &inic, ',', true); 
    // Copia hasta el primer ':' (OP2) desde donde se encontraba la segunda coma (inic)
    *op2 = cortaTrozo(mensa, inic, &inic, ':', true);
    // Copia hasta el segundo : (RESULT) desde donde se encontraba el primer ':' (inic)
    *result = cortaTrozo(mensa, inic, &inic, ':', true);  
}

/* 
 * Devuelve como String el contenido entre dos "car" (carácter)
 * comenzando en "inic" y hasta que se encuentra un "car", fin tendrá el
 * índice donde comienza el siguiente campo. El parámetro corta_si_no_esta
 * permite seleccionar si se devuelve el trozo o no si no se encuentra el 
 * carácter car
 */ 
String cortaTrozo(String s, int inic, int *fin, char car, bool corta_si_no_esta) {
  int pos_car;
  pos_car = s.indexOf(car,inic); // Devuelve a pos_car la posicion de car empezando en inic
  *fin = pos_car + 1; // El fin se asigna a donde comienza el siguiente campo
  if (pos_car!=-1) return s.substring(inic,pos_car); // Corta entre inic y fin
  else if (corta_si_no_esta) return s.substring(inic); // Corta desde inic al final
  else return String("-1"); // Error, devuelve el String "-1"
}
