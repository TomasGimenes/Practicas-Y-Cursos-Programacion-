pedir_nombre = input("Cual es tu nombre: ")
pedir_edad = int(input("Ahora dime tu edad: "))
pedir_altura = input("Por ultimo, dame tu estatura: ")

print(f"Mi nombre es {pedir_nombre}, tengo {pedir_edad} años y mido {pedir_altura} metros de altura")


if pedir_nombre == "Arroz":
    print("Flaco eso no es un nombre")
else:
    print("Tenes un nombre espectacular")