import pygame as pg

def draw_all(screen, *groups):
    for group in groups:
        group.draw(screen)

def update_all(*groups):
    for group in groups:
        group.update()