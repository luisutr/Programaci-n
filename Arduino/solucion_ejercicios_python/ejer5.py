#[-inf,-1], (-1,-0.5], (-0.5,0.5], (0.5,1], (1,inf] => 'muy bajo', 'bajo', 'medio', 'alto' y 'muy alto' respectivamente

def float_a_cadena(v):
	if v<=-1.:
		return 'muy bajo'
	elif v>-1. and v<=-0.5:
		return 'bajo'
	elif v>-0.5 and v<=0.5:
		return 'medio'
	elif v>-0.5 and v<=1.:
		return 'alto'
	else:
		return 'muy alto'
	
def intervalos(l):
	return [float_a_cadena(f) for f in l]

print( intervalos([0.5,-0.5, 1.2, 0.3, -0.3, 1., -1.]) )
	
