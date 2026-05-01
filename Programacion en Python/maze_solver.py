G = [[0, 1], [0, 2], [1, 3], [2, 19], [3, 4], [3, 5], [4, 6], [5, 20], [6, 7], [7, 21], [8, 9], [8, 10], [9, 11], [10, 22], [11,  12], [12, 13], [14, 15], [14, 16], [15, 17], [16, 23], [17, 18], [18, 24], [20, 25], [21, 26], [24, 32], [25, 33], [26, 22], [27, 28], [27, 29], [28, 30], [29, 34], [30, 31], [31, 23], [32, 35], [34, 44], [35, 50], [36, 37], [36, 38], [37, 33], [38, 51], [39, 40], [39, 41], [40, 42], [41, 52], [42, 43], [43, 53], [44, 54], [45, 46], [45, 47], [46, 48], [47, 55], [48, 49], [49, 35], [50, 56], [51, 57], [52, 60], [53, 61], [55, 62], [57, 58], [58, 59], [59, 66], [60, 67], [61, 54], [62, 68], [63, 64], [63, 65], [64, 56], [65, 69], [66, 73], [67, 74], [68, 79], [69, 80], [70, 71], [70, 72], [71, 66], [72, 83], [73, 84], [74, 75], [75, 76], [76, 85], [77, 78], [78, 86], [79, 87], [80, 81], [81, 82], [82, 88], [83, 89], [84, 90], [85, 93], [86, 94], [87, 95], [88, 98], [89, 99], [90, 100], [91, 92], [92, 101], [93, 102], [94, 103], [95, 104], [96, 97], [97, 105], [98, 106], [99, 107], [100, 108], [100, 109], [102, 110], [103, 111], [104, 112], [105, 113], [107, 114], [108, 101], [109, 115], [110, 116], [111, 117], [112, 118], [113, 106], [114, 119], [117, 123], [118, 124], [119, 130], [120, 121], [120, 122], [121, 116], [122, 131], [123, 132], [124, 133], [125, 126], [125, 127], [126, 128], [127, 134], [128, 129], [129, 135], [130, 136], [130, 137], [131, 140], [132, 143], [133, 144], [134, 145], [135, 146], [136, 138], [137, 147], [138, 139], [139, 148], [140, 141], [141, 142], [142, 132], [143, 149], [144, 150], [145, 151], [146, 152], [147, 153], [148, 154], [150, 159], [150, 160], [152, 161], [153, 162], [154, 155], [155, 156], [156, 157], [157, 158], [158, 149], [159, 151], [160, 163], [161, 164], [163, 174], [164, 176], [165, 166], [165, 167], [166, 168], [167, 177], [168, 169], [169, 170], [170, 171], [171, 172], [172, 173], [173, 178], [174, 175], [176, 179], [178, 186], [179, 192], [180, 181], [181, 177], [182, 183], [183, 184], [184, 185], [185, 193], [186, 194], [187, 188], [187, 189], [188, 190], [189, 195], [190, 191], [191, 196], [192, 197], [193, 205], [194, 206], [196, 207], [197, 208], [198, 199], [198, 200], [199, 201], [200, 209], [201, 202], [202, 203], [203, 204], [204, 193], [205, 210], [206, 195], [207, 197], [208, 211], [209, 212], [212, 225], [213, 214], [214, 215], [215, 216], [216, 210], [217, 218], [217, 219], [218, 220], [219, 226], [220, 221], [221, 227], [222, 223], [222, 224], [223, 211], [224, 228], [225, 229], [225, 230], [227, 238], [229, 231], [230, 241], [231, 232], [232, 233], [233, 234], [234, 242], [235, 236], [235, 237], [236, 226], [237, 243], [238, 228], [239, 240], [240, 244], [241, 245], [242, 247], [243, 248], [245, 246], [247, 243], [248, 249], [249, 250], [250, 251], [251, 252], [252, 253], [253, 254], [254, 244]]


def recorre(G, I, camino, partida, soluciones=[], salida=[]):
    if partida!=[]:
        conexion=partida
        partida=[]
    else:
        conexion = conect(G,I)
    if conexion != -1:
        if conexion[0]==I:
            I = conexion[1]
        else:
            I=conexion[0]
        G.pop(G.index(conexion))
        camino.append(conexion)
        recorre(G,I,camino, partida)
        #El truco
        todas_salidas(G,I)
        if 0 in conexion:
            #print("Salida")
            salida=camino
            return soluciones, salida
            #print(camino)
    else:
        #print("No salida")
        soluciones.append(camino)
        #print(camino)
    return soluciones, salida

def conect(G,I):
    for i in G:
        if I in i:
            return i
    return -1

def todas_salidas(Grafo,I):
    todas=[]
    soluciones=[]
    salida=[]
    for i in Grafo:
        if I in i:
            todas.append(i)
    for j in todas:
        soluciones, salida=recorre(Grafo,I,[],j)
    if soluciones:
        if caminoconsalida(soluciones)!=-1:
            return soluciones

def caminoconsalida(soluciones):
    caminos = len(soluciones)-1
    while caminos>1:
        for i in soluciones[caminos]:
            if 0 in i:
                return soluciones[caminos]
        caminos-=1
    return -1


#print(todas_salidas(G,188))

def recodificar(salidas,eslavon, salida):
    for i in salidas:
        for j in range(len(i)):
            if eslavon[0] in i[j]:
                return i[0:j+1]+salida
            if eslavon[1] in i[j]:
                return i[0:j+1]+salida

def cortaencero(S):
    for i in range(len(S)):
        if 0 in S[i]:
            return S[0:i+1]
    return S

def tuplas2listas(G):
    lista=[]
    for t in G:
        lista.append(list(t))
    return lista

def copiagrafo(G):
    copia=[]
    for i in G:
        copia.append(i)
    return copia

def maze_solver(G,origen):
    copia = copiagrafo(sorted(G))
    copia = tuplas2listas(copia)
    saidas=todas_salidas(copia,origen)
    for i in saidas:
        for j in i:
            if 0 in j:
                salida = i
    salida = recodificar(saidas, salida[0],salida)
    return cortaencero(salida)


print(maze_solver(G,188))