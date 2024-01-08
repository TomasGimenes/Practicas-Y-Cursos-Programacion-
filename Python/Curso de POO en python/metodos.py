class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    #metodos  
    def llamar(self):
        print(f'Estas llamando desde un: {self.modelo}')
    
    def cortar(self):
        print(f"Estas cortando desde un: {self.modelo}")
    ############

celular1 = Celular("Samsung", "S23", "48MP")

celular1.llamar()
celular1.cortar()