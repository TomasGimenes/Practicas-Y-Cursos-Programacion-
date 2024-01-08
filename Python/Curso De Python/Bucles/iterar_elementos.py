animales = ["Perro", "Gato", "Sapo", "Avion", "Escorpion"]
numeros = [10, 20, 40, 60, 90]

#Recorriendo la lista animales
for animal in animales:
    print(f"Ahora la variable animal es igual a: {animal}")

#Recorriendo la lista numeros y multiplicandola por 2
for numero in numeros:
    print(numero * 2)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros, animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#iterando nueros del 5 al 10 sin contar el 10
for num in range(5, 10):
    print(num)

#manera incorrecta de recorrer una lista (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#manera correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice}")
    print(f"el valor es: {valor}")
    
#usando el else
for numero in numeros:
    print(f"ejecurando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona exactamente igual para tuplas y conjuntos
