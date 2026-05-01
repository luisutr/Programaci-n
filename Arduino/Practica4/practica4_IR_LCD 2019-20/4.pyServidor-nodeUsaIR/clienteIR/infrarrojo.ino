// Lee pulsaciones del mando hasta que se pulsa "U/SD"
String leerHastaRetorno() {
  bool b = false;
  String r="", s;
  while(!b) {
    if (irrecv.decode(&results)) { // Si se ha recibido alguna señal
      // Lee el código pulsado y envía a programa python
      s = getValor(results.value); 
      if(s!="U/SD") {
        // Enviar identificador pulsado a python
        if(s=="LOOP") r = r + String(":");
        else r = r + s;
      } else {
        b = true; // completada cadena 
      }
      irrecv.resume(); // Recibir el siguiente valor
    }
    // Necesario para evitar el problema del "Soft WDT reset"
    // caused by watchdog timer.
    delay(1); // 
  }
  return String(r);
}

String getValor(unsigned long c) {
  byte i;
  i=0;
  while( (i<21) && (claves[i]!=c) ) {
    i++;
  }
  if (i==21) return String("");
  else return String(valor[i]);
}

