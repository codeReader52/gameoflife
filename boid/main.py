import pygame 
pygame.init()
screen =pygame.display.set_mode((800,600))
running = True
blue = [34, 5, 252]


while running:
    ind1=0
    ind2 =pygame.event.get()
    while ind1 < len(ind2):
        event = ind2[ind1]
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mouse.get_pos
            print(pygame.mouse.get_pos)

        ind1 += 1
        

    screen.fill(blue)
    pygame.display.update()