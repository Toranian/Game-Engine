import pygame; import random

TITLE = "Platformer"
WIDTH = 1024
HEIGHT = 768
FPS = 60
CLOCK = pygame.time.Clock()

# Define colors
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
RED = (159, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
DARKGREY = (40, 40, 40)
GRASS_GREEN = (76, 139, 58)
ORANGE = (243, 132, 0)

GAME_DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(TITLE)

def RAND_COLOUR():
    return random.choice([WHITE, BLACK, RED, GREEN, BLUE, YELLOW])

TILE_SIZE = 16
