#import modulo_saludar

#desde el el mismo modulo, importamos una funcion que esta dentro del mismo
#from modulo_saludar import saludar

#importando un modulo y asignandole el nombre saludar
import modulo_saludar as saludar

saludo = saludar.saludar("juan")
print(saludo)

