import re

#la cadena en la que se buscaran los patrones
text = "La fecha es 23/06/2021 y el telefono es +1-555-555-5555"

#el patron a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

#El texto con el que se remplazara el patron
remplacement = "Fecha oculta"

#reeplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(pattern, remplacement, text)

#imprimir el resultado
print("Texto modificado:",new_text)