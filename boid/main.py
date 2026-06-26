import pygame
from datetime import datetime
import random

a_random_no = random.random()
print(a_random_no)

lastTime = datetime.now()
def hasItBeen(seconds):
    global lastTime
    now = datetime.now()
    if (now - lastTime).total_seconds() > seconds:
        lastTime = now
        return True
    return False

pygame.init()

screen = pygame.display.set_mode((800,600))

blue = [34, 5, 252]
red = [255,0,0]

running = True
elements = []
velocities = []
timestep = 0.01
scale = 200

while running:
    ind1=0
    event_list = pygame.event.get()
    while ind1 < len(event_list):
        event = event_list[ind1]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            if cords in elements:
                print("This is already in the list")
            else:
                i = 0
                while i < 10:
                    elements.append(pygame.mouse.get_pos())
                    velocities.append([int(scale * random.uniform(-1, 1)), int(scale * random.uniform(-1, 1))])
                    i += 1
        ind1 += 1

    if hasItBeen(timestep):
        index = 0
        while index < len(elements):
            center = elements[index]
            velocity = velocities[index]
            center2 = [center[0]+ timestep*velocity[0], center[1]+ timestep*velocity[1]]
            elements[index] = center2
            index += 1

    screen.fill(blue)
    index = 0
    while index < len(elements):
        center = elements[index]
        pygame.draw.circle(screen,red,center,5)

        index += 1
    pygame.display.update()