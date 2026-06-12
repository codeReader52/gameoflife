import pygame 

pygame.init()

screen =pygame.display.set_mode((800,600))

blue = [34, 5, 252]

running = True
while running:
    ind1=0
    event_list = pygame.event.get()
    while ind1 < len(event_list):
        event = event_list[ind1]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

        ind1 += 1
        

    screen.fill(blue)
    pygame.display.update()