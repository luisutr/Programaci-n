void corta_fila_columna(int M[4][3], int n_fil, int fil[FIL], int n_col, int col[COL]) {
  int i;
  for(i=0; i<COL; i++) {
    fil[i] = M[n_fil][i];
  }
  for(i=0; i<FIL; i++) {
    col[i] = M[i][n_col];
  }
}

String aHexadecimal(int v) {
  char c[] = "0123456789ABCDEF";
  return String( c[v] );
}

void mostrarVectorIntLCD(int v[], int tam, int fila) {
  int i;
  String s="";
  lcd.setCursor(0,fila); // posiciona cursor
  for(i=0; i<tam; i++) s += aHexadecimal(v[i]) + String(" "); // Completa s con el vector
  lcd.print(s); // muestra el String s
}

String vectorIntAString(int v[], int tam) {
  int i;
  String s="";
  s = "{";
  for(i=0; i<tam; i++) {
    if (i!=tam-1) s += aHexadecimal(v[i]) + ","; // si no es el último
    else s += aHexadecimal(v[i]) + String("}"); // el último envía con "}"
  }
  return s;
}

void solucion_ejercicio1(String opc, String mensaje) {
  int inic, n_fil, n_col, m[FIL][COL] = { {11,2,13}, {0,15,6}, {3,5,14}, {4,7,10} }, f[COL], c[FIL];

  // Lee n_fil
  inic = 0;
  n_fil = cortaTrozo(mensaje, inic, &inic, ':', true).toInt();
  
  // Lee n_col
  n_col = cortaTrozo(mensaje, inic, &inic, ':', true).toInt();
  mensaje = mensaje.substring(inic); // quita n_col y el ':' de mensaje
  
  generarMatrizIntDesdeMensaje(mensaje, m);
  corta_fila_columna(m, n_fil, f, n_col, c);
  lcd.clear(); // Limpia LCD
  mostrarVectorIntLCD(f, COL, 0); // Muestra la fila en el vector en el LCD
  mostrarVectorIntLCD(c, FIL, 1); // Muestra la columna en el vector en el LCD
  Serial.println("1:" + vectorIntAString(f,COL) + ":" + vectorIntAString(c,FIL));
}
