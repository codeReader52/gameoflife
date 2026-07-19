import pygame
 
# Arcane stuff we do to get the windows going
pygame.init()

screen = pygame.display.set_mode((500, 500))

red = [255,0,0]
white = [255,255,255]
blue = [0,0,255]

# Game loop to keep the program from exiting
running = True
while running:
    event_list = pygame.event.get()
    event_index = 0
    while event_index < len(event_list):
        event = event_list[event_index]
        if event.type == pygame.QUIT:
            running = False
        event_index = event_index + 1

    screen.fill(white)
    pygame.draw.circle(screen,red,[250,250], 250)
    pygame.draw.circle(screen,blue,[375,250], 125)
    pygame.display.update()
