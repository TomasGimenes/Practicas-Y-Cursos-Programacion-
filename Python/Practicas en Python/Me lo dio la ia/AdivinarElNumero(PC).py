import random
input("Tienes que adivinar el numero que te doy \n (PRECIONA ENTER PARA EMPEZAR)")
numero = random.randint(1,151)
mi_numero = int(input("Dame un numero del 1 al 150: "))
jugando = True
while jugando:
    if mi_numero == numero:
        print(f"Adivinaste el numero era {numero}")
        jugando = False
    
    if mi_numero != numero:
        print("Ese no es el numero")
        if mi_numero < numero:
            mi_numero = int(input("El numero que ingresaste es menor, DAME UNO MAS ALTO: "))
        elif mi_numero > numero:
            mi_numero = int(input("El numero que ingresaste es mayor, DAME UNO MAS BAJO: "))
            