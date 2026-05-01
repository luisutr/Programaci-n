#include <stdio.h>

enum {MAX = 10};

typedef struct
{
  float datos[MAX];
  int cima;
} TPila;

void init(TPila* pila)
{
    pila->cima = 0;
}

void push(TPila* pila, float dato)
{
  pila->datos[pila->cima++] = dato;
}

float pop(TPila* pila)
{
    return pila->datos[--pila->cima];
}

int main(int argc, char *argv[])
{
  TPila pila;

  init(&pila);

  push(&pila, 1.0);
  push(&pila, 1.5);
  push(&pila, 2.0);
  push(&pila, 2.5);
  push(&pila, 3.0);
  
  for(int i=0; i<27; i++)
    push(&pila, 3.0);

  for(int i=0; i<27; i++)
    printf("%f\n", pop(&pila));





  return 0;
}
