pedir_texto_al_usuario = input("Dame un texto: ")

cantidad_de_palabras = pedir_texto_al_usuario.count(" ") + 1

cuanto_tardaria = cantidad_de_palabras * 1 / 2 

if (cuanto_tardaria >= 60):
    print("para flaco tampoco te pedi un testamento.")


print(f"La cantidad de palabras son: {cantidad_de_palabras}")
print(f"tardarias en decir esa frase {cuanto_tardaria} segundos")