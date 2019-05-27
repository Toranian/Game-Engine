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

TILE_SIZE = 16


def RAND_COLOR():
    return random.choice([WHITE, BLACK, RED, GREEN, BLUE, YELLOW])


class Master:

    def __init__(self):
        pass
    
    def center_object(width, height):
        """Takes the width and height of an object and returns the coordinates
        to center it."""
        return ((WIDTH / 2) - width, (HEIGHT / 2) - height)

    def key_test(self, key):
        if key == "w":
            return True
        if key == "a":
            return True
        if key == "s":
            return True
        if key == "d":
            return True


class GameObject:

    def __init__(self, width=10, height=10, initial_speed=0, x=0, y=0, color=BLACK, size=0):
        self.width = width
        self.height = width
        self.initial_speed = initial_speed
        self.x = x
        self.y = y
        self.color = color

        self.x_change = initial_speed
        self.y_change = initial_speed

        if size > 0:
            self.width = size
            self.height = size

    def movement(self):
        self.x += self.x_change
        self.y += self.y_change
    
    def vector(self, x_change, y_change):
        # self.stop()
        self.x_change = x_change
        self.y_change = y_change
        print(self.x_change, self.y_change)
    
    def stop(self):
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(GAME_DISPLAY, self.color, self.rect)

    def run(self):
        self.movement()
        self.update()