import random
import pygame as pg
from food import Foods, food_objects
from utilis import names
from utilis import calcular_distancia as c_dist
from utilis import lerp 
class Character:
    def __init__(self,x,y,image):
        self.name = self.random_name()
        self.health = 100 #cantidad de vida
        self.energy = 100 #cantidad de energia
        self.hunger = 0 #nivel de hambre inicial
        self.hunger_umbral = 50 #umbral de hambre para buscar comida
        self.speed = float(50) #velocidad de movimiento
        self.strong = 40 #fuerza de golpes mano a mano
        self.inventory = []
        self.location = (0,0)
        self.x = float(x)
        self.y = float(y)
        self.image = pg.image.load(image)
        self.position = (x,y)
        
    #Acciones
    def eat(self,food):
        self.hunger -= food.nutrition
        
    def move_towards(self,target_x,target_y):
        delta_x = target_x - self.x
        delta_y = target_y - self.y
        t = self.speed / c_dist.calculate_distance(self.x,self.y,target_x,target_y) 
        
        self.x = lerp.lerp(self.x,target_x,t)
        self.y = lerp.lerp(self.y,target_y,t)
        
    
    #Funciones 
    def draw(self,screen):
        screen.blit(self.image,(self.x, self.y))
    
    def random_name(self):
        name = names.names
        r_name = random.choice(name)
        return r_name
    
    def update(self):
        self.hunger += 1
        
        #verifica si el colono tiene hambre
        if self.hunger >= self.hunger_umbral:
            self.find_food() #llama a la funcion para buscar comida

    def find_food(self):
        #encuantra la comida mas cercana en base a su posicion actual
        food_cerca = self.find_cerca_food()
        
        if food_cerca:
            self.move_towards(food_cerca.x,food_cerca.y)
            self.eat(food_cerca)
            
    def find_cerca_food(self):
        closest_food = None
        closest_distance = float('inf')
        
        for food in food_objects:
            distance = c_dist.calculate_distance(self.x,self.y,food.x,food.y)
            if distance < closest_distance:
                closest_distance = distance
                closest_food = food
        return closest_food
    
personajes_objects = []

colono = Character(100,100,"assets\\personajes\\humanos\\humanodesnudo.png")

personajes_objects.append(colono)