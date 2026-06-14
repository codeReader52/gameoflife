import pygame
import random
from Circle import Circle

pygame.init()

screen = pygame.display.set_mode((500, 500))

mouse_position = (250, 250)
circle_radius = 5

circles = []
index = 0
while index < 500:
    random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    circle = Circle(random.randint(0, 500), random.randint(0, 500), circle_radius, random_color, screen)
    circles.append(circle)
    index += 1

while True:
    event_list = pygame.event.get()
    index = 0
    while index < len(event_list):
        event = event_list[index]
        if event.type == pygame.QUIT:
            import sys
            sys.exit(0)
        index += 1

    screen.fill((255, 255, 255))
    
    index = 0
    while index < len(circles):
        circles[index].draw()        
        index += 1
    pygame.display.update() 