import pygame
import os
import random
import pygetwindow as gw
from mss import mss

# Inicializar Pygame
pygame.init()

# Obtener la pantalla principal
screen_info = pygame.display.Info()
screen_width, screen_height = screen_info.current_w, screen_info.current_h

# Crear una pantalla del mismo tamaño que la pantalla principal
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.HWSURFACE | pygame.DOUBLEBUF)

# Obtener el reloj para controlar el tiempo
clock = pygame.time.Clock()

time_collide = 0.0

# Cargar imágenes y obtener el rectángulo del personaje
character_image = pygame.image.load("instagram.png")  # Reemplaza con la ruta de tu imagen
character_rect = character_image.get_rect()

# Lista para almacenar los personajes
characters = [character_rect]

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener la posición del mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for character in characters:
        # Calcular la dirección hacia la que mover el personaje
        direction = (mouse_x - character.centerx, mouse_y - character.centery)

        # Normalizar la dirección para mantener la misma velocidad en todas las direcciones
        length = max(1, (direction[0]**2 + direction[1]**2)**0.5)
        normalized_direction = (direction[0] / length, direction[1] / length)

        # Mover el personaje hacia la dirección del mouse con una velocidad específica
        speed = 5
        character.move_ip(normalized_direction[0] * speed, normalized_direction[1] * speed)

        # Verificar si el personaje toca el mouse
        if time_collide <= 0.0:
            if character.collidepoint(mouse_x, mouse_y):
                time_collide = 50.0
                # Crear un nuevo personaje en el borde aleatorio de la pantalla
                new_character = character_image.get_rect()
                side = random.choice(["top", "bottom", "left", "right"])
                if side == "top":
                    new_character.topleft = (random.randint(0, screen_width - new_character.width), 0)
                elif side == "bottom":
                    new_character.topleft = (random.randint(0, screen_width - new_character.width), screen_height - new_character.height)
                elif side == "left":
                    new_character.topleft = (0, random.randint(0, screen_height - new_character.height))
                elif side == "right":
                    new_character.topleft = (screen_width - new_character.width, random.randint(0, screen_height - new_character.height))
                    
                # Agregar el nuevo personaje a la lista
                characters.append(new_character)
        else:
            time_collide -= 0.1

    # Obtener la captura de pantalla del escritorio
    with mss() as sct:
        screenshot = sct.shot()

    # Limpiar la pantalla con la captura de pantalla
    screen.fill((0, 0, 0))  # Puedes ajustar el color según tus necesidades
    screen.blit(pygame.image.load(screenshot), (0, 0))

    # Dibujar todos los personajes en la nueva posición
    for character in characters:
        screen.blit(character_image, character)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad del juego
    clock.tick(60)

# Salir del juego
pygame.quit()

