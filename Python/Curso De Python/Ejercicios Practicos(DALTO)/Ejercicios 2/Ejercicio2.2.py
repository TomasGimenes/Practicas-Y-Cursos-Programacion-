numeros = int(input("Dame un numero: "))

def es_primos(num):
    for i in range(2,num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(num):
        resultado = es_primos(i)
        if resultado == True: primos.append(i)
    return primos
            

resultado = primos_hasta(numeros)
print(resultado)