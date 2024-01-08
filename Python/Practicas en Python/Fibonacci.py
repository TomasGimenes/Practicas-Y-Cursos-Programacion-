rango_nemerico = 15


def obtener_fibonacci(numero):
    if numero <= 1:
        return numero
    return obtener_fibonacci(numero-1) + obtener_fibonacci(numero-2)

def suma_fibonacci(rango):
    lista = []
    for i in range(1,rango +1):
        resultado = obtener_fibonacci(i)
        lista.append(resultado)
    print(lista)

suma_fibonacci(rango_nemerico)