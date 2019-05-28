import pygame; import random

# TITLE = "Platformer"
# WIDTH = 1024
# HEIGHT = 768
# FPS = 60
# CLOCK = pygame.time.Clock()

# # Define colors
# WHITE = (240, 240, 240)
# BLACK = (0, 0, 0)
# RED = (159, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# DARKGREY = (40, 40, 40)
# GRASS_GREEN = (76, 139, 58)
# ORANGE = (243, 132, 0)


# GAME_DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

# pygame.display.set_caption(TITLE)

# TILE_SIZE = 16


class Window:

    def __init__(self, width=1024, height=768, fps=60, background_color=(255, 255, 255), title="Game Window"):
        self.width = width
        self.height = height
        self.fps = fps
        self.background_color = background_color
        self.game_display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.title = title
        pygame.display.set_caption(self.title)
    
    def update(self):
        self.game_display.fill(self.background_color)
        self.clock.tick(self.fps)
      

class Color:

    def __init__(self):
        self.white = (240, 240, 240)
        self.black = (0, 0, 0)
        self.red = (159, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.darkgrey = (40, 40, 40)
        self.grassgreen = (76, 139, 58)
        self.orange = (243, 132, 0)
    
    def rand_color(self):
        return random.choice([
        self.white,
        self.black, 
        self.red, 
        self.green,
        self.blue,
        self.yellow,
        self.orange
        ])


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

    def __init__(self, window, width=10, height=10, initial_speed=0, x=0, y=0, color=(0, 0, 0), size=0):
        self.width = width
        self.height = width
        self.initial_speed = initial_speed
        self.x = x
        self.y = y
        self.color = color

        self.x_change = initial_speed
        self.y_change = initial_speed

        self.window = window
        self.fps = self.window.fps

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
        pygame.draw.rect(self.window.game_display, self.color, self.rect)

    def run(self):
        self.movement()
        self.update()
    
    def move_to(self, target_x, target_y):
        if target_x > self.x:
            self.x_change = (target_x - self.x) / self.fps
        if target_x > self.x:
            self.x_change = (self.x - target_x) / self.fps
        
        if target_y < self.y:
            self.y_change = (target_y - self.y) / self.fps
        
        if target_y > self.y:
            self.y_change = (self.y - target_y) / self.fps
        # self.x_change = abs(float(target_x - self.x) / self.fps)
        # self.x_change = abs(float(target_y - self.y) / self.fps)

        # return (self.x_change, self.y_change)
