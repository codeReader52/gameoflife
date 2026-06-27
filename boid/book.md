# 🐦 Building a Boid Simulation in Python

This mini-book walks through a complete boid simulation step by step.
We will use while loops, simple object-oriented programming, and pygame to build a flock that:
- moves like a group,
- reacts to nearby boids,
- avoids the screen edges,
- and is created by clicking the mouse.

The final program in this book is meant to match the current implementation in the project.

---

# 1. 🌍 What is a boid?

A boid is a simple object that behaves a little like a bird or a fish.
It has:
- a position: where it is on the screen,
- a velocity: the direction and speed it is moving,
- an acceleration: a small change that helps it react to forces.

A flock looks interesting because each boid follows a few small rules.

---

# 2. 🔁 Why do we use while loops?

Games and simulations usually run forever until the user quits.
That is why we use while loops.

```python
running = True
while running:
    print("The simulation is running")
```

This loop keeps updating the screen again and again.

In our program we use while loops for:
- the main game loop,
- looping through events,
- looping through all boids,
- spawning several boids when the user clicks.

So the whole simulation is driven by while loops.

---

# 3. 🧱 What is a Boid class?

Instead of storing every boid as separate variables, we make a class.
A class is a blueprint for objects.

```python
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
```

Each boid gets its own:
- position,
- velocity,
- acceleration.

That is the heart of object-oriented programming. `self.max_speed`, `self.max_force` and `self.perception_radius` are other information that the object can access, which are discussed below.

---

# 4. 🧠 The three boid rules

The classic boid rules are:
- separation: avoid getting too close to neighbors,
- alignment: move in a similar direction to nearby boids,
- cohesion: move toward the center of nearby boids.

These three rules create flock-like motion.

## 4.1 Separation

Separation makes a boid move away from nearby boids.
This prevents crowding.

```python
def separation(self, boids):
    steer = [0.0, 0.0]
    count = 0
    index = 0
```

Here is what each line means:
- `def separation(self, boids):` starts a method called `separation` that belongs to each boid. It receives the full list of boids as input.
- `steer = [0.0, 0.0]` creates a small steering force for this boid. It will be changed little by little as the boid checks its neighbors.
- `count = 0` starts a counter that will record how many nearby boids are close enough to matter.
- `index = 0` begins a while-loop counter so we can check each boid in the list one by one.

The next part of the code is the loop that examines neighbors:

```python
while index < len(boids):
    other = boids[index]
    if other is not self:
        distance = math.hypot(
            other.position[0] - self.position[0],
            other.position[1] - self.position[1],
        )
```

- `while index < len(boids):` keeps checking boids until every item in the list has been looked at.
- `other = boids[index]` picks one boid from the list.
- `if other is not self:` makes sure we do not compare the boid with itself.
- `distance = math.hypot(...)` calculates how far away that other boid is. The `hypot` function gives the straight-line distance between two points.

Then we decide whether that distance is small enough to matter:

```python
if 0 < distance < self.perception_radius:
    away = [
        self.position[0] - other.position[0],
        self.position[1] - other.position[1],
    ]
```

- `if 0 < distance < self.perception_radius:` means: only react if the boid is close enough, but not exactly on top of the current boid.
- `away = [...]` creates a vector pointing away from the neighbor.

Finally, we add that push to the steering force:

```python
if distance > 0:
    away[0] /= distance
    away[1] /= distance
steer[0] += away[0]
steer[1] += away[1]
count += 1
```

- `away[0] /= distance` and `away[1] /= distance` normalize the direction so the push has a consistent strength.
- `steer[0] += away[0]` and `steer[1] += away[1]` add the push into the total steering force.
- `count += 1` remembers that one nearby boid was found.

At the end of the function, the average steering value is calculated:

```python
if count > 0:
    steer[0] /= count
    steer[1] /= count
    steer = self.limit(steer, self.max_speed)
    steer[0] -= self.velocity[0]
    steer[1] -= self.velocity[1]
    steer = self.limit(steer, self.max_force)
```

- `if count > 0:` only averages the steering force if at least one nearby boid was found.
- `steer[0] /= count` and `steer[1] /= count` turn the total push into an average push.
- `self.limit(steer, self.max_speed)` prevents the steering force from becoming too large.
- `steer[0] -= self.velocity[0]` and `steer[1] -= self.velocity[1]` make the steering act like a change to the current motion.
- `self.limit(steer, self.max_force)` makes sure the correction stays small and smooth.

## 4.2 Alignment

Alignment makes a boid match the direction of nearby boids.
This helps the flock move together.

```python
def alignment(self, boids):
    steer = [0.0, 0.0]
    count = 0
    index = 0
```

This starts the same way as separation, but it is used for direction instead of distance.

The main loop is:

```python
while index < len(boids):
    other = boids[index]
    if other is not self:
        distance = math.hypot(
            other.position[0] - self.position[0],
            other.position[1] - self.position[1],
        )
```

This checks the same kind of information as before, but now the goal is to read the neighbor's velocity.

```python
if 0 < distance < self.perception_radius:
    steer[0] += other.velocity[0]
    steer[1] += other.velocity[1]
    count += 1
```

- `steer[0] += other.velocity[0]` and `steer[1] += other.velocity[1]` gather the motion directions of nearby boids.
- `count += 1` counts how many neighbors influenced the result.

Then the average is computed and turned into a steering correction:

```python
if count > 0:
    steer[0] /= count
    steer[1] /= count
    steer = self.limit(steer, self.max_speed)
    steer[0] -= self.velocity[0]
    steer[1] -= self.velocity[1]
    steer = self.limit(steer, self.max_force)
```

This makes the boid gradually turn to match the motion of its neighbors.

## 4.3 Cohesion

Cohesion makes a boid move toward the average position of nearby boids.
This makes the flock stay together.

```python
def cohesion(self, boids):
    steer = [0.0, 0.0]
    count = 0
    index = 0
```

This starts like the other two methods, but it uses the positions of nearby boids instead of their distances or velocities.

The loop collects their positions:

```python
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
```

- `steer[0] += other.position[0]` and `steer[1] += other.position[1]` add the positions of nearby boids together.
- `count += 1` counts how many neighbors are close enough to influence the flock.

Then the average position is computed and used to guide the boid:

```python
if count > 0:
    steer[0] /= count
    steer[1] /= count
    steer[0] -= self.position[0]
    steer[1] -= self.position[1]
    steer = self.limit(steer, self.max_speed)
    steer[0] -= self.velocity[0]
    steer[1] -= self.velocity[1]
    steer = self.limit(steer, self.max_force)
```

This makes the boid move toward the center of the flock instead of wandering away.

---

# 5. ⚡ Speed and minimum speed

A boid should not become frozen.
If it gets too slow, it stops looking alive.

That is why we include a minimum speed check.

```python
def enforce_min_speed(self):
    speed = math.hypot(self.velocity[0], self.velocity[1])
    min_speed = 2
    if speed < min_speed and speed > 0:
        scale = min_speed / speed
        self.velocity[0] *= scale
        self.velocity[1] *= scale
```

Here is a detailed explanation of each line:
- `def enforce_min_speed(self):` defines a helper method that belongs to a boid object.
- `speed = math.hypot(self.velocity[0], self.velocity[1])` calculates the boid's current speed using the velocity values. The `hypot` function finds the length of the velocity vector.
- `min_speed = 2` sets the smallest allowed speed.
- `if speed < min_speed and speed > 0:` checks whether the boid is slower than the minimum, but not zero. This avoids dividing by zero.
- `scale = min_speed / speed` computes how much we need to increase the velocity so the boid reaches the minimum speed.
- `self.velocity[0] *= scale` multiplies the x component by the scale factor.
- `self.velocity[1] *= scale` multiplies the y component by the same scale factor.

This keeps the boid moving even when the steering forces get small.
It makes the simulation feel more lively and prevents boids from drifting too slowly.

---

# 6. 🧱 Wall repulsion

The boids should not simply disappear off the edge of the screen.
Instead, we create a gentle repulsive force near the walls.

```python
wall_force = [0.0, 0.0]
wall_margin = 80
```

Here is what each line does:
- `wall_force = [0.0, 0.0]` creates a two-part force vector. The first value pushes horizontally, and the second pushes vertically.
- `wall_margin = 80` defines how close a boid must get to the edge before the wall force starts to matter.

The next part of the code uses that force when the boid is near the left or right border:

```python
if self.position[0] < wall_margin:
    wall_force[0] += (wall_margin - self.position[0]) / wall_margin
elif self.position[0] > WIDTH - wall_margin:
    wall_force[0] -= (self.position[0] - (WIDTH - wall_margin)) / wall_margin
```

- `if self.position[0] < wall_margin:` checks whether the boid is near the left wall.
- `wall_force[0] += (...)` adds a positive x-force to push the boid back toward the center.
- `elif self.position[0] > WIDTH - wall_margin:` checks whether the boid is near the right wall.
- `wall_force[0] -= (...)` adds a negative x-force so the boid is pushed back left.

A similar idea is used for the top and bottom edges:

```python
if self.position[1] < wall_margin:
    wall_force[1] += (wall_margin - self.position[1]) / wall_margin
elif self.position[1] > HEIGHT - wall_margin:
    wall_force[1] -= (self.position[1] - (HEIGHT - wall_margin)) / wall_margin
```

- `if self.position[1] < wall_margin:` checks whether the boid is near the top.
- `wall_force[1] += (...)` pushes it downward.
- `elif self.position[1] > HEIGHT - wall_margin:` checks whether it is near the bottom.
- `wall_force[1] -= (...)` pushes it upward.

Finally, the wall force is added to the boid's other steering forces:

```python
self.apply_force(wall_force)
```

This means the wall is treated like another force in the same way as separation, alignment, and cohesion.
The boid is gently pulled away from the edges instead of being instantly stopped or teleported.

Here is the full code pattern for this section:

```python
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
```

---

# 7. 🖱 Clicking to spawn boids

The user creates new boids by clicking the screen.
Each click spawns 5 boids.

```python
elif event.type == pygame.MOUSEBUTTONDOWN:
    x, y = pygame.mouse.get_pos()
    spawn_count = 0
    while spawn_count < 5:
        boids.append(Boid(x, y))
        spawn_count += 1
```

This is a nice interactive feature because the flock grows where the user clicks.

---

# 8. 🔺 Drawing the boids as triangles

We draw each boid as a small triangle.
The triangle points are calculated from the boid's velocity direction, so the triangle points forward.

```python
def draw(self, screen):
    angle = math.atan2(self.velocity[1], self.velocity[0])
    size = 6
    points = [
        (self.position[0] + math.cos(angle) * size * 2, self.position[1] + math.sin(angle) * size * 2),
        (self.position[0] + math.cos(angle + 2.6) * size, self.position[1] + math.sin(angle + 2.6) * size),
        (self.position[0] + math.cos(angle - 2.6) * size, self.position[1] + math.sin(angle - 2.6) * size),
    ]
    pygame.draw.polygon(screen, (255, 255, 255), points)
```

Here is what each line does:
- `def draw(self, screen):` creates a method that draws the boid onto the pygame screen.
- `angle = math.atan2(self.velocity[1], self.velocity[0])` calculates the direction the boid is facing. The `atan2` function turns velocity into an angle.
- `size = 6` sets the size of the triangle.
- `points = [` starts a list of the three corner points of the triangle.
- The first point is the tip of the triangle. It uses the boid's current direction to place the tip forward.
- The second and third points are the two rear corners. They are offset by a small angle to make the triangle shape.
- `pygame.draw.polygon(screen, (255, 255, 255), points)` draws the triangle using white color on the screen.

This makes the flock much easier to understand visually because each boid clearly shows where it is moving.

---

# 9. 🔄 The full update step

Every frame, each boid:
1. checks nearby boids,
2. calculates separation, alignment, and cohesion,
3. applies a wall force,
4. updates its velocity,
5. moves to a new position,
6. draws itself.

That is why the update method is the most important part of the program.

---

# 10. ✅ Final code

The code below is the complete version of the simulation used in this project.
It includes:
- triangle boids,
- while loops only,
- 5 boids per click,
- separation, alignment, and cohesion,
- minimum speed,
- wall repulsion.

```python
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
```