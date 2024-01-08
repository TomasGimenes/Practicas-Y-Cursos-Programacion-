peso = int(input("Dime tu peso: "))
altura = float(input("Dime tu altura: "))

imc = peso / (altura ** 2)

print(f"Tu peso es: {peso}")
print(f"Tu altura es: {altura}")
print(f"Por lo tanto tu IMC es: {imc}")