import pygame as pg
from models.constantes import (ANCHO_VENTANA, ALTO_VENTANA, FPS)
from models.player.main_player import Jugador
from models.enemy.enemy import Enemigo

pantalla = pg.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pg.init()
reloj = pg.time.Clock()
imagen_de_fondo = pg.image.load("Pygame/juego_prueba_01/assets/img/background/ice_kingdom.jpeg")
imagen_de_fondo = pg.transform.scale(imagen_de_fondo, (ANCHO_VENTANA, ALTO_VENTANA))


ejecucion = True

finn = Jugador(0,10, frame_rate= 70, speed_walk= 10, speed_run= 20)
rey_helado = Enemigo(0,10, frame_rate=70, speed_walk= 10, speed_run=20)


while ejecucion:
    #print(delta_ms)
    lista_eventos = pg.event.get()
    lista_teclas_presionadas = pg.key.get_pressed()
    
    for event in lista_eventos:
        
        match event.type:
            case pg.KEYDOWN:
                if event.key == pg.K_w:
                    finn.jump()
            case pg.QUIT:
                print("Estoy CERRANDO el juego")
                ejecucion = False
                break
    
    if lista_teclas_presionadas[pg.K_d] and not lista_teclas_presionadas[pg.K_a]:
        finn.walk("Right")
    if lista_teclas_presionadas[pg.K_a] and not lista_teclas_presionadas[pg.K_d]:
        finn.walk("Left")
    if not lista_teclas_presionadas[pg.K_d] and not lista_teclas_presionadas[pg.K_a]:
        finn.stay()
    if lista_teclas_presionadas[pg.K_d] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_a]:
        finn.run("Right")
    if lista_teclas_presionadas[pg.K_a] and lista_teclas_presionadas[pg.K_LSHIFT] and not lista_teclas_presionadas[pg.K_d]:
        finn.run("Left")
        
    if lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        rey_helado.walk("Right")
    if lista_teclas_presionadas[pg.K_LEFT] and not lista_teclas_presionadas[pg.K_RIGHT]:
        rey_helado.walk("Left")
    if not lista_teclas_presionadas[pg.K_RIGHT] and not lista_teclas_presionadas[pg.K_LEFT]:
        rey_helado.stay()
    
      
        
    pantalla.blit(imagen_de_fondo, imagen_de_fondo.get_rect())
    delta_ms= reloj.tick(FPS)
    finn.update(delta_ms)
    finn.draw(pantalla)
    rey_helado.update(delta_ms)
    rey_helado.draw(pantalla)
    pg.display.update()

pg.quit()
                
            