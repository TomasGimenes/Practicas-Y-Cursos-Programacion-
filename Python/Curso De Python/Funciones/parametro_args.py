#forma no optima de sumar valores
def sumar(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados
resultado1 = sumar([2,2,2,2])
print(resultado1)

#Otra forma optima de suma valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total([10,20,40,10])
print(resultado2)

#Lo mismo de arriba pero utilizando el operador * como parametro (*args)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado3 = suma("Tomy" ,10,20,40,10)
print(resultado3)