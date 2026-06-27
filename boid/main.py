import math
import random
import pygame

WIDTH, HEIGHT = 900, 900
FPS = 60


class Boid:
    def __init__(self, x, y):
        self.position = [x, y]
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(5, 20)
        self.velocity = [math.cos(angle) * speed, math.sin(angle) * speed]
        self.acceleration = [0.0, 0.0]
        self.max_speed = 3.0
        self.max_force = 0.05
        self.perception_radius = 80

    def apply_force(self, force):
        self.acceleration[0] += force[0]
        self.acceleration[1] += force[1]

    def limit(self, value, max_value):
        length = math.hypot(value[0], value[1])
        if length > max_value:
            scale = max_value / length
            value[0] *= scale
            value[1] *= scale
        return value

    def enforce_min_speed(self):
        speed = math.hypot(self.velocity[0], self.velocity[1])
        min_speed = 2
        if speed < min_speed and speed > 0:
            scale = min_speed / speed
            self.velocity[0] *= scale
            self.velocity[1] *= scale

    def separation(self, boids):
        steer = [0.0, 0.0]
        count = 0
        index = 0

        while index < len(boids):
            other = boids[index]
            if other is not self:
                distance = math.hypot(
                    other.position[0] - self.position[0],
                    other.position[1] - self.position[1],
                )

                if 0 < distance < self.perception_radius:
                    away = [
                        self.position[0] - other.position[0],
                        self.position[1] - other.position[1],
                    ]
                    if distance > 0:
                        away[0] /= distance
                        away[1] /= distance
                    steer[0] += away[0]
                    steer[1] += away[1]
                    count += 1
            index += 1

        if count > 0:
            steer[0] /= count
            steer[1] /= count
            steer = self.limit(steer, self.max_speed)
            steer[0] -= self.velocity[0]
            steer[1] -= self.velocity[1]
            steer = self.limit(steer, self.max_force)

        return steer

    def alignment(self, boids):
        steer = [0.0, 0.0]
        count = 0
        index = 0

        while index < len(boids):
            other = boids[index]
            if other is not self:
                distance = math.hypot(
                    other.position[0] - self.position[0],
                    other.position[1] - self.position[1],
                )

                if 0 < distance < self.perception_radius:
                    steer[0] += other.velocity[0]
                    steer[1] += other.velocity[1]
                    count += 1
            index += 1

        if count > 0:
            steer[0] /= count
            steer[1] /= count
            steer = self.limit(steer, self.max_speed)
            steer[0] -= self.velocity[0]
            steer[1] -= self.velocity[1]
            steer = self.limit(steer, self.max_force)

        return steer

    def cohesion(self, boids):
        steer = [0.0, 0.0]
        count = 0
        index = 0

        while index < len(boids):
            other = boids[index]
            if other is not self:
                distance = math.hypot(
                    other.position[0] - self.position[0],
                    other.position[1] - self.position[1],
                )

                if 0 < distance < self.perception_radius:
                    steer[0] += other.position[0]
                    steer[1] += other.position[1]
                    count += 1
            index += 1

        if count > 0:
            steer[0] /= count
            steer[1] /= count
            steer[0] -= self.position[0]
            steer[1] -= self.position[1]
            steer = self.limit(steer, self.max_speed)
            steer[0] -= self.velocity[0]
            steer[1] -= self.velocity[1]
            steer = self.limit(steer, self.max_force)

        return steer

    def update(self, boids):
        sep = self.separation(boids)
        align = self.alignment(boids)
        coh = self.cohesion(boids)

        sep[0] *= 2.5
        sep[1] *= 2.5
        align[0] *= 2.0
        align[1] *= 2.0
        coh[0] *= 0.8
        coh[1] *= 0.8

        self.apply_force(sep)
        self.apply_force(align)
        self.apply_force(coh)

        wall_force = [0.0, 0.0]
        wall_margin = 80

        if self.position[0] < wall_margin:
            wall_force[0] += (wall_margin - self.position[0]) / wall_margin
        elif self.position[0] > WIDTH - wall_margin:
            wall_force[0] -= (self.position[0] - (WIDTH - wall_margin)) / wall_margin

        if self.position[1] < wall_margin:
            wall_force[1] += (wall_margin - self.position[1]) / wall_margin
        elif self.position[1] > HEIGHT - wall_margin:
            wall_force[1] -= (self.position[1] - (HEIGHT - wall_margin)) / wall_margin

        self.apply_force(wall_force)

        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity = self.limit(self.velocity, self.max_speed)
        self.enforce_min_speed()

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        if self.position[0] < 0:
            self.position[0] = 0
        elif self.position[0] > WIDTH:
            self.position[0] = WIDTH

        if self.position[1] < 0:
            self.position[1] = 0
        elif self.position[1] > HEIGHT:
            self.position[1] = HEIGHT

        self.acceleration[0] = 0.0
        self.acceleration[1] = 0.0

    def draw(self, screen):
        angle = math.atan2(self.velocity[1], self.velocity[0])
        size = 6
        points = [
            (self.position[0] + math.cos(angle) * size * 2, self.position[1] + math.sin(angle) * size * 2),
            (self.position[0] + math.cos(angle + 2.6) * size, self.position[1] + math.sin(angle + 2.6) * size),
            (self.position[0] + math.cos(angle - 2.6) * size, self.position[1] + math.sin(angle - 2.6) * size),
        ]
        pygame.draw.polygon(screen, (255, 255, 255), points)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boid Simulation")
clock = pygame.time.Clock()

boids = []

running = True
while running:
    event_list = pygame.event.get()
    index = 0
    while index < len(event_list):
        event = event_list[index]
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            spawn_count = 0
            while spawn_count < 5:
                boids.append(Boid(x, y))
                spawn_count += 1
        index += 1

    screen.fill((10, 20, 40))

    boid_index = 0
    while boid_index < len(boids):
        boid = boids[boid_index]
        boid.update(boids)
        boid.draw(screen)
        boid_index += 1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()