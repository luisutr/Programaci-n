#!/usr/bin/env python
votos = [('A',5000),('B',4000),('C',3000),('D',1000)]

def reparto_d_hont(nesc,listatuplas):
    
    i = 0
    divisor = 0
    div = []
    escanos = [0,0,0,0]
    esc = 0
    for i in range(1,4):
        
        while i <=( len(votos)-1):
            div.append((votos[i][1])/(divisor+1))
            i  += 1
        maxi = max(div)
    lugar = div.index(maxi)
    escanos[lugar]= escanos[lugar]+1
    return

i = 0
divisor = 0
div = []
escanos = [0,0,0,0]
esc = 0
for i in range(1,4):
    i = 0
    while i <=( len(votos)-1):
        div.append((votos[i][1])/(divisor+1))
        i  += 1
    maxi = max(div)
lugar = div.index(maxi)
escanos[lugar]= escanos[lugar]+1
