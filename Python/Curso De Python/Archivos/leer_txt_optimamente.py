#abrimos el archivo con with open
with open("Archivos\\texto_de_tomy.txt",encoding="UTF-8") as archivo:
    #leemos el archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
#no es necesario cerrarlo al usar with open