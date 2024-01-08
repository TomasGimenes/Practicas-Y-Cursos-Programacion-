def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
num = int(input("Ingresa un numero: "))
if es_par(num):
    print("El numero es par.")
else:
    print("El numero es impar.")