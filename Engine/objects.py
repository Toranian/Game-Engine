import pygame
import random


def center_object(length):
    """Takes the width and height of an object and returns the coordinates
    to center it."""
    return (length / 2) - length


def key_test(event, key):
    if key == "w" and event.key == pygame.K_w:
        return True
    if key == "a":
        return True
    if key == "s":
        return True
    if key == "d":
        return True


def exit_game():
    print("Quitting Game!")
    pygame.quit()
    quit()


def create_velocity(fps, pixels, seconds):
    return pixels / (fps * seconds)


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


class GameObject:

    def __init__(
        self, window, width=10, 
        height=10, initial_speed=0, 
        x=0, y=0, 
        color=(0, 0, 0), size=0,
        speed=0
    ):

        # Takes the window argument for the FPS
        self.window = window
        self.fps = self.window.fps
        
        # Sets the height and width of the object
        self.width = width
        self.height = width
        self.initial_speed = initial_speed
        self.x = x
        self.y = y
        self.color = color
        self.speed = speed

        self.x_change = initial_speed
        self.y_change = initial_speed

        self.velocity = self.speed / self.fps

        if size > 0:
            self.width = size
            self.height = size

    def movement(self):

        # TODO: Create a way to stop an object when it reaches the 
        # desired location

        self.x += self.x_change
        self.y += self.y_change
    
    def vector(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change
    
    def stop(self):
        self.x_change = 0
        self.y_change = 0

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.window.game_display, self.color, self.rect)

    def run(self):
        self.movement()
        self.update()
    
    def move_to(self, target_x, target_y, time):
        """Moves object towards the given target. Time is taken in seconds."""

        self.target_x = target_x
        self.target_y = target_y

        if self.target_x > self.x and self.target_y > self.y:
            self.x_change = (self.target_x - self.x) / (self.fps * time)
            self.y_change = (self.target_y - self.y) / (self.fps * time)
            return
        
        elif self.target_x < self.x and self.target_y < self.y:
            self.x_change = (self.target_x - self.x) / self.fps
            self.y_change = (self.target_y - self.y) / self.fps
            return

        elif self.target_x > self.x and self.target_y < self.y:
            self.x_change = (self.target_x - self.x) / self.fps
            self.y_change = (self.target_y - self.y) / self.fps
            return
        
        elif self.target_x < self.x and self.target_y > self.y:
            self.x_change = (self.target_x - self.x) / self.fps
            self.y_change = (self.target_y - self.y) / self.fps
            return

    def accelerate(self, x_change, y_change):
        self.x_change -= x_change
        self.y_change -= y_change
        
