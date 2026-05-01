def matrnxm(n,m):
    S = []
    for i in range(n):
        S.append([])
        for j in range(m):
            S[-1].append(0)
    return S

print(matrnxm(3,4))