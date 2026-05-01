def incrementa(l):
	s = []
	for e in l:
		if (e%2)==0:
			s.append(e+2)
		else:
			s.append(e+1)
	return s

def incCompresion(l):
	return [e+2 if (e%2)==0 else e+1 for e in l]

print( incrementa([1,2,4,3,5,7,6,8]) )
