import pygame
import math
from datetime import datetime

previous = datetime.now()
SCREEN_SIZE = 800

def has_it_been(milliseconds):
    global previous
    now = datetime.now()

    if (now - previous).total_seconds() * 1000 > milliseconds:
        previous = now
        return True
    else:
        return False

def polar_to_cartesian(radius, theta, translation = [SCREEN_SIZE / 2, SCREEN_SIZE / 2]):
    cat_coord = (radius * math.cos(theta), -1 * radius * math.sin(theta))
    return [cat_coord[0] + translation[0], cat_coord[1] + translation[1]]

# Arcane stuff we do to get the windows going
pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
center = (400, 400)

red = [255,0,0]
white = [255,255,255]
blue = [0,0,255]
black = [0,0,0]
green = [0, 255, 0]

angle = 0
delta_angle = 0.03
blue_circle_radius = 125
blue_circle_centre = [SCREEN_SIZE - 125, SCREEN_SIZE / 2]
point_right_p = [blue_circle_radius, 0]
point_left_p = [blue_circle_radius, math.pi]

trajectory = []

# Game loop to keep the program from exiting
running = True
while running:
    event_list = pygame.event.get()
    event_index = 0
    while event_index < len(event_list):
        event = event_list[event_index]
        if event.type == pygame.QUIT:
            running = False
        event_index = event_index + 1

    # Enable this code to enable moving
    if has_it_been(10):
        angle = angle + delta_angle
        blue_circle_centre = polar_to_cartesian(275, angle)
        point_right_p[1] -= delta_angle
        point_left_p[1] -= delta_angle
        point_right_c = polar_to_cartesian(point_right_p[0], point_right_p[1], blue_circle_centre)
        point_left_c = polar_to_cartesian(point_left_p[0], point_left_p[1], blue_circle_centre)
        
        portion = abs(math.sin(datetime.now().timestamp()))
        centre = [
            portion * point_left_c[0] + (1 - portion) * point_right_c[0],
            portion * point_left_c[1] + (1 - portion) * point_right_c[1]
        ]
        trajectory.append(centre)
   
    screen.fill(white)
    pygame.draw.circle(screen,red, center, 400)
    pygame.draw.circle(screen, blue, blue_circle_centre, 125)
    pygame.draw.line(screen, black, point_right_c, point_left_c, 3)    
    px = (1-0.2/blue_circle_radius) * blue_circle_centre[0] + 0.2/blue_circle_radius * point_right_c[0]
    py = (1-0.2/blue_circle_radius) * blue_circle_centre[1] + 0.2/blue_circle_radius * point_right_c[1]
    pygame.draw.circle(screen, green, [px, py], 8)

    # Instead: iterate through all points in the list trajectory, draw a circle of radius 5 centered at each point in the trajectory list
    index = 0
    while index < len(trajectory):
        recent  = trajectory[index]
        pygame.draw.circle(screen, green, recent, 5)
        index += 1

    # Calculate the coordinate of the point 80% mid way between blue_circle_centre and point_right_c
    # Draw a tiny circle of radius 3px around this point

    pygame.display.update()
