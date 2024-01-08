import re

texto = """Hola maestro, Esta es la cadena 1. ¿como estas mi capitan?
Esta es la linea 2 de texto
Y Esta es la final (linea 3) definitiva pa"""

#haciendo una busqueda simple
resultado2 = re.search("Hola",texto)
resultado1 = re.findall("Esta",texto)

#\d -> busca digitos numericos del texto del 0 - 9
resultado3 = re.findall(r"\d",texto)

#\D -> busca TODO MENOS digitos numericos del texto del 0 - 9
resultado4 = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado5 = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado5 = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios, tabs, saltos de linea
resultado6 = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de linea
resultado6 = re.findall(r"\s",texto)

#\n -> busca todos los saltos en linea
resultado7 = re.findall(r"\n",texto)

#. -> busca TODO MENOS los saltos en linea
resultado8 = re.findall(r".",texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado9 = re.findall(r"\.",texto)

#armando una cadena que busque un nuero, seguido de un punto y un espacio
resultado10 = re.findall(f"\d\.\s",texto)

#^ -> busca el comienzo de una linea
resultado11 = re.findall(r"^",texto)

#$ -> busca el final de una linea
resultado12 = re.findall(r"$",texto)

#{n} -> busca n cantidad de veces el valor de la izquierda
resultado13 = re.findall(r"\d{3}",texto)

#{n,m} -> almenos n, como maximo m
resultado14 = re.findall(r"\d{1,4}",texto)

# | -> busca una cosa o otra
resultado15 = re.findall(r"\d{1,4}|Hola",texto)

print(resultado15)