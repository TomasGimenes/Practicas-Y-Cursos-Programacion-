frutas = ["Banana", "Mnazana", "Ciruela", "Kiwi", "Pera", "Granada", "Durazno"]
cadena = "Hola tomy"
numeros = [2,8,4,10]

#Evitando que coma una granada con la sentencia continue
for fruta in frutas:
    if fruta == "Granada":
        continue
    print(f"Me voy a comer una {fruta}")

print("----------------------------------")
#Evitar que el bucle siga ejecutandose con break
for fruta in frutas:
    if fruta == "Pera":
        break
    print(f"Me voy a comer una {fruta}")
    
print("---------------------------------")
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)

print("---------------------------------")
#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)