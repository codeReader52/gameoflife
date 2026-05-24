import pygame

great_depression= [194, 178, 178]
b = [34, 5, 252]
great_money = [98, 252, 3]


class Cell:

    def __init__(self, x, y, is_alive, neighbours=[]):
        self.x = x
        self.y = y
        self.isAlive = is_alive
        self.neighbours = neighbours

    def print(self):
        print(self.x, self.y, self.isAlive)

    def draw(self, screen):
        colour = great_depression
        if self.isAlive:
            colour = b
            
        pygame.draw.rect(screen, colour, pygame.Rect(10*self.x,10*self.y,10,10))
        pygame.draw.rect(screen, great_money, pygame.Rect(10*self.x,10*self.y,10,10),1)
            
    def addNeighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def isUnderPopulated(self):
        index = 0
        noAliveCells = 0
        while index < len(self.neighbours):
            neighbourCell = self.neighbours[index]
            if neighbourCell.isAlive:
                noAliveCells += 1
            index += 1

        if noAliveCells <= 1:
            return True
        else:
            return False

    def canLiveOn(self):
        index = 0
        AliveCells = 0
        while index < len(self.neighbours):
            neighbourCell2 = self.neighbours[index]
            if neighbourCell2.isAlive:
                AliveCells += 1

            index += 1

        if AliveCells == 2 or AliveCells == 3:
            return True
        else:
            return False

    def isOverPopulated(self):
        index = 0
        noAlivecells = 0
        while index < len(self.neighbours):
            cell = self.neighbours[index]
            if cell.isAlive:
                noAlivecells += 1
            index += 1

        if noAlivecells > 3:
            return True
        else:
            return False

    def isRevived(self):
        index = 0
        noAlivecells = 0
        while index < len(self.neighbours):
            cell = self.neighbours[index]
            if cell.isAlive:
                noAlivecells += 1
            index += 1
        if noAlivecells == 3:
            return True
        else:
            return False
