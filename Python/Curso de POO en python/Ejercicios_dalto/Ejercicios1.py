class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print("Estudiando...")

nombre = input("Dame tu nombre ")
edad = input(f"Dame tu edad ")
grado = input(f"Decime el grado al que vas: ")

estudiate = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiate.nombre} \n
      Edad: {estudiate.edad} \n
      Grado: {estudiate.grado} \n
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiate.estudiar()




