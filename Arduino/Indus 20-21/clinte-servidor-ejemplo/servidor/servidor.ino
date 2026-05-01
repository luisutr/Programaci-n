void setup() {
  Serial.begin(115200); 
}

void loop() {
  String s, trama; // trama tendrá la trama recibida
  int inic, opc, i, N, sol;
  int *v_int; // puntero que contendrá el vector de enteros recibido
  float *v_float, f; // puntero que contendrá el vector de enteros recibido

  // LEE LA TRAMA POR EL PUERTO COM
  //trama = leerTrama('\n'); // lee la trama

  // LEE POR TECLADO 
  //trama = leerLinea(); 
  // OJO tengo que meter los datos con la sintaxis: opc:N:V1:V2:Vn
  
  s = cortaTrozo(trama, 0, &inic, ':', true); // s recibe la opcion como String
  //inic=fin; // Apuntamos al principio del siguiente campo de la trama
  opc = s.toInt(); // La opción (s) se convierte a entero

  // OBTENER N
  s = cortaTrozo(trama, inic, &inic, ':', true); // s recibe N como String 
  //inic=fin; // Apuntamos al principio del siguiente campo de la trama
  N = s.toInt(); // N (s) se convierte a entero
  
  // ESTUDIO DE PETICIONES
  if (opc==1) { // PETICIÓN 1
    // v_int contiene el vector de N enteros
    v_int = obtenListaEnteros(trama, inic, &inic, ':', true, N); 
    sol = sumaListaEnteros(v_int, N); // devuelve la suma de los N enteros
    Serial.println( String(sol) ); // Envía al programa Python el resultado
    free(v_int); // IMPORTANTE: Libera la memoria de v_int
  } 
  else if (opc==2) { // PETICIÓN 2
    //2:3:1.5:1.6:1.7:2.9
    // opcion dos, le damos el numero de float, luego el vector de float 
    // y al final un float a sumar o incrementar a cada float del vector. 
    // Ese vector incrementado es lo que tiene que devolver 
    
    // v_float contiene el vector de N float
    v_float = obtenListaFloat(trama, inic, &inic, ':', true, N);
    //inic = fin; // Apuntamos al principio del siguiente campo de la trama
    s = cortaTrozo(trama, inic, &inic, ':', true); // s recibe el float a sumar como String 
    //inic=fin; // Apuntamos al principio del siguiente campo de la trama
    f = s.toFloat(); // s se convierte a float y se almacena en f
    incrementaListaEn(v_float, N, f); // incrementa cada valor de v_float en f
    s = String(""); // s contendrá la trama a enviar al programa Python
    for(i=0;i<N;i++) { // MONTA LA TRAMA DE SALIDA
      s += String(v_float[i]);
      if (i!=N-1) s += String(':');
    }
    Serial.println(  s  ); // Se envía la trama con los resultados al programa Python
    free(v_float); // IMPORTANTE: Libera la memoria de v_float
  }
}

// Función que lee una trama terminada en car
String leerLinea() {
  // Espera hasta que haya algo que leer
  while(Serial.available() < 1) {
    delay(1);
  }
  return Serial.readStringUntil('\n'); // Recibe info hasta '\n'
}

/////////////////////// FUNCIONES TRAMA COMUNICACION //////////////////////////

// Función que lee una trama terminada en car
String leerTrama(char c) {
        // Espera hasta que haya algo que leer
        while(Serial.available() < 1) {
              delay(1);
        }
        return Serial.readStringUntil(c); // Recibe info hasta '\n'
}
