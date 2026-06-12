import pygame 

pygame.init()

screen =pygame.display.set_mode((800,600))

blue = [34, 5, 252]
red = [255,0,0]

running = True
elements = []

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
                elements.append(pygame.mouse.get_pos())
                print(elements)
        ind1 += 1

    screen.fill(blue)
    index = 0
    while index < len(elements):
        center = elements[index]
        pygame.draw.circle(screen,red,center,5)
        index += 1
    pygame.display.update()