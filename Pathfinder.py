import pygame, sys
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.core.diagonal_movement import DiagonalMovement


class Pathfinder:

    def __init__(self, matrix, screen, field, start_x, start_y, diagonals):
        self.matrix = matrix
        self.screen = screen
        self.field = field
        self.grid = Grid(matrix=matrix)
        self.select_image = pygame.image.load('icon.png').convert_alpha()

        # pathfinding
        self.start_x = start_x
        self.start_y = start_y
        self.diagonals = diagonals
        self.path = []

    def calculate_tile(self):
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0] // self.field
        y = mouse_pos[1] // self.field
        return [x, y]

    def draw_active_cell(self):
        tile = self.calculate_tile()
        rect = pygame.Rect((tile[0] * self.field, tile[1] * self.field), (self.field, self.field))
        self.screen.blit(self.select_image, rect)

    def return_active_cell(self):
        tile = self.calculate_tile()
        x = tile[0]
        y = tile[1]

        if self.matrix[y][x] == 0:
            print((x, y, 'OBSTACLE'))
        else:
            print((x, y, 'OK'))
            self.start_x = x
            self.start_y = y

    def set_start_point(self):
        x, y = self.calculate_tile()[0], self.calculate_tile()[1]
        return [x, y]

    def create_path(self):

        # start
        start_x, start_y = self.start_x, self.start_y
        start = self.grid.node(start_x, start_y)

        # end
        end_x, end_y = self.calculate_tile()[0], self.calculate_tile()[1]
        end = self.grid.node(end_x, end_y)

        # path
        if self.diagonals :
            finder = AStarFinder(diagonal_movement = DiagonalMovement.always)
        else:
            finder = AStarFinder()

        self.path, _ = finder.find_path(start, end, self.grid)
        self.grid.cleanup()
        print(self.path)

    def draw_path(self):
        if len(self.path) >= 2:
            points = []
            for point in self.path:
                x = (point[0] * self.field) + (self.field // 2)
                y = (point[1] * self.field) + (self.field // 2)
                points.append((x, y))
            pygame.draw.lines(self.screen, '#ff0303', False, points, 5)

    def update(self):
        self.draw_active_cell()
        self.draw_path()
