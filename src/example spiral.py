import pygame as pg
import math
pg.init()
screen_width = 1920 
screen_height = 1080
win = pg.display.set_mode((screen_width, screen_height)) 
x = 0 
y = 0 
angle = 0 
radius = 0
win.fill((0, 0, 0))
run = True 
draw = True 
while run: 
    x = radius * math.cos(angle) 
    y = radius * math.sin(angle) 
    if -screen_width / 2 < x < screen_width / 2 and -screen_height / 2 < y < screen_height / 2 and draw: 
        pg.draw.circle(win, (255, 255, 255), (x + screen_width / 2, y + screen_height / 2), 2) 
    else: 
        draw = False 
    pg.display.update() 
    angle += 0.01 
    radius += 0.25 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            run = False