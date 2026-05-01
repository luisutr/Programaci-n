def calcular_valor_interpolado(LO, Pos_i):
    """
    Función auxiliar: Solo se encarga de aplicar la fórmula
    matemática dada una lista YA ordenada y una posición.
    """
    # "j la parte entera de Pos_i"
    j = int(Pos_i)
    
    # "parte decimal de Pos_i"
    parte_decimal = Pos_i - j
    
    # RECORDATORIO:
    # La fórmula matemática usa posiciones empezando en 1.
    # Python usa índices empezando en 0.
    # Por tanto, la posición 'j' del texto es el índice [j-1] en Python.
    
    if parte_decimal == 0:
        # Caso sin decimales: Qi = LO[j-1]
        return LO[j - 1]
    else:
        # Caso con decimales: Fórmula de interpolación
        # Valor Base + Decimal * (Siguiente - Base)
        valor = LO[j - 1] + parte_decimal * (LO[j] - LO[j - 1])
        return valor

def cuartiles(L):
    """
    Función principal: Ordena, calcula posiciones y llama a la auxiliar.
    """
    # 1. ORDENAR
    LO = sorted(L)
    N = len(LO)

    # 2. CALCULAR POSICIONES (Según enunciado)
    # Pos = (N + 1) * Porcentaje
    Pos_1 = (N + 1) * 0.25
    Pos_2 = (N + 1) * 0.50
    Pos_3 = (N + 1) * 0.75
    
    # 3. OBTENER LOS VALORES (Llamando a la función independiente)
    Q1 = calcular_valor_interpolado(LO, Pos_1)
    Q2 = calcular_valor_interpolado(LO, Pos_2)
    Q3 = calcular_valor_interpolado(LO, Pos_3)
    
    # Para Q4 el enunciado dice directamente el último valor
    Q4 = LO[-1]

    return Q1, Q2, Q3, Q4

# --- ZONA DE PRUEBA ---
datos = [3, 7, 8, 5, 12, 14, 21, 13, 18]

# Llamada simple para el alumno
q1, q2, q3, q4 = cuartiles(datos)

print(f"Lista Ordenada: {sorted(datos)}")
print(f"Q1 (25%): {q1}")
print(f"Q2 (50%): {q2}")
print(f"Q3 (75%): {q3}")
print(f"Q4 (Max): {q4}")