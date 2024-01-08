archivo_txt_sin_leer = open("Archivos\\texto_de_tomy.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo_txt_sin_leer.read()


#leer linea por linea
#lineas = archivo_txt_sin_leer.readlines()

#leer una sola linea
linea_1 = archivo_txt_sin_leer.readline()

#cerrar el archivo
archivo_txt_sin_leer.close
print(linea_1)