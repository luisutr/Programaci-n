
/* Use File->Load Prog to
   load a different Program
*/

#define TAM 8

void setup() {
	Serial.begin(115200);
	randomSeed(analogRead(0));
}

void loop() {
	int v1[TAM], v2[TAM], r1[TAM];
	
	rellenaVectorAleatorio(v1, TAM); // Rellenar primer vector
	rellenaVectorAleatorio(v2, TAM); // Rellenar segundo vector
	sumaVectores(v1, v2, r1, TAM);
	Serial.println("____________________________________");
	Serial.print("v1 = "); muestraVector(v1, TAM);
	Serial.print("v2 = "); muestraVector(v2, TAM);
	Serial.print("r1 = "); muestraVector(r1, TAM);
	
	delay(2000);
}

void rellenaVectorAleatorio(int v[], int tam) {
	int i;
	for(i=0;i<tam;i++) {
		v[i] = random(0,10);
	}
}

void sumaVectores(int v1[], int v2[], int r[], int tam) {
	int i;
	for(i=0;i<tam;i++) {
		r[i] = v1[i] + v2[i];
	}
}

void muestraVector(int v[], int tam){
	int i;
	String s;
	for(i=0;i<tam;i++) {
		if(i==0) {
			s += String("[") +String(v[i]);
		} else {
			s += String(", ") + String(v[i]);
		}
	}
	Serial.println(s+String("]"));
}
