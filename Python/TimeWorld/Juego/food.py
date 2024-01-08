import pygame as pg

class Foods:
    def __init__(self,tipo,nutrition,state,x,y,image):
        self.tipo = tipo
        self.nutrition = nutrition
        self.state = state
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.position = (x,y)
        
        
    def food_draw(self,screen):
        screen.blit(self.image,(self.x, self.y))
    
    def food_update(self):
        pass


food_objects = []
manzana = Foods("Manzana",50,100,500,500,"assets\\comidas\\manzana.png")
food_objects.append(manzana)

