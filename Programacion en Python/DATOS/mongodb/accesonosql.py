from pymongo import MongoClient

# Establecer conexión con la base de datos sin autenticación
cliente = MongoClient('localhost', 27017)
basededatos = cliente['primera_db']
coleccion_clientes = basededatos['clientes']
################  INSERTAR ###################
'''
informacion_cliente = {
"nombre": "García",
"direccion": "Calle Ejemplo 10",
"codigo_postal": "46006",
"ciudad": "Valencia"
}
coleccion_clientes.insert_one(informacion_cliente)

informacion_cliente = [
{
"nombre" : "García",
"direccion" : "Calle Ejemplo 10",
"codigo_postal" : "46006",
"ciudad" : "Valencia"
},
{
"nombre" : "Rodríguez",
"direccion" : "Calle Principal 1",
"codigo_postal" : "28007",
"ciudad" : "Madrid"
},
{
"nombre" : "González",
"direccion" : "Calle Amplia 2",
"codigo_postal" : "36002",
"ciudad" : "Pontevedra"
}
]
coleccion_clientes.insert_many(informacion_cliente)
'''
############# CONSULTAR ####################
datos = coleccion_clientes.find ( { "ciudad" : "Valencia" } )
for info in datos:
    print(info['nombre'])

################ UPDATE #############
myquery = { "direccion" : "Calle Ejemplo 10" }
newvalues = { "$set" : { "direccion" : "Calle Diferente 82" } }
coleccion_clientes.update_one (myquery, newvalues)
for x in coleccion_clientes.find ():
    print(x)

## VARIOS
myquery = { "nombre" :{"$regex" : "^G" }}
newvalues = { "$set" : { "ciudad" : "Cádiz" } }
x = coleccion_clientes.update_many (myquery, newvalues)
print (x.modified_count, "documents updated.")
for x in coleccion_clientes.find ():
    print(x)

##############  ELIMINAR ###################
myquery = { "dirección" : "Calle Amplia 2" }
coleccion_clientes.delete_one (myquery)

#### VARIAS
myquery = { "nombre" :{"$regex" : "^G" }}
x = coleccion_clientes.delete_many (myquery)

### TODAS

x = coleccion_clientes.delete_many ( { } )
print (x.deleted_count, "documents deleted.")