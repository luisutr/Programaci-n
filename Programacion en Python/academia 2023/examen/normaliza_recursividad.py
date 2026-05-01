hiper= [
            [
                [2, 3, 4],
                [1, 2],
                2,
                [1]
            ],
            [
                2,
                [2, 3],
                1,
                4,
                [2, 2, 6, 7]
            ],
            5
        ]

def normalizaconjunto(hiper,d):
    for i in hiper:
        if type(i) == list:
            normalizaconjunto(i, d)
        else:
            if type(hiper) == list:
                # relleno hasta la dimension
                numelem = len(hiper)
                if numelem != d:
                    for j in range(numelem, d):
                        hiper.append(0)
            else:
                sub = []
                for x in range(d):
                    sub.append(0)
                sub[0] = i
                hiper = sub
    return hiper

print(normalizaconjunto(hiper,5))

