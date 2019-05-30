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

# class Point:

#     """Get the distance between two points in a 2 dimensional space."""

#     def __init__(self, coords=(0, 0)):
#         self.coords = coords

#     def __eq__(self, other_point):
#         if self.coords == other_point.coords:
#             return True
#         else: 
#             return False
    
#     def add(self, other_point):
#         x = other_point.coords[0] + self.coords[0]
#         y = other_point.coords[1] + self.coords[1]
#         self.coords = (x, y)

#     def __add__(self, other_point):
#         coords = ((self.coords[0] + other_point.coords[0], self.coords[1] + other_point.coords[1]))
#         print(coords)
#         return Point(coords)

#     def __str__(self):
#         return "P({}, {})".format(self.coords[0], self.coords[1])
    
#     def distance_to(self, other_point):
#         second_x = other_point.coords[0]
#         second_y = other_point.coords[1]
#         distance =  ((self.coords[0] - second_x)**2 + (self.coords[1] - second_y)**2 ) ** 0.5
#         return distance

#     @staticmethod
#     def distance_between(x1, y1, x2, y2):
        
#         distance =  ((x1 - x2)**2 + (y1 - y2)**2 ) ** 0.5
#         return distance

class Formulas:

    def __init__(self):
        self.big_g = 6.67e5

    def gravitational_attraction_g(self, object1, object2):
        """Returns the FORCE OF GRAVITY. Takes in the current object and an object to be attracted to."""

        return self.big_g * ((object1.mass * object2.mass) / self.distance_between(object1.x, object1.y, object2.x, object2.y)**2)
    
    def distance_between(self, x1, y1, x2, y2):
        distance =  ((x1 - x2)**2 + (y1 - y2)**2 ) ** 0.5
        return distance

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
        speed=0,
        mass=0,
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

        # Physical Properties
        self.velocity = self.speed / self.fps
        self.mass = mass
        self.acceleration = 0
        self.accelerate = False

        if size > 0:
            self.width = size
            self.height = size

    def movement(self):

        # TODO: Create a way to stop an object when it reaches the 
        # desired location

        # Increases the speed by an amount every second.
        if self.accelerate:
            self.x_change += self.acceleration
            self.y_change += self.acceleration

        self.x += self.x_change
        self.y += self.y_change
    
    def vector(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change
    
    def stop(self):
        self.x_change = 0
        self.y_change = 0

    def update(self):
        # print(self.x, self.y, self.width, self.height)
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.window.game_display, self.color, rect)

    def run(self):
        self.movement()
        self.update()
    
    def move_to(self, target_x, target_y, velocity=0, time=1, acceleration=0):
        """Moves object towards the given target. Time is taken in seconds."""

        self.target_x = target_x
        self.target_y = target_y

        if time > 0:
            speed = self.fps * time
        
        if velocity > 0:
            speed = velocity * self.fps
        
        if acceleration > 0:
            self.accelerate = True
            self.acceleration = acceleration
            speed = self.fps * time

        if self.target_x > self.x and self.target_y > self.y:
            self.x_change = (self.target_x - self.x) / speed
            self.y_change = (self.target_y - self.y) / speed
        
        elif self.target_x < self.x and self.target_y < self.y:
            self.x_change = (self.target_x - self.x) / speed
            self.y_change = (self.target_y - self.y) / speed

        elif self.target_x > self.x and self.target_y < self.y:
            self.x_change = (self.target_x - self.x) / speed
            self.y_change = (self.target_y - self.y) / speed
            return
        
        elif self.target_x < self.x and self.target_y > self.y:
            self.x_change = (self.target_x - self.x) / speed
            self.y_change = (self.target_y - self.y) / speed
            return

    def get_rect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def accelerate(self, x_change, y_change):
        self.x_change -= x_change
        self.y_change -= y_change
        
