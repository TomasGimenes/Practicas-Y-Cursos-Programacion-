def Resta(*num):
    resultado = num[0]
    for numero in num[1:]:
        resultado -= numero
    return resultado

