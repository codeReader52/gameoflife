import pygame
import random
from datetime import datetime
from Circle import Circle

previous = datetime.now()
def has_it_been(milliseconds):
    global previous
    now = datetime.now()

    if (now - previous).total_seconds() * 1000 > milliseconds:
        previous = now
        return True
    else:
        return False

pygame.init()

max_w = 500
max_h = 500
screen = pygame.display.set_mode((max_w, max_h))

circle_radius = 5

circles = []
index = 0
while index < 500:
    random_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    circle = Circle(random.randint(0, max_w), random.randint(0, max_h), circle_radius, random_color, screen)
    circles.append(circle)
    index += 1

start_animation = False

while True:    
    event_list = pygame.event.get()
    index = 0
    while index < len(event_list):
        event = event_list[index]
        if event.type == pygame.QUIT:
            import sys
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("You have started the Game")
            start_animation = True
        index += 1

    # If start_animation is True, then: 
    # Update all the circles so that their y coordinate is increased by 5px every second
    if start_animation == True:
        if has_it_been(50):
            index = 0
            while index < len(circles): 
                circle = circles[index]
                # Make the circle move randomly, but maximally -10 to the left and 10 to the right, -10 up and 10 down
                # circle.update_position(random.randint(-10, 10), random.randint(-10, 10))
                dx, dy = random.randint(-10, 10), random.randint(-10, 10)
                x, y = circle.x, circle.y
                if x + dx < 0:
                    x = abs(x + dx)
                elif x + dx > max_w:
                    x = 2 * max_w - x - dx
                else:
                    x = x + dx

                if y + dy < 0:
                    y = abs(y + dy)
                elif y + dy > max_h:
                    y = 2 * max_h - y - dy
                else:
                    y = y + dy

                circle.x, circle.y = x, y
                index += 1
                
    screen.fill((255, 255, 255))
    
    index = 0
    while index < len(circles):
        circles[index].draw()        
        index += 1
    
    pygame.display.update() 