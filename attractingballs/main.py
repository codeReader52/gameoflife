import pygame
import random
pygame.init()

screen = pygame.display.set_mode((500, 500))

mouse_position = (250, 250)
gold = [255, 215, 0]

while True:
    event_list = pygame.event.get()
    index = 0
    while index < len(event_list):
        event = event_list[index]
        if event.type == pygame.QUIT:
            import sys
            sys.exit(1)
        index += 1
    randomCx = random.randint(0, 500)
    randomCy = random.randint(0, 500)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, gold, [randomCx, randomCy], 30)
    pygame.display.update()