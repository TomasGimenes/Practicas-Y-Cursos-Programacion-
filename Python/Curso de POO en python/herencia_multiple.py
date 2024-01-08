class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Estoy hablando un poco")


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"
        
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,nacionalidad,habilidad,trabajo,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.trabajo = trabajo
        self.salario = salario
        self.empresa = empresa
    
    def presentarse(self):
        return f'Hola soy {self.nombre} y {super().mostrar_habilidad()}'

        
tomas = EmpleadoArtista("Tomas",18,"argentino","Tocar Guitarra","Programador",3000,"Google")
print(tomas.presentarse())

instancia = isinstance(tomas,EmpleadoArtista)
herencia = issubclass(EmpleadoArtista, Artista)

