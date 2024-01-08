import random

pedir_cant_numeros = int(input("Dame la cantidad de numeros de la clave: "))
pedir_cant_letras = int(input("Dame la cantidad de letras de la clave: "))
pedir_cant_simbolos= int(input("Dame la cantidad de simbolos de la clave: "))

numeros = [1,2,3,4,5,6,7,8,9,0]
letras = "abcdefghijklmnñopqrstuvwxyz"
simbolos = ["!","#","$","%","&","/","="]


def numero_random(cant_letras):
    while (pedir_cant_letras):
        print(random.randrange(1,27))

def letras_random(cant_letras):
    char = list(letras)
    for l in range(cant_letras):
        char[0] = l
        print(char)


letras_random(pedir_cant_letras)
numero_random(pedir_cant_letras)
