import pygame
import math
from datetime import datetime

previous = datetime.now()
SCREEN_SIZE = 800
white = 255, 255, 255
blue = 0, 0, 255
red = 255, 0, 0
green = 0, 255, 0
green_circle_radius = 125
green_circle_centre = [SCREEN_SIZE - 125, SCREEN_SIZE / 2]
point_right_p = [green_circle_radius, 0]

angle = 0
delta_angle = 0.03
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

def has_it_been(milliseconds):
    global previous
    now = datetime.now()
    if (now - previous).total_seconds() * 1000 > milliseconds:
        previous = now
        return True
    else:
        return False

def polar_to_cartesian(radius, thetha, translation = [SCREEN_SIZE/ 2, SCREEN_SIZE / 2]):
    cat_coord = (radius * math.cos(thetha), -1 * radius * math.sin(thetha))
    return [cat_coord[0] + translation[0], cat_coord[1] + translation[1]]

running = True
while running:
    event_list = pygame.event.get()
    event_index = 0
    while event_index < len(event_list):
        event = event_list[event_index]
        if event.type == pygame.QUIT:
            running = False
        event_index += 1

    if has_it_been(10):
        angle = angle - delta_angle
        green_circle_centre = polar_to_cartesian(275, angle)
        
    screen.fill(white)
    pygame.draw.circle(screen, blue, [400, 400], 400)
    pygame.draw.circle(screen, green, green_circle_centre, 100)
    
    pygame.draw.circle(screen, red, [green_circle_centre[0], green_circle_centre[1] - 100] , 5)
    pygame.display.update()