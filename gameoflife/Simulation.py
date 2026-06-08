from Cell import Cell


def createGridWorld(width, height):
    theWorld = []

    outterIndex = 0
    while outterIndex < width:
        innerIndex = 0
        row = []
        while innerIndex < height:
            row.append(Cell(innerIndex, outterIndex, False, []))
            innerIndex += 1

        theWorld.append(row)
        outterIndex += 1

    return theWorld
