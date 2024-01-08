#creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#utilizando keyword arguments
frase_resultante = frase(apellido="Gimenes", adjetivo="Boludo", nombre="Tomas")
print(frase_resultante)

#creando la misma funcion con una parametro opcional y un valor por defecto
def frase_otra(nombre,apellido,adjetivo = "Boludo"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante1 = frase_otra("Tomas", "Gimenes", adjetivo="Inteligente")
print(frase_resultante1)