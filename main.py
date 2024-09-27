import pygame
from math import sin, cos, pi 
# pygame setup
heigh = 512
width = 512
pygame.init()
screen = pygame.display.set_mode((heigh, width))
clock = pygame.time.Clock()
running = True

class rotation_matrix:
    def __init__(self, angle):
        self.x = [
            [1, 0, 0],
            [0, cos(angle), -(sin(angle))],
            [0, sin(angle), cos(angle)]]
        self.y = [
            [cos(angle), 0, -(sin(angle))],
            [0, 1, 0],
            [sin(angle), 0, cos(angle)]]
        self.z = [
            [cos(angle), -(sin(angle)), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1]]

class display_matrix:
    def __init__(self, distance, z):
        c = 1/(distance-z)
        self.matrix = [
            [c, 0, 0],
            [0, c, 0],
        ] 

class Box:
    points = []
    def __init__(self, a, center):
        b = a/2
        self.center = center
        self.scale = a
        self.points = [
            [-0.5, -0.5, +0.5],
            [-0.5, -0.5, -0.5],
            [-0.5, +0.5, +0.5],
            [-0.5, +0.5, -0.5],
            [+0.5, -0.5, +0.5],
            [+0.5, -0.5, -0.5],
            [+0.5, +0.5, +0.5],
            [+0.5, +0.5, -0.5],
            ]
    def draw_box(self, screen):
        coordinates_list = []
        for point in self.points:
            new_point = [0, 0, 0]
            dm = display_matrix(2, point[2])
            new_point[0] = point[0]
            new_point[1] = point[1]
            new_point = self.matrix_multipy([new_point], dm.matrix)[0]
            coordinates = (int(self.center[0]+(new_point[0]*self.scale)), int(self.center[1]+(new_point[1]*self.scale)))
            coordinates_list.append(coordinates)
            pygame.draw.circle(screen, "white", coordinates, 1)
        pygame.draw.line(screen, "white",coordinates_list[0], coordinates_list[1], 5)
        pygame.draw.line(screen, "white",coordinates_list[0], coordinates_list[2], 5)
        pygame.draw.line(screen, "white",coordinates_list[0], coordinates_list[4], 5)
        pygame.draw.line(screen, "white",coordinates_list[1], coordinates_list[3], 5)
        pygame.draw.line(screen, "white",coordinates_list[1], coordinates_list[5], 5)
        pygame.draw.line(screen, "white",coordinates_list[2], coordinates_list[3], 5)
        pygame.draw.line(screen, "white",coordinates_list[2], coordinates_list[6], 5)
        pygame.draw.line(screen, "white",coordinates_list[3], coordinates_list[7], 5)
        pygame.draw.line(screen, "white",coordinates_list[4], coordinates_list[5], 5)
        pygame.draw.line(screen, "white",coordinates_list[4], coordinates_list[6], 5)
        pygame.draw.line(screen, "white",coordinates_list[5], coordinates_list[7], 5)
        pygame.draw.line(screen, "white",coordinates_list[6], coordinates_list[7], 5)
        
    def rotate(self, angle, axis):
        rotation_m = rotation_matrix(angle) 
        if axis == "x":
            rotation_m = rotation_m.x
        elif axis == "y":
            rotation_m = rotation_m.y
        elif axis == "z":
            rotation_m = rotation_m.z
        self.points = self.matrix_multipy(self.points, rotation_m)
        
    def matrix_multipy(self, points, matrix):
        new_points = []
        for p in range(len(points)):
            point = points[p].copy()
            new_points.append([])
            for i, m in enumerate(matrix):
                new_points[p].append(0) 
                for j, n in enumerate(m):
                    new_points[p][i] += n*point[j]  
        return new_points

    def __str__(self):
        return str(self.points) 

box = Box(300, [256, 256, 256])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    box.rotate(0.03, "x")
    box.rotate(0.015, "y")
    box.rotate(-0.005, "z")
    box.draw_box(screen)
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
