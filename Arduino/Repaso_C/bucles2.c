#include <stdio.h>

// Sumatorio utilizando bucle for
int sumatorioFor(int num) {
	int total, i;

	total = 0;
	for(i = 1; i <= num; i++) {
		total = total + i;
	}
	return total;
}

// Sumatorio utilizando bucle while
int sumatorioWhile(int num) {
	int total, i;

	total = 0;
	i = 0;
	while(i<num) {
		i++;
		total = total + i;
	}
	return total;
}

// Sumatorio utilizando bucle do/while
int sumatorioDoWhile(int num) {
	int total, i;

	total = 0;
	i = 0;
	do {
		total = total + i;
		i++;
	} while(i<num);
	return total;
}

int main() {
	int n, r;

	// Leyendo el valor n para los diferentes casos
	printf("Dame el numero final\n");
	scanf("%d", &n);

	// Sumatorio hasta un numero indicado por el usuario
	// utilizando el bucle for
	r = sumatorioFor(n);
	printf("FOR: r = %d\n", r);

	// Sumatorio hasta un numero indicado por el usuario
	// utilizando el bucle while
	r = sumatorioWhile(n);
	printf("WHILE: r = %d\n", r);

	// Sumatorio hasta un numero indicado por el usuario
	// utilizando el bucle do/while
	r = sumatorioDoWhile(n);
	printf("DO/WHILE: r = %d\n", r);
	
	return 0;
}
