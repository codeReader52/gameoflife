import pygame

class Circle:
    def __init__(self, x, y, radius, color, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update_position(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        