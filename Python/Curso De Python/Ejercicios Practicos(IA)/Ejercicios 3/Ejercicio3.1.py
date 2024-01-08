num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))

numeros_ingresados = (num1, num2)

suma = num1 + num2
multiplicar = num1 * num2
dividir = num1 / num2
resta = num1 - num2

resultado = (suma, multiplicar, dividir, resta)

print(f"El resultado de todo es: {resultado}")
print(numeros_ingresados)
