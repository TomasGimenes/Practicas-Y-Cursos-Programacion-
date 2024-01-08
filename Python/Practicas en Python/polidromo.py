palabra = "121"

def dar_vuelta_el_string(p):
    lista = []
    for i in p:
        lista.append(i)
    lista.reverse()
    palabra_al_reves = "".join(lista)
    return palabra_al_reves

def comprobar_si_es_un_plidromo(palabra, palabra_al_reves):
    if palabra_al_reves == palabra:
        print(f"la palabra '{palabra}' es un polidromo")
    else:
        print(f"la palabra '{palabra}' NO es un polidromo")

        
string_dado_vuelta = dar_vuelta_el_string(palabra)
comprobar_si_es_un_plidromo(palabra,string_dado_vuelta)