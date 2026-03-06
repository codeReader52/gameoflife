from Cell import Cell
import pygame

pygame.init()

screen = pygame.display.set_mode([800, 800])

white = [255, 255, 255]
red = [255, 0, 0]

while True:
    event_list = pygame.event.get()
    index = 0
    while index < len(event_list):
        event = event_list[index]
        if event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        if event.type == pygame.QUIT:
            import sys
            sys.exit(0)
        index += 1

    screen.fill(white)
    index = 0
    while index < 800 / 10:
        pygame.draw.rect(screen, red, pygame.Rect(10 * index, 0, 10, 10))
        index += 1

    pygame.display.update()
