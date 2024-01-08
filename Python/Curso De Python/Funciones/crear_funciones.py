#crendo una funcion simple con "def"
#def saludar():
#    print("Hola buenas")

#saludar()

#creando funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        print(f"Hola {nombre}, como va genia?")
    elif (sexo == "hombre"):
        print(f"Hola {nombre}, como va genio?")
    
saludar("Manolito", "hombre")

#crea una funcion con contrase
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    c4 = num - 7
    c5 = num - 3
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{chars[c4]}{chars[c5]}{num*2}"
    return contraseña

password = crear_contraseña_random(6)
frase = f"Tu contraseña nueva es: {password}"
print(frase)



    
