//Jesús Rodríguez Esteban

///////////////////////////////////////////////// FUNCIONAMIENTO PRÁCTICA III ////////////////////////////////////////////////
//Al subir el programa, aparecerá un mensaje inicial con mi nombre y apellido y el numero de la práctica (en este caso III). 
//Se mostrará un menú con cada una de las operaciones, que se corresponden con un número en concreto (0,1,2 o 3).
//Pulsar con la operación deseada.
//Dar pulsaciones con los números se quiera, en total 2 números. 
//Una vez dadas las dos pulsaciones pulsar cualquier botón y mostrará el resultado
//El resultado se mostrará 5 segundos y volverá al menú inicial y podremos volver a introducir cualquier operación.
//IMPORTARNTE: SI SE PULSA UNA TECLA QUE NO SEA UN NÚMERO, DAR 3 PULSACIONES CON CUALQUIER BOTÓN (se indica en el LED)
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//Definimos las bibliotecas necesarias

#include <IRremoteESP8266.h>
#include <IRrecv.h>

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

//Mando Infrarrojo
unsigned long claves[21] = {0xFFA25D,0xFF629D, 0xFFE21D, 0xFF22DD, 0xFF02FD,
0xFFC23D, 0xFFE01F,0xFFA857,0xFF906F,0xFF6897, 0xFF9867, 0xFFB04F, 0xFF30CF,
0xFF18E7, 0xFF7A85, 0xFF10EF, 0xFF38C7, 0xFF5AA5, 0xFF42BD, 0xFF4AB5,0xFF52AD};
String valor[21] = {"No valido", "No valido", "No valido", "No valido", "No valido", "No valido",
"No valido", "No valido", "No valido", "0", "No valido", "No valido", "1", "2", "3", "4", "5", "6", "7", "8","9"};
//Invalidamos todas las posibles pulsaciones que no nos son de interes
//Solo se deberan usar los numeros del mando. No usar los demas botones.

int RECV_PIN = 2; // pin del receptor IR al pin D4 del nodeMCU

IRrecv irrecv(RECV_PIN); // Crea objeto de 'irrecv'
decode_results results; // Crea objeto de 'decode_results'

String operacion,numero1,numero2 = ""; //Definimos las variables que vamos a emplear
int curso = 0;

void setup() {
        Serial.begin(115200);
        irrecv.enableIRIn(); // Inicializa el receptor
        Wire.begin(5, 4);
        lcd.setBacklight(HIGH); //Use predefined PINS consts
        lcd.begin(16,2);
        lcd.home();
        //Mensaje Inicial
        lcd.setCursor(0,0); // Primer digito corresponde a la columna
                            // Segundo digito corresponde a la fila
        lcd.print("Jesus  Rodriguez"); // Autor
        lcd.setCursor(2,1);
        lcd.print("Practica III");
        delay(2000); //Espereamos 2sg y desaparece el mensaje inicial
        lcd.clear(); //Limpiamos el lcd

        //Definimos el menu
        lcd.setCursor(1,0); 
        lcd.print("Opc0:+"); //Opcion para sumar
        lcd.setCursor(9,0); 
        lcd.print("Opc1:-"); //Opcion para restar

        lcd.setCursor(1,1); 
        lcd.print("Opc2:x"); //Opcion para multiplicar
        lcd.setCursor(9,1);
        lcd.print("Opc3:/"); // Opcion para dividir
        delay(1000);
}


void loop() {
                  String s;
                  if (irrecv.decode(&results)) { // Si se ha recibido alguna señal
                    s = getValor(results.value); // Recoge cadena desde código
                  curso +=1;
                  
                    switch (curso){
                      case 1: //Recibe la orden a realizar
                        lcd.clear();
                        operacion = s;
                        lcd.setCursor(2,0);
                        lcd.print("Operacion: " + operacion);
                        delay(200);
                        
                        if (operacion == "0"){ //En funcion de la operacion, dibujamos el lcd
                                                //de la manera mas grafica y sencilla posible
                          lcd.setCursor(0,1);
                          lcd.print("Sumar");
                          lcd.setCursor(9,1);
                          lcd.print("+");
                          lcd.setCursor(11,1);
                          lcd.print("=");
                          delay(200);
                        }
                        
                        else if (operacion == "1"){
                          lcd.setCursor(0,1);
                          lcd.print("Restar");
                          lcd.setCursor(9,1);
                          lcd.print("-");
                          lcd.setCursor(11,1);
                          lcd.print("=");
                          delay(200);
                        }
                        
                        else if (operacion == "2"){
                          lcd.setCursor(0,1);
                          lcd.print("Multipl");
                          lcd.setCursor(9,1);
                          lcd.print("x");
                          lcd.setCursor(11,1);
                          lcd.print("=");
                          delay(200);
                        }
                        
                        else if (operacion == "3"){
                          lcd.setCursor(0,1);
                          lcd.print("Dividir");
                          lcd.setCursor(9,1);
                          lcd.print("/");
                          lcd.setCursor(11,1);
                          lcd.print("=");
                          delay(200);
                        }
                        
                        else{
                          lcd.clear();;
                          lcd.setCursor(0,0);
                          lcd.print("No valido. Da");
                          delay(200);
                          lcd.setCursor(0,1);
                          lcd.print("tres pulsaciones");
                          delay(200);
                        }
                        break;
                        
                      case 2:  //Recibe el primer numero
                        numero1 = s;
                        lcd.setCursor(8,1);
                        lcd.print(s);
                        delay(200);
                        break;
                        
                      case 3: //Recibe el segundo numero
                        numero2 = s;
                        lcd.setCursor(10,1);
                        lcd.print(s);
                        delay(200);
                        break;
                        
                      case 4: //Muestra el resultado por pantalla
                        String resultado = funciones(operacion,numero1,numero2);
                        lcd.setCursor(12,1);
                        lcd.print(resultado); //Es necesario dar a cualquier boton para ver el resultado
                        operacion,numero1,numero2 = "";
                        delay(5000);
                        curso=0;            //Esperamos 5sg para volver a introducir otra cuenta
                        lcd.clear();        //Limpiamos el lcd para proceder a la nueva operacion

                        //Volvemos a mostar el menu
                        lcd.setCursor(1,0); 
                        lcd.print("Opc0:+"); //Opcion para sumar
                        lcd.setCursor(9,0); 
                        lcd.print("Opc1:-"); //Opcion para restar
                
                        lcd.setCursor(1,1); 
                        lcd.print("Opc2:x"); //Opcion para multiplicar
                        lcd.setCursor(9,1);
                        lcd.print("Opc3:/"); // Opcion para dividir
                        delay(1000);
                        break;
                    }
                    irrecv.resume(); // Recibir el siguiente valor
                  }
}


String funciones(String op,String n1,String n2){ //Operaciones matematicas a realizar
  int operacion = op.toInt();
  int numero1 = n1.toInt();
  int numero2 = n2.toInt();

  if (operacion == 0){
    return String(numero1+numero2); //Suma
  }
  else if (operacion == 1){
    return String(numero1-numero2); //Resta
  }
  else if (operacion == 2){
    return String(numero1*numero2);  //Multiplicación
  }
  else if (operacion == 3){
    float fn1=(float)numero1; //DIvidiremos con floats para mostrar decimales
    float fn2=(float)numero2;
    return String(fn1/fn2); //División
  }
  else{
    curso = 0;
    return "Operacion incorrecta";
  }
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
