import os

directorio = r"C:\Users\Administrator\Desktop"

nombre_base = "Hackeado"

extension = ".txt"

num_creaciones = 45

def crear_archivo_multiples_veces():
    for i in range(1, num_creaciones + 1):
        nombre_archivo = f"{nombre_base}_{i}{extension}"
        
        ruta_archivo = os.path.join(directorio, nombre_archivo)
        
        with open(ruta_archivo, "w") as archivo:
            archivo.write("Fuste hackeado")
        
crear_archivo_multiples_veces()