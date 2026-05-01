String maximoFila(int M[4][3], int n_fil, int *maxi) {
  int i;
  *maxi = M[n_fil][0];
  for(i=0; i<COL; i++)
    if (*maxi<M[n_fil][i]) *maxi = M[n_fil][i];
  return aHexadecimal(*maxi);
}

void solucion_ejercicio2(String opc, String mensaje) {
  int inic, n_fil, m[FIL][COL], maxi;
  String v;

  // Lee n_fil
  inic = 0;
  n_fil = cortaTrozo(mensaje, inic, &inic, ':', true).toInt();
  mensaje = mensaje.substring(inic); // quita n_fil y el ':' de mensaje
  
  generarMatrizIntDesdeMensaje(mensaje, m);
  v = maximoFila(m, n_fil, &maxi);
  lcd.clear(); // Limpia LCD
  lcd.setCursor(0,0); lcd.print(String(v)); // Muestra el char v en la primera fila del LCD
  lcd.setCursor(0,1); lcd.print(String(maxi)); // Muestra el maximo como entero en la segunda fila del LCD
  Serial.println("2:" + v + ":" + String(maxi));
}
