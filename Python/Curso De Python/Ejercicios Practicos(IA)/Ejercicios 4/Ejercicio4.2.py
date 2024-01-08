#dale el numero y te dare el factorial del mismo
dame_numero = int(input("Dame un numero: "))

def factorial(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(1,num + 1):
            result *= i
        return result
            
resultado = factorial(dame_numero)
print(resultado)