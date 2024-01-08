class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def datos(self):
        print(f'El nombre de la persona es {self.nombre} y su edad es {self.edad}')
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    def grad(self):
        print(f'{self.nombre} es estudiante y va a {self.grado} grado')
        
estudiante = Estudiante("Tomas",18,"septimo")
estudiante.datos()
estudiante.grad()

