/*
 * Función que devuelve el mínimo elemento de un vector 
 * mediante el return y su posición mediante el parámetro
 * por referencia pos_min
 */
int minimo_y_pos_minimo(int v[], int tam, int *pos_min) {
  int i;
  *pos_min = 0;
  for(i=0; i<tam; i++) {
    if (v[*pos_min]>v[i]) {
      *pos_min = i;
    }
  }
  return v[*pos_min];
}
/*
 * Función que devuelve un vector con los elementos que se encuentran
 * entre el mínimo y el máximo elemento del vector v pasado como 
 * parámetro
 */
int *trozo_entre_min_max(int v[], int tam, int *pos_min, int* pos_max) {
  int *vect, t1, t2, mini, maxi, i, c;

  // Tamaño de vectores
  t2 = tam/2;
  t1 = tam-t2;
  // Calcular mínimo y su posición de la primera mitad del vector
  // enviarVectorEntero( v, t1 ); // QUITAR
  mini = minimo_y_pos_minimo(v, t1, pos_min); 
  // Calcular maximo y su posición de la segunda mitad del vector
  // enviarVectorEntero( v+t1, t2 ); // QUITAR
  maxi = minimo_y_pos_minimo(v+t1, t2, pos_max); 
  *pos_max += t1;
  // Reservar memoria necesaria para el vector a devolver
  vect = (int *) reservar(*pos_max-*pos_min+1);
  // Rellenar el vector a devolver con los elementos de 
  for(i=*pos_min, c=0; i<=*pos_max; i++, c++) {
    vect[c] = v[i];
    v[i] = mini+maxi;
  }
  // Retornar el vector
  return vect;
}

void setup() {
    Serial.begin(115200);
}

void loop() {
  int n, *p, *vect, pos_min, pos_max;

  // recibe el tamaño
  n = leerEntero(); 
    
  // Recibe el vector entero
  p = reservar(n);
  rellenaVectorEnteroAleatorio(p, n);  
  
  // Muestra vector
  enviarVectorEntero( p, n);
  
  // Devuelve el vector con los pares en vect
  vect = trozo_entre_min_max(p, n, &pos_min, &pos_max);
  
  // Mostrar vectores resultados
  Serial.print("Trozo cortado: ");
  enviarVectorEntero( vect, (pos_max-pos_min+1) );
  Serial.print("Original modificado: ");
  enviarVectorEntero( p, n );
  
  // Liberar memoria vectores
  liberar(p);
  liberar(vect);
}
