import pygame
import random
from datetime import datetime
from Circle import Circle

previous = datetime.now()
def has_it_been(seconds):
    global previous
    now = datetime.now()

    if (now - previous).seconds > seconds:
        previous = now
        return True
    else:
        return False

pygame.init()

screen = pygame.display.set_mode((500, 500))

circle_radius = 5

circles = []
index = 0
while index < 500:
    random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    circle = Circle(random.randint(0, 500), random.randint(0, 500), circle_radius, random_color, screen)
    circles.append(circle)
    index += 1

start_animation = False

while True:    
    event_list = pygame.event.get()
    index = 0
    while index < len(event_list):
        event = event_list[index]
        if event.type == pygame.QUIT:
            import sys
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("You have started the Game")
            start_animation = True
        index += 1

    
    benry = 0

    # If start_animation is True, then: 
    # Update all the circles so that their y coordinate is increased by 5px every second
    if start_animation == True:
        if has_it_been(1):
            while benry < len(circles): 
                tenry = circles[index]
                tenry.y += 5
                benry += 1



    screen.fill((255, 255, 255))
    
    index = 0
    while index < len(circles):
        circles[index].draw()        
        index += 1
    
    pygame.display.update() 