import random

for x in range(1):
    num_random = random.randint(1,10000)


    #print(num_random)

adiviar = random.randint(1,101)

while adiviar != num_random:
    adiviar = random.randint(1,10000)
    print(adiviar)
    if adiviar < num_random:
        print("El numero es menor")
        #adiviar = int(input("dame otro numero: "))
    
    elif adiviar > num_random:
        print("El numero es mayor")
        #adiviar = int(input("dame otro numero: "))
else:
    print(f"Haz adivinado el numero y ese era {num_random}")
    
    