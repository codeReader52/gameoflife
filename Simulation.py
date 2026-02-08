def simulate(width, height):
    # to build up width * height cells
    x = 0
    y = 0
    while x < width:
        print(x, 0)
        x += 1

    while y < height:
        print(0, y)
        y += 1
        
    


simulate(3, 3)
