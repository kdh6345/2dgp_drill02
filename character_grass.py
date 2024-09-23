from pico2d import *
import random
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
center_x = 400  
center_y = 290  
radius = 200  
angle = 0

while (True):
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x+=2
        
        delay(0.001)
    while(x>400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x-=math.cos(45/360*2*math.pi)
        y+=math.sin(45/360*2*math.pi)
        delay(0.001)
        
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x-=math.cos(45/360*2*math.pi)
        y-=math.sin(45/360*2*math.pi)
        delay(0.001)

    while (angle < 360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        
        x = center_x + radius * math.cos(math.radians(angle))
        y = center_y + radius * math.sin(math.radians(angle))
        
        character.draw_now(x, y)
        
        angle += 5  
        delay(0.01)

    x = 0  
    y = 90
    angle = 0  
close_canvas()
