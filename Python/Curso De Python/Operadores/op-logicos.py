#AND
resultado1 = True & True #Devuelve True
resultado2 = False & True #Devuelve False
resultado3 = True & False #Devuelve False
resultado4 = False & False #Devuelve False

#OR
resultado5 = True | True #Devuelve True
resultado6 = False | True #Devuelve True
resultado7 = True | False #Devuelve True
resultado8 = False | False #Devuelve False

#NOT
resultado9 = not True #Devuelve Falso
resultado10 = not False #Devuelve True

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print(resultado9)
print(resultado10)

############################PRACTICA...
a = "Marcelo" == "marcelo"
b = "Daniel" == "daniel"


result = a | b
print(result)