# creando un conjunto con Set()

conjunto = set(["Dato1", "Dato2"])

#metiendo cojunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1, "Dato3"}

print(conjunto2)

#teoria de conjuntos

numeros_Impares = {1,3,5,7}
numeros = {1,3,7}

#Verificando si es un subconjunto
resultado = numeros.issubset(numeros_Impares)
resultado = numeros <= numeros_Impares

#Verificando si es un superconjunto
resultado = numeros.issuperset(numeros_Impares)
resultado = numeros_Impares > numeros

#verifica si hay algun numero en comun
resultado = numeros.isdisjoint(numeros_Impares)

print(resultado) 