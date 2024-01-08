diccionario = dict(nombre = "Tomas", apellido = "Gimenes")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Tomas", "Capo"]): "XD"}

#creando diccionario con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["Nombre", "Apellido"])

#creando diccionario con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["Nombre", "Apellido"], "no se")

print(diccionario)