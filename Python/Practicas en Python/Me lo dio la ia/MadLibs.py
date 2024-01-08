import random


def pedir_palabra():
    palabras = []
    for i in range(5):
        pedir_palabras = input(f"Dame el adjetivo numero {i+1} : ")
        palabras.append(pedir_palabras)
    return palabras

def tomar_frase_aleatoria():
    palabras = pedir_palabra()
    frases = [
        f"Francisco era muy {palabras[0]} y le gustaba {palabras[1]}, el queria {palabras[2]} pero no lo dejaban entonces un dia {palabras[3]} y {palabras[4]} a su vecino.",
        f"camilo era muy {palabras[0]} pero chupo un {palabras[1]} y se volvio {palabras[2]}, eso no evito que Camilo hiciera {palabras[3]}, por lo que fue a {palabras[4]}.",
        f"Daniela era tremenda {palabras[0]} y en un momento tuvo que {palabras[1]} cuando en su casa habia {palabras[2]} entonces cambio de {palabras[3]} y se fua a su {palabras[4]}"
    ]
    frase = random.choice(frases)
    return frase

resultado = tomar_frase_aleatoria()
print(resultado)

