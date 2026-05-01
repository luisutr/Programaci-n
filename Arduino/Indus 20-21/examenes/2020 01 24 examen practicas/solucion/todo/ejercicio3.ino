char *a_vector_hexadecimal(int M[4][3]) {
  int i, j, k;
  char *vect;
  vect = (char *) malloc( sizeof(char)*FIL*COL+1 );
  k = 0;
  for(i=0; i<FIL; i++) {
    for(j=0; j<COL; j++) {
      vect[k] = aHexadecimal(M[i][j])[0];
      k++; 
    }
  }
  return vect;
}

String aStringVectorChar(char v[], int tam) {
  int i;
  String s="";
  for(i=0; i<tam; i++) s+=v[i]; // Completa s con el vector
  return s;
}

void solucion_ejercicio3(String opc, String mensaje) {
  int inic, n_fil, m[FIL][COL], maxi;
  char *v;
  
  generarMatrizIntDesdeMensaje(mensaje, m);
  v = a_vector_hexadecimal(m);
  lcd.clear(); // Limpia LCD
  lcd.setCursor(0,0); lcd.print(aStringVectorChar(v,12)); // Muestra el char v en la primera fila del LCD
  Serial.println(aStringVectorChar(v,12));
  free(v);
}
