def sol_equa(n):
    lasi = []
    for i in range(n):
        for j in range(n):
            if (i - 2 * j) * (i + 2 * j) == n:
                lasi.append((i, j))
            else:
                continue

    return lasi

print(sol_equa(90005))