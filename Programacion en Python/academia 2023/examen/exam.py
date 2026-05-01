
def movmean(x,n):
  resultado = []
  for i in range(len(x)):
    inicio = i-(n-1) if i-(n-1) >= 0 else 0
    resultado.append(sum(L[inicio:i+1]) / n)

  return resultado



movmean([1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1],2)