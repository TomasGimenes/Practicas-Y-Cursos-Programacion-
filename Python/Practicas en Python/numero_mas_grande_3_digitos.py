cadena = "2145222999"
def buscar_numero_mas_grande_de_tres_digitos(cad:str):
    if cad.isnumeric() == True:
        lista = []
        indice_cadena = 0
        for i in range(3):
            lista.append(cad[indice_cadena])
            indice_cadena += 1
        convertir_a_cadena = "".join(lista)
        print(convertir_a_cadena)
    else:
        print("")

def ordenar_cadena(cad:str):
    convertir_lista = list(cad)
    ordenar_numeros = sorted(convertir_lista, reverse=True)
    cadena_ordenada = "".join(ordenar_numeros)
    
    return cadena_ordenada
        
    
cadena_ordenada = ordenar_cadena(cadena)
buscar_numero_mas_grande_de_tres_digitos(cadena_ordenada)