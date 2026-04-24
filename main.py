import pygame 
import sys

from Simulation import createGridWorld

def mousePositionToCellCoord(mouseCoord):
    cellCoord = (mouseCoord[0]) - (mouseCoord[0] % 10)
    cellCock = mouseCoord[1] - mouseCoord[1] % 10
    return [int(cellCoord / 10),int(cellCock / 10)]

pygame.init()
screen = pygame.display.set_mode((800,800))

great_depression= [194, 178, 178]
b = [34, 5, 252]
great_money = [98, 252, 3]

index = 0
running = True
cells = createGridWorld(800/ 10, 800 / 10)
cells[0][0].isAlive = True


while running:
    # Handle user events
    eventl = pygame.event.get()
    eventi= 0
    while eventi <len (eventl):
        event = eventl[eventi]
        if event.type == pygame.QUIT:
            running =False    
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            col_index = int(mousepos[0] / 10)
            row_index = int(mousepos[1] / 10)

            cells[row_index][col_index].isAlive = True
            
        eventi = eventi + 1

    # Drawing graphics
    screen.fill(b)
    index = 0
    while index < len(cells):
        tndex = 0
        row =cells[index]
        while tndex <len(row):
            cell = row[tndex]
            cell.draw(screen)
            tndex += 1
        index +=1

    pygame.display.update()
