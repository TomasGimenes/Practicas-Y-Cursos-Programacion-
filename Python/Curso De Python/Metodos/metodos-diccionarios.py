diccionario = {
    "nombre" : 'tomas',
    "apellido" : 'gimenes',
    "edad" : 18
}

#devolver las claves del diccionario
claves = diccionario.keys()

#devolver el valor de una clave (si no encuentra nada el programa continua)
valor_de_clave = diccionario.get("nombre")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario (por su clave)
diccionario.pop("nombre")

#obteniando un elemento dict_item iterable
diccionario_iterable = diccionario.items(1)

print(diccionario_iterable)