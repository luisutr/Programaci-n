def es_entero(e):
	try:
		v = int(e)
		return True
	except:
		return False

def es_vocal(e):
	# se puede mejorar usando una cadena o lista o tupla
	if e=='a' or e=='e' or e=='i' or e=='o' or e=='u' or \
		e=='A' or e=='E' or e=='I' or e=='0' or e=='U':
		return True
	return False 

def es_letra_no_vocal(e):
	return (e>='a' and e<='z') or (e>='A' and e<='Z') and not es_vocal(e)
	
def contarCadena(s):
	e, v, l, o = 0, 0, 0, 0
	for i in s:
		if es_entero(i):
			e+=1
		elif es_vocal(i):
			v+=1
		elif es_letra_no_vocal(i):
			l+=1
		else:
			o+=1	
	return e, v, l, o

def contarCadenaWhile(s):
	e, v, l, o = 0, 0, 0, 0
	i = 0
	while i<len(s):
		if es_entero(s[i]):
			e+=1
		elif es_vocal(s[i]):
			v+=1
		elif es_letra_no_vocal(s[i]):
			l+=1
		else:
			o+=1	
		i+=1
	return e, v, l, o

ents, vocals, letras, otros = contarCadena('a2;3onNjlF2I1tuZ-')
print(ents, vocals, letras, otros)

ents, vocals, letras, otros = contarCadenaWhile('a2;3onNjlF2I1tuZ-')
print(ents, vocals, letras, otros)


