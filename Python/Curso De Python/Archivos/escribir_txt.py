with open("Archivos\\texto_de_tomy.txt","w",encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("asjdajsja re la recontra teclee")
    
    #agregando 2 lineas con writelines
    archivo.writelines([" - Hola mostro\n", " - Soy la segunda linea xd\n"])
    
    #agregando otras 2 lineas
    archivo.writelines([" - La segunda linea me cae mal \n", " - A mi la primera linea me cae mal"])