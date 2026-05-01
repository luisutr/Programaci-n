#include <stdio.h>

#define FIL 3
#define COL 2

// Rellenar matriz
void rellenarMatriz(float M[FIL][COL]) {
	int i, j;

	for (i = 0; i < FIL; i++) {
		for (j = 0; j < COL; j++) {
			printf("Dame el valor de la posicion (%d,%d)\n", i,j);
			scanf("%f",&M[i][j]);getchar();
		}
	}
}

// Devuelve el máximo elemento de la fila indicada por el parametro "fila"
float maxFila(float M[FIL][COL], int fila) {
	int j;
	float max;

	max = M[fila][0]; 
	for (j = 0; j < COL; j++) {
		if(M[fila][j]>max) {
			max = M[fila][j];
		}
	}

	return max;
}

// Muestra matriz por pantalla
void mostrarMatriz(float M[FIL][COL]) {
	int i, j;

	for (i = 0; i < FIL; i++)	{
		for (j = 0; j < COL; j++) {
			printf("%.3f ", M[i][j]);
		}
		printf("\n");
	}
}

int main(void) {
	float M[FIL][COL], r;
	int fil;

	// Invocacion a la funcion que rellena la matriz
	rellenarMatriz(M);

	// Invocacion a la funcion que muestra la matriz
	printf("MATRIZ:\n");
	mostrarMatriz(M);

	// Invocacion a la funcion maximoFila
	printf("Dame la fila a buscar su maximo\n");
	scanf("%d",&fil);getchar();
	r = maxFila(M,fil);
	printf("Maximo de fila %d = %.3f\n", fil, r);

	return 0;
}
