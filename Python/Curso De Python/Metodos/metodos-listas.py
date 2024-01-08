#creando una lista con list()
lista = list(["Tomas","Juan",34])
lista_numerica = list([3,2,6,4,5,1,8,7,10,9])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("Lokita")

#agregando un elemento a la lista en un indice especifico
lista.insert(1,"Putaso")

#agregando varios elementos a la lista
lista.extend([False,46,18])

#elimiando un elemento de la lista (por su indice)
lista.pop(0) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove(34)

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena al reves)
lista_numerica.sort()

#invirtiendo los elementos de una lista
lista.reverse()

print(lista)