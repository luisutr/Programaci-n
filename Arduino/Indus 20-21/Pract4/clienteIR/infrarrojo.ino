// Lee pulsaciones del mando hasta que se pulsa "ST/REPT"
String leerHastaRetorno() {
  bool b = false;
  String r="", s;
  while(b == false) {
    if (irrecv.decode(&results)) { // Si se ha recibido alguna señal, mediante una pulsacion, entramos en el if y provoca una lectura almacenando el resultado en results (con un paso por referencia para que la variable se actualice).
      // Lee el código pulsado y envía a programa python
      s = getValor(results.value); // Se lee el valor con la funcion getValor y se almacena en s
      if(s!="ST/REPT") { // carácter que marca fin de cadena
        if(s=="ON/OFF") { // ON/OFF se utiliza para indicar la coma
          r = r + String(",");
        } else if(s=="EQ") { // MODE se utiliza para indicar EL :
          r = r + String(":");
        } else if(s=="PREV") { // PREV se utiliza para indicar el producto
          r = r + String("*");
        } else if(s=="NEXT") { // NEXT se utiliza para indicar la división entera
          r = r + String("%");
        } else if(s=="UP") { // UP se utiliza para indicar la suma
          r = r + String("+");
        } else if(s=="DOWN") { // DOWN se utiliza para indicar la resta
          r = r + String("-");
        } else if(s!="") { // Cualquier pulsación no vacía se introduce
          r = r + s; 
        }
        if (r!="") { // Actualiza el LCD si r no es vacío
          lcd.clear();
          lcd.setCursor(0,1);
          lcd.print(r);
        }
      } else { // Si es el carácter fin de cadena b a true para salir del while
        b = true; // completada cadena 
      }
      
      irrecv.resume(); //Orden para recibir el siguiente valor. Necesario para una nueva lectura
    }
    // Necesario para evitar el problema del "Soft WDT reset"
    // caused by watchdog timer.
    delay(1); // 
  }
  return String(r);
}

void muestraTodoLCD(String result_recibido, String op1, String cod, String op2, String result) {
  lcd.clear(); lcd.setCursor(0,0); // Borra LCD y coloca en posición (0,0)
  lcd.print(op1+cod+op2+"="+result); // Muestra la cadena a evaluar en el formato solicitado
  if (result_recibido==result) { // TRUE si le recibido es igual a result de la cadena de entrada
    lcd.setCursor(0,1); 
    lcd.print("TRUE"); // Muestra TRUE en fila 1
  } else {
    lcd.setCursor(0,1);
    lcd.print("FALSE"); // Muestra FALSE en fila 1
  }  
}

String getValor(unsigned long c) { // Esta funcion recibe un unsigned long c (que es uno de los codigos del mando, del vector claves) y busca el valor que le corresponda.
  byte i;
  i=0;
  while( (i<21) && (claves[i]!=c) ) { // Con este bucle se recorre el vector claves hasta encontrar la posición pedida.
    i++;
  }
  if (i==21) return String(""); // En caso de que sea el valor 21 significa que hemos recorrido el vector entero sin encontrarlo y devuelve una cadena en blanco.
  else return String(valor[i]);// Cuando ha encontrado la posición accede al vector valor y devuelve el resultado. 
}
