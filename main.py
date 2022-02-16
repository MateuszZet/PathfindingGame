import pygame, sys
import Pathfinder

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()

# mouse clicks
LEFT = 1
MIDDLE = 2
RIGHT = 3
SCROLL_UP = 4
SCROLL_DOWN = 5

# game setup
background = pygame.image.load('map.png').convert_alpha()
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

pathfinder = Pathfinder.Pathfinder(matrix, screen, 64, 1, 1, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            pathfinder.create_path()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT:
            pathfinder.return_active_cell()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == SCROLL_UP:
            pathfinder.diagonals = True
            print('Diagonal movement available!')
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == SCROLL_DOWN:
            pathfinder.diagonals = False
            print('Diagonal movement disable1')

    screen.blit(background, (0, 0))
    pathfinder.update()
    pygame.display.update()
    clock.tick(60)
