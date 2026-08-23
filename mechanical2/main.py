import pygame
import math
from datetime import datetime

previous = datetime.now()
SCREEN_SIZE = 800
white = 255, 255, 255
blue = 0, 0, 255
green = 0, 255, 0
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

running = True
while running:
    event_list = pygame.event.get()
    event_index = 0
    while event_index < len(event_list):
        event = event_list[event_index]
        if event.type == pygame.QUIT:
            running = False
        event_index += 1



    screen.fill(white)
    pygame.draw.circle(screen, blue, [400, 400], 400)
    pygame.draw.circle(screen, green, [100, 400], 100)
    pygame.display.update()