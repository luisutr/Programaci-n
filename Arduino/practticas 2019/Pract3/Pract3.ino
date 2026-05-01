
/* Use File->Load Prog to
   load a different Program
*/

#define TAM 8
int elem = 5;

void setup() {
	Serial.begin(115200);
	randomSeed(analogRead(0));
}

void loop() {
	int v1[TAM];
	double r;
	
	rellenaVectorAleatorio(v1, TAM); // Rellenar primer vector
	Serial.println("____________________________________");
	Serial.print("v1 = "); muestraVector(v1, TAM);
	r = (double) sqrt( a(v1,TAM,elem) * b(v1,TAM,elem) );
	Serial.println( String("r = ") + String(r) );
	delay(2000);
}

int contar(int v[], int tam, int elem) {
	int i, cont;
	
	cont = 0;
	for(i=0;i<tam;i++) {
		if(i==elem) {
			cont++;
		}
	}
	return cont;
}

float a(int v[], int tam, int elem) {
	int i;
	float r;
	
	r = 0.0;
	for(i=0;i<tam;i++) {
		if (v[i]!=elem) {
			r += v[i]*(i-contar(v,i,elem));
		}
	}
	return r;
}

float b(int v[], int tam, int elem) {
	int i;
	float r;
	
	r = 0.0;
	for(i=0;i<tam;i++) {
		if (v[i]!=elem) {
			r += (float) v[i]/(i+1-contar(v,i,elem));
		}
	}
	return r;
}

void rellenaVectorAleatorio(int v[], int tam) {
	int i;
	for(i=0;i<tam;i++) {
		v[i] = random(1,10);
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
