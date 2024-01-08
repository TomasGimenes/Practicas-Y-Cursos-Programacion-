import character as char
import food as fd

class CharacterManager:
    def __init__ (self):
        self.characters = char.personajes_objects
    
    def add_character(self, character):
        self.characters.append(character)
    
    def update(self):
        for character in self.characters:
            character.update()
            
    def draw(self,screen):
        for character in self.characters:
            character.draw(screen)

class FoodManager:
    def __init__ (self):
        self.foods = fd.food_objects
    
    def add_character(self, food):
        self.foods.append(food)
    
    def update(self):
        for food in self.foods:
            food.food_update()
            
    def draw(self,screen):
        for food in self.foods:
            food.food_draw(screen)