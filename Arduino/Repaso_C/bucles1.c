#include<stdio.h>

// Funcion para calcular una potencia
int potencia(int base, int exp) {
	int p = 1, i;
	for(i=1;i<=exp;i++) {
		p = p * base;
	}
	return p;
}

// Funcion para calcular una potencia
int potenciaWhile(int base, int exp) {
	int p, i;
	
	p = 1;
	i = 1;
	while(i<=exp) {
		p = p * base;
		i++;
	}
	return p;
}

// Funcion para calcular una potencia
int potenciaDoWhile(int base, int exp) {
	int p, i;
	
	p = 1;
	i = 1;
	do {
		p = p * base;
		i++;		
	} while(i<=exp);
	
	return p;
}

// Programa principal
int main(void)
{
	// Muestra el resultado de 2^3
	printf("Resultado = %d\n",potenciaDoWhile(3, 2));
	return 0;
}
