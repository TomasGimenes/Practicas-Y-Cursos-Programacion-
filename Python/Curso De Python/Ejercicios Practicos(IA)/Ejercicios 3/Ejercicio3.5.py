#dale un numero y te dara todos los pares hasta llegar a ese numero
dame_numero = int(input("Dame un numero: "))
par = []
def numero_par(num):
    for i in range(num):
        if i%2 == 0:
            par.append(i)
    print(par)
    
numero_par(dame_numero)
        