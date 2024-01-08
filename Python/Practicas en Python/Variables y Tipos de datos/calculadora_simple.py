def calculadora_s():
    preguntar = input("¿Quieres restar,sumar,multiplicar o dividir?: ")
    preguntar.upper()
    
    #Esto suma numeros
    if preguntar == "sumar":
        while True:
            a = input("Dame el numero 1: ")
            b = input("Dame el numero 2: ")
            try:
                resultado = int(a) + int(b)
            except:
                print("Te pedi un numero bobo")
            else:
                break
        return resultado
    #esto resta numeros
    elif preguntar == "restar":
        while True:
            a = input("Dame el numero 1: ")
            b = input("Dame el numero 2: ")
            try:
                resultado = int(a) - int(b)
            except:
                print("Te pedi un numero bobo")
            else:
                break
        return resultado
    #esto multiplica numeros
    elif preguntar == "multiplicar":
        while True:
            a = input("Dame el numero 1: ")
            b = input("Dame el numero 2: ")
            try:
                resultado = int(a) * int(b)
            except:
                print("Te pedi un numero bobo")
            else:
                break
        return resultado
    #esto divide numeros
    elif preguntar == "dividir":
        while True:
            a = input("Dame el numero 1: ")
            b = input("Dame el numero 2: ")
            try:
                resultado = int(a) / int(b)
            except:
                print("Te pedi un numero bobo")
            else:
                break
        return resultado
    
print(calculadora_s())
    