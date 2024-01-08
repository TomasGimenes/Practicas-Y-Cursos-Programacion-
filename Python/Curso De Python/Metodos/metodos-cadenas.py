cadena1 = "Hola soy tomi"
cadena2 = "Puto,el,que,lee"

#convierte a MAYUSCULA
mayus = cadena1.upper()

#convierte a minuscula
minus = cadena2.lower()

#convierte la pirera letra a MAYUSCULA
primera_letra_mayus = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("t")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("l")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfa numerico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("a")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("Hola")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("tomi")

#remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("tomi","juan")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena2.split(" ")

print(cadena_separada)
