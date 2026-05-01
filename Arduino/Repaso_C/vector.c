#define TAM 8

#include<stdio.h>

// Rellenar vector de tamanno tam
void rellenar(double vect[], int tam) {
	int i;

	for(i = 0; i < tam; i++) {
		printf("Dame un valor entero para la posicion %d\n", i);
		scanf("%lf", &vect[i]);getchar();
	}
} 

// Mostrar vector de tamanno tam
void mostrar(double vect[], int tam) {
	int i;

	printf("[");
	for(i = 0; i < tam; i++) {
		if(i==tam-1) {
		printf("%.3f", vect[i]);
		} else {
			printf("%.3f, ", vect[i]);
		}
	}
	printf("]\n");
}

// Dividir por tods los elementos de un vector de tamanno tam
void dividir2(double vect[], double vect1[], int tam) {
	int i; 
	i = 0;
	while(i<tam) {
		vect1[i] = vect[i]/2;
		i++;
	}
} 
int main(void) {
	double v[TAM], w[TAM]; // TAM celdas que se acceden con los indices del 0 al TAM-1

	//Rellenar vector
	rellenar(v, TAM);

	// Mostrar vector
	printf("v = ");
	mostrar(v, TAM);

	// Dividir valor de cada celda entre 2 mediante un bucle while
	dividir2(v, w, TAM);

	// Mostrar vector de nuevo
	printf("w = ");
	mostrar(w, TAM);

	return 0;
}
