import pygame 
import sys

from Simulation import createGridWorld

def mousePositionToCellCoord(mouseCoord):
    cellCoord = (mouseCoord[0]) - (mouseCoord[0] % 10)
    cellCock = mouseCoord[1] - mouseCoord[1] % 10
    return [int(cellCoord / 10),int(cellCock / 10)]

pygame.init()
screen = pygame.display.set_mode((800,800))

grey = [194, 178, 178]
blue = [34, 5, 252]
green = [98, 252, 3]

index = 0
running = True
cells = createGridWorld(80, 80)

i = 0
while i < len(cells):
    row = cells[i]
    j = 0
    while j < len(row):
        currentcell = cells[i][j]
        if i - 1 >= 0 and i - 1 < len(cells) and j - 1 >= 0 and j - 1 < len(row):
            currentcell.addNeighbour(cells[i-1][j-1])
        if i - 1 >= 0 and i - 1 < len(cells) and j >= 0 and j < len(row):
            currentcell.addNeighbour(cells[i-1][j])
        if i - 1 >= 0 and i - 1 < len(cells) and j + 1 >= 0 and j + 1 < len(row):
            currentcell.addNeighbour(cells[i-1][j+1])
        if i >= 0 and i < len(cells) and j - 1 >= 0 and j - 1 < len(row):
            currentcell.addNeighbour(cells[i][j-1])
        if i >= 0 and i < len(cells) and j + 1 >= 0 and j + 1 < len(row):
            currentcell.addNeighbour(cells[i][j+1])
        if i + 1 >= 0 and i + 1 < len(cells) and j - 1 >= 0 and j - 1 < len(row):
            currentcell.addNeighbour(cells[i+1][j-1])
        if i + 1 >= 0 and i + 1 < len(cells) and j >= 0 and j < len(row):
            currentcell.addNeighbour(cells[i+1][j])
        if i + 1 >= 0 and i + 1 < len(cells) and j + 1 >= 0 and j + 1 < len(row):
            currentcell.addNeighbour(cells[i+1][j+1])

        j += 1
        
    i += 1

startSimulation = False

while running:
    # Handle user events
    eventl = pygame.event.get()
    eventi= 0
    while eventi < len(eventl):
        event = eventl[eventi]
        if event.type == pygame.QUIT:
            running =False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                startSimulation = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            col_index = int(mousepos[0] / 10)
            row_index = int(mousepos[1] / 10)

            if row_index >= len(cells):
                eventi = eventi + 1
                continue
            if col_index >= len(cells[row_index]):
                eventi = eventi + 1
                continue

            cells[row_index][col_index].isAlive = True

        if event.type == pygame.MOUSEMOTION:
            mousepos = event.pos
            col_index = int(mousepos[0] / 10)
            row_index = int(mousepos[1] / 10)

            if row_index >= len(cells):
                eventi = eventi + 1
                continue
            if col_index >= len(cells[row_index]):
                eventi = eventi + 1
                continue
            
            mouse_state = pygame.mouse.get_pressed()
            if mouse_state[0]:
                cells[row_index][col_index].isAlive = True

            if mouse_state[2]:
                cells[row_index][col_index].isAlive = False
            
        eventi = eventi + 1

    if startSimulation:
        index = 0
        while index < len(cells):
            row = cells[index]
            index2 = 0
            while index2 < len(row):
                cell = row[index2]
                if cell.isAlive:
                    if cell.isUnderPopulated():
                        cell.isAlive = False
                    elif cell.isOverPopulated():
                        cell.isAlive = False
                    else:
                        pass    
                else:
                    if cell.isRevived():
                        cell.isAlive = True
                index2 += 1

            index += 1

    # Drawing graphics
    screen.fill(blue)
    index = 0
    while index < len(cells):
        row = cells[index]
        tndex = 0
        while tndex < len(row):
            cell = row[tndex]
            cell.draw(screen)
            tndex += 1
        index +=1

    pygame.display.update()
