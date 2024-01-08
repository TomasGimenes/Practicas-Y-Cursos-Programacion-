#dale una palabra y te dira si es capicua
pedir_palabra = input("Dame una palabra y te digo si es capicua: ")
def es_capicua(palabra):
    pedir_palabra.lower()
    palabra_comun = list(pedir_palabra)
    palabra_comun.reverse()
    palabra_al_reves = "".join(palabra_comun)
    if  palabra_al_reves == pedir_palabra:
        print(f"La palabra {pedir_palabra} es capicua")
    else:
        print(f"La palabra {pedir_palabra} no es capicua")
    return palabra_al_reves
    
resultado = es_capicua(pedir_palabra)
print(resultado)