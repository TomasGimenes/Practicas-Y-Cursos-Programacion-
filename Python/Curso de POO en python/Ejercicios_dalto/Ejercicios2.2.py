class Animal:
    def comer(self):
        print("El Animal come")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamanta a su bebe")

class Ave(Animal):
    def volar(self):
        print("El animal vuela")

class Murcielago(Mamifero,Ave):
    pass

