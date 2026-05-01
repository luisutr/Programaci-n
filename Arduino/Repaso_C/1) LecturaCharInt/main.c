#include<stdio.h>

int main() {
	int i = 0;
	int p[10]={1,2,3,4,5,6,7,8,9,10};
	unsigned char *c;
	int q[5]={0,0,0,0,0};
	unsigned char *d;
	int pos, n;

	// pedir inicio
	printf("Dame la posición origen\n");
	scanf("%d",&pos);getchar();
	printf("¿Cuantos valores quieres copiar?\n");
	scanf("%d",&n);getchar();

	// Asignacion de punteros
	c = (unsigned char *) &p[pos];
	d = (unsigned char *) q; // esta orden tambien se escribir "d = (unsigned char *) &q[0];"

	// Copiado de valores de byte en byte
	for(i=0; i<(int) sizeof(int)*n; i++) {
		d[i] = c[i];
	}

	// Mostrar vector destino, es decir, q
	for(i=0; i < 5; i++) {
		printf("%d ", q[i]);
	}	
	return 0;
}
