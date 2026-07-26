class Vector:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def add(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def scale(self, factor):
        return Vector(self.x * factor, self.y * factor)



V1 = Vector(1, 2)
V2 = Vector(6, 7)

v3 = V1.add(V2)
v4 = v3.scale(2)
print(v4.x, v4.y)
