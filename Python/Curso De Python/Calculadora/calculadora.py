import suma
import resta
import multiplicar
import dividir

preguntar = input("¿Quieres Sumar, Restar, Multiplicar o Dividir?: ")

preguntar.lower()

if preguntar == "sumar":
    preguntar_cantidad = int(input("Dime la cantidad de numeros que quieres sumar: "))
    numero_suma = []
    for i in range(preguntar_cantidad):
        num = int(input("Dime el numero: "))
        numero_suma.append(num)
    resultado = suma.Sumar(*numero_suma)
    print(f"La suma de los numeros es {resultado}")

elif preguntar == "restar":
    preguntar_cantidad = int(input("Dime la cantidad de numeros que quieres restar: "))
    numero_resta = []
    for i in range(preguntar_cantidad):
        num = int(input("Dime el numero: "))
        numero_resta.append(num)
    resultado = resta.Resta(*numero_resta)
    print(f"La resta de los numeros es {resultado}")

elif preguntar == "multiplicar":
    preguntar_cantidad = int(input("Dime la cantidad de numeros que quieres multiplicar: "))
    numero_multiplicar = []
    for i in range(preguntar_cantidad):
        num = int(input("Dime el numero: "))
        numero_multiplicar.append(num)
    resultado = multiplicar.Multiplicar(*numero_multiplicar)
    print(f"La multiplicacion de los numeros es {resultado}")
    
elif preguntar == "dividir":
    preguntar_cantidad = int(input("Dime la cantidad de numeros que quieres dividir: "))
    numero_dividir = []
    for i in range(preguntar_cantidad):
        num = int(input("Dime el numero: "))
        numero_dividir.append(num)
    resultado = dividir.Divicion(*numero_dividir)
    print(f"La divicion de los numeros es {resultado}")