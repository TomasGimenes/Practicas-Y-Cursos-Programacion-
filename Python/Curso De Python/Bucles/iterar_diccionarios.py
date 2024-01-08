diccionario = {
    "Nombre": "Tomas",
    "Apellido": "Gimenes",
    "Edad": "18"
}

#muestra solo las llaves
for key in diccionario:
    print(key)

#muestra las llaves y valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")