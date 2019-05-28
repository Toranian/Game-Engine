from settings import *
import pygame; pygame.init()
import random, time


class Healthbar:

    """Create and control a visual healthbar, but also
    correspond to a player / object class"""

    def __init__(self, max_health, length, height, x=0, y=0):

        # health vars
        self.max_health = max_health
        self.current_health = self.max_health
        self.length = length
        self.height = height
        self.x = x
        self.y = y
        self.colour = RED
        self.health_point = self.length / self.max_health


    def display(self):
        pygame.draw.rect(GAME_DISPLAY, RED,
        [self.x, self.y, self.length, self.height])

    def damage(self, damage):
        # self.damage = damage
        self.current_health -= damage
        self.length -= self.health_point * damage

    def death(self):
        if self.current_health <= 0:
            return True


class Player:

    """Player class"""


    def __init__(self, level, healthbar):

        # Other class variables
        self.level = level
        self.healthbar = healthbar


        # Player variables
        self.size = 40
        self.x = WIDTH / 2 - self.size / 2
        self.y = self.level.floor - self.size
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.speed = 4
        self.x_change = 0
        self.y_change = 0
        # self.texture = pygame.image.load('character.png')
        self.colour = ORANGE




        # Physics variables and level variables
        self.gravity = True
        self.g_speed = 3
        self.floor = self.level.floor
        self.jump_speed = 4
        self.jump_speed_control = self.jump_speed
        self.jump_height = 25
        self.momentum = 0
        self.decrement = self.jump_speed / self.jump_height

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(GAME_DISPLAY, self.colour, self.rect)
        # GAME_DISPLAY.blit(self.texture, (self.x, self.y))

        if self.y > self.level.floor - self.size:
            self.y = self.level.floor - self.size

        self.healthbar.display()

    def move(self):
        # To modify a rect, set the self.rect = (modified rect)
        # self.rect = self.rect.move(self.x_change, self.y_change)
        self.x += self.x_change
        self.y += self.y_change
        self.update()

    def direction(self, x_change, y_change):
        self.x_change = x_change
        self.y_change = y_change

    def stop(self, x=0, y=0):
        self.x_change = 0
        self.y_change = 0

    def fall(self):
        if self.gravity:
            if self.y >= self.level.floor - self.size:
                self.gravity = False
                self.momentum = 0
                self.y_change = 0


            else:
                self.momentum += 0.3
                self.y += self.momentum


    def run(self):
        # self.fall()
        self.update()
        self.move()


class Obstacle:

    def __init__(self, player, width=100, height=20, x=WIDTH/2, y=HEIGHT/2):
        self.player = player
        self.player_rect = self.player.rect
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.colour = BLACK

    def update(self):
        pygame.draw.rect(GAME_DISPLAY, self.colour, self.rect)

    def detection(self):
        if self.rect.colliderect(self.player.rect):
            self.player.stop()

    def run(self):
        self.detection()
        self.update()


class Level:

    def __init__(self, floor, ceiling=None):
        self.floor = HEIGHT - floor
        self.ceiling = ceiling
        self.gravity = 8
        self.floor_rect = pygame.Rect(0, self.floor, WIDTH, HEIGHT - self.floor)
        self.colour = GRASS_GREEN

    def update(self):
        pygame.draw.rect(GAME_DISPLAY, self.colour, self.floor_rect)


class Bullet:

    def __init__(self, player):

        self.player = player

        self.size = 10
        self.colour = DARKGREY
        self.x = self.player.x
        self.y = self.player.y
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.speed = 2

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        pygame.draw.rect(GAME_DISPLAY, self.colour, self.rect)

    def trace(self, target_x, target_y):

        self.get_x = True
        self.get_y = True

        if self.get_x:

            if self.x == target_x:
                self.get_x = False

            if self.x > target_x:
                self.x -= self.speed
            if self.x < target_x:
                self.x += self.speed

        if self.get_y:

            if self.y == target_y:
                self.get_y = False

            if self.y > target_y:
                self.y -= self.speed
            if self.y < target_y:
                self.y += self.speed

        print("current: ", self.x, self.y, "  target:", target_x, target_y)

        if not self.get_x and not self.get_y:
            return

        self.update()



class Camera:

    pass


class Cloud:

    def __init__(self):
        self.x = random.randint(300, 600)
        self.y = random.choice(0, WIDTH + 200)
        self.texture = pygame.image.load

    def update(self):
        pygame.blit()
