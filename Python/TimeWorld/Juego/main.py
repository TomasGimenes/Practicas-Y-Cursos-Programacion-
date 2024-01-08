import pygame as pg
import config as cfg
import objects_manager as o_manager
from character import Character
import sys


def main():
    pg.init()
    
    pg.display.set_caption("TimeWorld")
    reloj1 = pg.time.Clock()
    last_time = pg.time.get_ticks()
    runing = True
    fullscreen = False
    ventana = pg.display.set_mode([cfg.v_ancho,cfg.v_alto],pg.FULLSCREEN if fullscreen else 0)
    
    
    c_manager = o_manager.CharacterManager()
    f_manager = o_manager.FoodManager()
    
    while runing: #Loop Principal
        current_time = pg.time.get_ticks()
        delta_time = (current_time - last_time) / 1000.0
        last_time = current_time
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                runing = False
            elif event.type == pg.KEYDOWN: #Alternar pantalla completa a ventana
                if event.key == pg.K_F12:
                    fullscreen = not fullscreen
                    if fullscreen:
                        ventana = pg.display.set_mode([cfg.p_ancho,cfg.p_alto],pg.FULLSCREEN)
                    else:
                        ventana = pg.display.set_mode([cfg.v_ancho,cfg.v_alto],0)
            
        c_manager.update()
        f_manager.update()
        
        ventana.fill("black")
        
        c_manager.draw(ventana)
        f_manager.draw(ventana)
        
        pg.display.flip()
        reloj1.tick(60) #limitar FPS a 30
    
    pg.quit()
    sys.exit()
    
main()