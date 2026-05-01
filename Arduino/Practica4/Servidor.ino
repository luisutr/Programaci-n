//Jesús Rodríguez Esteban

///////////////////////////////// FUNCIONAMIENTO PRÁCTICA IV /////////////////////////////////
//Subir el presente skecth
//En el LCD aparecerá mi nombre y el número de la práctica (Práctica IV)
//Correr el programa  cliente en pyCharm
//Se desplegará un menú en la parte del cliente (PyCharm)
//Introducir operación deseada (0,1,2,3,4 o 5)
//Seguir los pasos que se indican en los ejemplos dentro de cada operación
//Introducir valores como los que se indican en los ejemplos
//Cada vez que se ejecute una operación, se mostrará el resultado en el cliente y y en el LCD
//Una vez terminada, se podrá volver a alegir cualquiera de las opciones
/////////////////////////////////////////////////////////////////////////////////////////////// 

//Definimos bibliotecas necesarias
#define LED 5 // pin D1 del nodeMCU, muestra mientras atiende petición

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

String ultima_orden; //String donde almacenaremos el resultado de cada ejecución

void setup() {
        Serial.begin(115200);
        Wire.begin(5, 4);
        lcd.setBacklight(HIGH); //Use predefined PINS consts
        lcd.begin(16,2);
        lcd.home();
        //Mensaje Inicial
        lcd.setCursor(0,0); // Primer digito corresponde a la columna
                            // Segundo digito corresponde a la fila
        lcd.print("Jesus  Rodriguez"); // Autor
        lcd.setCursor(2,1);
        lcd.print("Practica IV"); //Número de la prática
        delay(5000); //Espereamos 5sg y desaparece el mensaje inicial
        lcd.clear();
}

void loop() {
        lcd.setCursor(3,0);
        lcd.print("Resultado:");
        lcd.setCursor(0,1);
        lcd.print(ultima_orden); //Para imprimir el resultado en el LCD
        delay(6000);//Mostramos el mensaje durante 6sg
        lcd.clear();//Borramos el lcd para no solapar resultados
        
        String s, trama; // trama tendrá la trama recibida
        int inic, fin, opc, i, N, sol;
        int *v_int; // puntero que apunta al vector de enteros
        float *v_float, f; // puntero que apunta al vector de enteros
        trama = leerTrama('\n'); // lee la trama
        digitalWrite(LED, HIGH); // Se enciende mientras procesa

        //Estudio de cada opción
        s = cortaTrozo(trama, 0, &fin, ':', true); // s (String) recibe la opcion
        inic=fin; // Apuntamos al principio del siguiente campo de la trama
        opc = s.toInt(); // La opción (s) se convierte a entero


        // Estudio de cada petición
        if (opc==1) {
          v_int = obtenListaEnteros(trama, inic, &fin, ',', true, 2); //Recibe dos numeros
          sol = sumatorio(v_int[0],v_int[1]); // devuelve la suma de los enteros
          ultima_orden = String(sol); //almacenamos el String de sol en ultima_orden
          Serial.println(ultima_orden); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
        }
         
        if (opc==2) {
          //n cuadrados de n números
          String cantidad_numeros;
          cantidad_numeros = cortaTrozo(trama, inic, &fin, ',', true); //Extraemos la cantidad de numeros
          inic=fin; // Apuntamos al principio del siguiente campo      
          N = cantidad_numeros.toInt();
          v_int = obtenListaEnteros(trama, inic, &fin, '-', true, N); //Extraemos los numeros que hay que elevar
          ultima_orden = cuadrados(v_int, N); //Almacenamos en ultima_orden     
          Serial.println(ultima_orden); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
        }
        
        if(opc==3){
          //Contar el número de letras
          String texto, letras, veces;
          texto = cortaTrozo(trama, inic, &fin, ',', true);// Extraemos cadena donde queremos buscar
          inic=fin; // Apuntamos al principio del siguiente campo
          letras = cortaTrozo(trama, inic, &fin, '-', true); //Extraemos letras que queremos buscar
          inic=fin; // Apuntamos al principio del siguiente campo
          N = letras.length();
          veces = vecesletra(texto,letras, N);
          ultima_orden = veces; //Almacenamos en ultima_orden
          Serial.println(ultima_orden); // Envía a Python el resultado
          free(v_int); // IMPORTANTE: Libera la memoria de v_int
          }

        if (opc==4) {
          //¿Es palindromo?
          String cadena;
          cadena = cortaTrozo(trama, inic, &fin, ':', true); //Extraemos la cadena de texto
          inic=fin; // Apuntamos al principio del siguiente campo
          s = esPalindromo(cadena);
          ultima_orden = s; //Almacenamos en ultima_orden
          Serial.println( ultima_orden ); // Se envía la trama a Python
        }
  
        if(opc==5){
          //Devolución última orden
          Serial.println(ultima_orden);   // Envía a Python el último resultado almacenado en ultima_orden
          }
          
          digitalWrite(LED, LOW); // Se apaga al terminar de procesar
}

///////////////////////////////// FUNCIONES PRACTICA 4 /////////////////////////////////


// Funcion que devuelve como String el contenido entre dos "car" (carácter)
// comenzando en "inic" y hasta que se encuentra un "car", fin tendrá el
// índice donde comienza el siguiente campo
String cortaTrozo(String s, int inic, int *fin, char car, bool corta) {
        int pos_car;
        pos_car = s.indexOf(car,inic); // posicion de car empezando en inic
        *fin = pos_car + 1; // fin se asigna a donde comienza el siguiente campo
        if (pos_car!=-1) return s.substring(inic,pos_car); // Entre inic y fin
        else if (corta) return s.substring(inic); // Desde inic al final
        else return String("-1"); // Error, devuelve el String "-1"
}


// Devuelve un vector de N enteros a partir de la trama comenzando en "inic"
int *obtenListaEnteros(String linea, int inic, int *fin, char car, bool c, int N) {
        int *v_int, i;
        String s;
        v_int = (int *) malloc(sizeof(int)*N); // Reserva de memoria
        for(i=0;i<N;i++) { // Para cada trozo
          s = cortaTrozo(linea, inic, fin, car, c); // s = v_i como String
          inic=*fin; // Apuntamos al principio del siguiente campo
          v_int[i] = s.toInt(); // s se convierte a entero y se almacena
        }
        return v_int; // Devolución del vector
}



// Devuelve un vector de tam float a partir de la trama comenzando en "inic"
float *obtenListaFloat(String linea, int inic, int *fin, char car, bool c, int N) {
        float *v_float;
        int i;
        String s;
        v_float = (float *) malloc(sizeof(float)*N);
        for(i=0;i<N;i++) { // Para cada trozo
              s = cortaTrozo(linea, inic, fin, car, c); // s = v_i como String
              inic=*fin; // Apuntamos al principio del siguiente campo
              v_float[i] = s.toFloat(); // s se convierte a float y se almacena
        }
        return v_float; // Devolución del vector
}


// Devuelve la suma de los valores enteros en el vector v
int sumaListaEnteros(int v[], int tam) {
        int i, r = 0;
        for(i=0;i<tam;i++) {
            r += v[i];
        }
        return r;
}


// Incrementa cada valor del vector v en f
float incrementaListaEn(float v[], int tam, float M) {
        int i;
        for(i=0;i<tam;i++) {
            v[i] += M;
        }
        return M;
}


// Función que lee una trama terminada en car
String leerTrama(char c) {
        // Espera hasta que haya algo que leer
        while(Serial.available() < 1) {
              delay(1);
        }
        return Serial.readStringUntil(c); // Recibe info hasta '\n'
      }


///////////////////////////////// FUNCIONES PRACTICA 2 /////////////////////////////////

///////////////////////////////// SUMATORIO/////////////////////////////////
int sumatorio (int a, int b){
  int suma=0; //Inicializamos suma a 0
  for(a;a<=b;a++){ //Recorremos el vector donde estan los dos enteros
    suma+=a;  //Los sumamos
  }
  return suma; //Devuelve la suma total
}

///////////////////////////////// CUADRDADOS /////////////////////////////////
String cuadrados(int v_int[], int N){
  int v_cuadrados[N]; //Vector donde almacenamos los cuadrados del primer vector
  String cadena;
  for (int i=0; i<N;i++){
    v_cuadrados[i]=(v_int[i])*(v_int[i]); //Hacemos el cuadrado del numero de v_int
    cadena+= String(v_cuadrados[i]) + " ";
  } 
  return cadena; //Devuelve cadena con los números que le hemos pasado al cuadrado
}

///////////////////////////////// CONTAR LETRAS /////////////////////////////////
String vecesletra(String texto, String letras, int n){
  int vecesletra;
  String vecesletras;
  int len;
  len = texto.length();
  for (int j=0; j<n;j++){ //Recorre las letras a bucar
    vecesletra=0;
    for (int i=0; i<len;i++){
      if (texto[i]==letras[j]){ //Recorre tecto donde hay que buscar
        vecesletra++;
      }
    }
    vecesletras += letras[j] + String(vecesletra) + "veces" + "  "; 
  }
  return vecesletras;  //Devuelve las veces que aparaece cada letra
}

////////////////////////////////// PALINDROMO /////////////////////////////////
String esPalindromo(String palin){
  int longitud;
  int inicio=0,fin;
  longitud=palin.length();  
  for(fin=longitud-1; palin[fin]==palin[inicio] && fin>=0; inicio++,fin--); 
  //Recorre la cadebna que le hemos pasado
  if(inicio==longitud){
    return "Es Palindromo";
  }else{
    return "No es palindromo";
  }
}
