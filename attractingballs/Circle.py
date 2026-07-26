import pygame

class Circle:
    def __init__(self, x, y, radius, color, screen, max_w, max_h):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen
        self.max_w = max_w 
        self.max_h = max_h        

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update_position(self, delta_x, delta_y):
        x, y = self.x, self.y
        if x + delta_x < 0:
            x = abs(x + delta_x) 
        elif x + delta_x > self.max_w:
            x = 2 * self.max_w - x - delta_x 
        else:
            x = x + delta_x

        if y + delta_y < 0:
            y = abs(y + delta_y) 
        elif y + delta_y > self.max_h:
            y = 2 * self.max_h - y - delta_y
        else:
            y = y + delta_y

        self.x = x
        self.y = y