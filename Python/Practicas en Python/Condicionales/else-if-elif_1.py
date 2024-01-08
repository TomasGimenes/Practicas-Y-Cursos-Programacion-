
#Dado un entero, x, realizar las siguientes acciones condicionales:

# Si x es extraño, imprimir "Extraño"
# Si x es uniforme y en el rango inclusivo de 2 a 5, imprimir "No extraño"
# Si x es uniforme y en el rango inclusivo de 6 a 20, imprimir "Extraño"
# Si x es incluso y mayor que 20, imprimir "No extraño"

numero = int(input("dame un numero entero: "))

def deteccion_num_extraño(num):
    if num < 2:
        print(f"El numero {num} es extraño")
    elif num >= 2:
        print(f"El numero {num} no es extraño")
    elif num >= 6:
        print(f"El numero {num} es extraño")
    elif num > 20:
        print(f"El numero {num} no es extraño")

deteccion_num_extraño(numero)
    
    