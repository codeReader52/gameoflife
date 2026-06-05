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
cells = createGridWorld(800/ 10, 800 / 10)
indexr = 0

while indexr < len(cells):
    row = cells[indexr]
    indexc = 0
    while indexc <len(row):
        cell = row[indexc]

        if indexr - 1 >= 0 and indexr - 1 < len(cells) and indexc - 1 >= 0 and indexc - 1 < len(row):
            cell.addNeighbour(cells[indexr-1][indexc-1])

        if indexr - 1 >= 0 and indexr - 1 < len(cells) and indexc >= 0 and indexc < len(row):
            cell.addNeighbour(cells[indexr-1][indexc])

        if indexr - 1 >= 0 and indexr - 1 < len(cells) and indexc + 1 >= 0 and indexc + 1 < len(row):
            cell.addNeighbour(cells[indexr-1][indexc+1])

        if indexr >= 0 and indexr < len(cells) and indexc - 1 >= 0 and indexc - 1 < len(row):
            cell.addNeighbour(cells[indexr][indexc-1])

        if indexr >= 0 and indexr < len(cells) and indexc + 1 >= 0 and indexc + 1 < len(row):
            cell.addNeighbour(cells[indexr][indexc+1])
        
        if indexr + 1 >= 0 and indexr + 1 < len(cells) and indexc - 1 >= 0 and indexc - 1 < len(row):
            cell.addNeighbour(cells[indexr+1][indexc-1])

        if indexr + 1 >= 0 and indexr + 1 < len(cells) and indexc >= 0 and indexc < len(row):
            cell.addNeighbour(cells[indexr+1][indexc])

        if indexr + 1 >= 0 and indexr + 1 < len(cells) and indexc + 1 >= 0 and indexc + 1 < len(row):
            cell.addNeighbour(cells[indexr+1][indexc+1])

        indexc += 1

    indexr += 1

startSimulation = False

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

        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                mousepos = pygame.mouse.get_pos()
                col_index = int(mousepos[0] / 10)
                row_index = int(mousepos[1] / 10)

                cells[row_index][col_index].isAlive = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                startSimulation = True
                print("Start simulation!!")
                
        eventi = eventi + 1

    if startSimulation:
        indexr = 0
        while indexr < len(cells):
            indexc = 0
            row = cells[indexr]
            while indexc < len(row):
                cell = cells[indexr][indexc]
                if cell.isAlive:
                    if cell.canLiveOn():
                        pass
                    elif cell.isUnderPopulated():
                        cell.isAlive = False
                    else:
                        cell.isAlive = False
                else:
                    if cell.isRevived():
                        cell.isAlive = True

                indexc += 1
            indexr += 1

    # Drawing graphics
    screen.fill(blue)
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
