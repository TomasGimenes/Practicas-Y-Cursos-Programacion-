#Creando un conjunto listas (Se pueden modificar)
nombres = "Tomas Franco"
apellidos = "Gimenes"
es_Mayor = True
edad = 18

lista = [nombres, apellidos, es_Mayor, edad]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

#Creando un conjunto tuplas (No se pueden modificar)
tuplas = ("Daniel", "Ramirez", False, 16)
print(tuplas[0])
print(tuplas[1])
print(tuplas[2])
print(tuplas[3])

#Creando un conjunto (set)
sets = {"Daniel", "Ramirez", False, 16}
print(sets)

#Creando un diccionario(dict)
diccionario = {
    'nombre' : "Tomas",
    'apellido' : "Gimenes",
    'edad' : 18,
    'aprende_rapido' : True
}
print(diccionario['edad'])