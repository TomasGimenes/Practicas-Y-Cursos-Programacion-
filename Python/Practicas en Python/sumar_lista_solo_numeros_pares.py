# Este programa agarra todos los numeros pares de una lista y los suma
lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def identificar_pares(lista):
    nueva_lista = [i for i in lista if i % 2 == 0]
    return nueva_lista

def sumar_numeros_pares(lista):
    lista_con_pares = identificar_pares(lista)
    resultado_final = sum(lista_con_pares)
    return lista_con_pares, resultado_final

pares, suma_pares = sumar_numeros_pares(lista)
print(f"Los numeros pares de la lista son: {pares}")
print(f"Y la suma de todos los numeros pares es: {suma_pares}")