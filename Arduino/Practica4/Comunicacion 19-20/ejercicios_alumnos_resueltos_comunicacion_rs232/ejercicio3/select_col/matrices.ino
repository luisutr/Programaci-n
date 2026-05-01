// Genera String con matriz FIL*COL en formato
// {v00,v01,...,v0COL-1},{v10,v11,...,v1COL-1},{v20,v21,...,v2COL-1}, etc
String muestraMatrizChar(char m[FIL][COL]){
  int i, j;
  String s;

  s = "";
  for(i=0;i<FIL;i++) {
    for(j=0;j<COL;j++) {
      if(j==0) s += String("{") +String(m[i][j]);
      else s += String(", ") + String(m[i][j]);
    }
    if (i!=COL-1) s += String("},");
    else s += String("}");
  }
  return s;
}
