#include <stdio.h>
#include <stdlib.h>

/*
 Estructura TNodo que posee dos atributos, data con el valor y otro mismo TNodo auxiliar
 Este auxiliar nos vale para almanecar todos los nodos que necesitemos.
 */
typedef struct TNodoAux
{
    int data;
    struct TNodoAux* next;
} TNodo;

/*
 Esta función recibe una lista tipo Tnodos y devuelve un valor entero con la cantidad de elementos que tiene dicha lista. Utiliza un contador con un while para recorrer hasta que el ultimo nodo apunte a NULL, incrementando un contador que lleva la cuenta de los nodos.
 */
int get_size(TNodo* lista)
{
    int counter = 0;
    TNodo* it = lista;
    if(it != NULL)
    {
        counter++;
        while(it->next!=NULL)
        {
            it = it->next;
            counter++;
        }
     }
    return counter;
}

/*
 Rebide una lista de Tnodos y un valor entero denominado posicion, el cual es usado para
 encontrar el nodo deseado. Recorremos en este caso mediante un for dicha lista y en cuento llega a la posición devuelve este nodo mediente return a la función que la llamo.
 recorre hasta posición menos uno, dado que el reccorido empieza desde cero.
 Si la posición no perteneciera a la lista, es menor o igual que cero o por el contrario superior a la cantidad de elementos nodos, nos muestra un mensaje de error.
 */
TNodo* get_node(TNodo* lista, int pos)
{
    if(pos <= 0 || pos > get_size(lista))
    {
        fprintf(stderr, "Posicion %d no válida; máx = %d\n",
                pos, get_size(lista));
        return NULL;
    }
    TNodo* it = lista;
    for (int i=0; i<pos-1; i++)
        it = it->next;
    return it;
}

/*
 Recibe la lista de Tnodos y nos devuelve el ultimo elemento nodo, recorre mediente un while hasta que el nodo que encuentra apunta a NULL, que quiere decir que ha llegado a el ultimo.
 */
TNodo* get_last(TNodo* lista)
{
    TNodo* it = lista;
    while(it->next!=NULL) it = it->next;
    return it;
}

/*
 La función push es usada para almacenar nuevos nodos en la lista, recibe como parametros la lista de Tnodos y el valor que queremos introducir en el nuevo nodo. Es diferente a instertar, push siempre por defición introduce al final de la lista.
 Ha sido modificada para ser capaz de crear un nuevo Nodo si no existe la lista (lista es NULL). Reserva espacio para el nuevo nodo, asigana el valor que queremos introducir y hace que el atributo next del nuevo nodo apunte NULL. Si existen elementos en la lista, hace que el ultimo nodo apunte al nuevo.
 Sino existen nodos, hace que la lista se inicialice con el nuevo nodo creado.
 */
void push(TNodo** lista, int valor)
{
    TNodo* nuevo_nodo = (TNodo*)malloc(sizeof(TNodo));
    nuevo_nodo->data = valor;
    nuevo_nodo->next = NULL;
    if (*lista!=NULL)
        {
            TNodo* ultimo = get_node(*lista, get_size(*lista));
            ultimo->next = nuevo_nodo;
        }
    else
        {
            *lista = nuevo_nodo;
        }
}

/*
 La función insert a diferencia de Push es capaz de introducir el nodo en una posición indicada. Recibe como parametros de entrada, la lista de Tnodos, la posición donde queremos guardar y el valor que queremos guardar.
 Si no es posible guardar valor, devuelve que la posición no es valida.
 Si es posible crea e inicializa un nuevo nodo como hace push. Recorre la lista hasta la posición donde queremos introducir, llegada a esa posición hacemos que el nuevo nodo apunte a los siguientes nodos que quedan en la lista.
 Si la posición era la primera, tan solo con guardar en la lista ese nodo hemos terminado.
 De no ser así, el nodo anterior de la lista (es decir la lista de nodos hasta la posición donde queria insertar) hago que apunte a al nuevo nodo, que ya esta encadenado, este y los nodos posteriores.
 */
void insert(TNodo** lista, int pos, int valor)
{
    if (pos <= 0 || pos > (get_size(*lista)))
        {
            fprintf(stderr, "Posición %d no válida; max = %d\n", pos, get_size(*lista) + 1);
            return;
        }
    TNodo* nuevo_nodo = (TNodo*)malloc(sizeof(TNodo));
    nuevo_nodo->data = valor;
    TNodo* it_anterior = NULL;
    TNodo* it_actual = *lista;
    int i = 1;
    while (it_actual != NULL && i != pos)
        {
            it_anterior = it_actual;
            it_actual = it_actual->next;
            i++;
        }
    nuevo_nodo->next = it_actual;
    if(pos==1)
        {
            *lista = nuevo_nodo;
        }
    else
        {
            it_anterior->next = nuevo_nodo;
        }
}
/*
 Remove hace algo muy similar a insertar, pero en este caso, recorreo por while hasta la posición y posteroir si la posición anteroir es null es que hemos eliminado el ultimo nodo y podemos guardar la lista.
 de no ser así, al nodo anterior (hasta la posición donde recorrimos, sin llegar a la posición del que queremos eliminar) encadeno los nosods que quedaban.
 */
void remove_node(TNodo** lista, int pos)
{
    if (pos <= 0 || pos > get_size(*lista))
    {
            fprintf(stderr, "Posición %d invalida; max = %d\n", pos, get_size(*lista));
            return;
        }
    TNodo* it_anterior = NULL;
    TNodo* it_actual = *lista;
    int i = 1;
    while (it_actual != NULL && i != pos)
        {
            it_anterior = it_actual;
            it_actual = it_actual->next;
            i++;
        }
    if (it_anterior == NULL)
    {
            *lista = (*lista)->next;
    } else
    {
        it_anterior->next = it_actual->next;
    }
    free(it_actual);
}
/*
 dadas dos listas de nodos, recorro la lista2 de los nodos que quiero concatenar y al ultimo nodo lista1 voy haciendo push de los nodos de la lista2
 */
void concat(TNodo** lista1,TNodo* lista2)
{
    TNodo* it= lista2;
    while(it != NULL)
    {
        push(lista1, it->data);
        it = it->next;
    }
}

void print(TNodo* lista)
{
    TNodo* it_print = lista;
    while(it_print!=NULL)
    {
        printf("[%d]", it_print->data);
        it_print = it_print->next;
    }
    printf("\n");
}


/*
 
 */
int main(){
    TNodo* list = NULL; /* init */
    printf("size = %d\n", get_size(list));
    push(&list, 2);
    printf("size = %d\n", get_size(list));
    push(&list, 3);
    printf("size = %d\n", get_size(list));
    push(&list, 4);
    printf("size = %d\n", get_size(list));
    push(&list, 5);
    printf("size = %d\n", get_size(list));
    TNodo* node = get_node(list, 50);
    if (node != NULL)
            printf("[%d]\n", node->data);
    insert(&list, 6, 6);
    print(list);
    insert(&list, 1, 3);
    print(list);
    insert(&list, 2, 4);
    print(list);
    insert(&list, 0, 1);
    print(list);
    TNodo* another_list = NULL;
    push(&another_list, 7);
    push(&another_list, 8);
    push(&another_list, 9);
    push(&another_list, 10);
    concat(&list, another_list);
    print(list);
    print(another_list);
    remove_node(&list, -1);
    remove_node(&list, 1);
    print(list);
    remove_node(&list, 4);
    print(list);
    remove_node(&list, 2);
    print(list);
    remove_node(&list, 1);
    print(list);
    remove_node(&list, 1);
    print(list);
    remove_node(&list, 1);
    return 0;
}
