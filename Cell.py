class Cell:

    def __init__(self, x, y, is_alive, neighbours=[]):
        self.x = x
        self.y = y
        self.isAlive = is_alive
        self.neighbours = neighbours

    def print(self):
        print(self.x, self.y, self.isAlive)

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
