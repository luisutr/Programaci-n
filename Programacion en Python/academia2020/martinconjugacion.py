def presente_indicativo(verbo):
    conjugado = []
    raiz = verbo[:-2]
    terminacionpresente = {'ar':('o','as','a','amos','áis','an'),'er':('o','es','e','emos','éis','en'),'ir':('o','es','e','imos','ís','en')}
    conjugacion = verbo[-2:]
    conjugaciones = terminacionpresente[conjugacion]
    for terminacion in conjugaciones:
        x = raiz + terminacion
        conjugado.append(x)
    return conjugado

print(presente_indicativo('amar'),['amo', 'amas', 'ama', 'amamos', u'amáis', 'aman'])
print(presente_indicativo('leer'), ['leo', 'lees', 'lee', 'leemos', u'leéis', 'leen'])
print(presente_indicativo('batir'), ['bato', 'bates', 'bate', 'batimos', u'batís', 'baten'])
print(presente_indicativo('ir'), ['o', 'es', 'e', 'imos', u'ís', 'en'])