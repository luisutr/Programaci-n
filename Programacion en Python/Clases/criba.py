def criba(n):
    """buscar numeros primas hasta 'n'."""
    a = [False] * 2 + [True] * (n - 1)  # inicializa una lista de elementos True y False
    for (i, primo) in enumerate(a):
        if primo:
            for x in range(i * i, n, i):
                a[x] = False
    return [j for (j, k) in enumerate(a) if k == True]
