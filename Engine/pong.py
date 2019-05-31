from objects import *
import pygame
import random


# class instances
color = Color()
window = Window(fps=120, title="Pong", background_color=color.black)
control = Control()
formula = Formulas(window)

# Constants
WIDTH = window.width
HEIGHT = window.height
FPS = window.fps

# Paddle variables
p_buffer = 50
p_width = 20
p_height = 150

# Ball variables
b_size = 15

# Create the game objects
ball = GameObject(x=center(WIDTH - center(b_size)), y=center(HEIGHT - center(b_size)), color=color.white, window=window, size=b_size, initial_speed_x=formula.velocity(random.randint(100, 200)))
paddle_left = GameObject(x=p_buffer-p_width, y=center(HEIGHT - center(p_height)), height=p_height, width=p_width, window=window, color=color.white)
paddle_right = GameObject(x=WIDTH-p_buffer, y=center(HEIGHT - center(p_height)), height=p_height, width=p_width, window=window, color=color.white)

print(paddle_right.x)

# Game loop time!
game_exit = False

while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
    
    window.update()
    ball.run()
    paddle_left.run()
    paddle_right.run()

    pygame.display.update()

exit_game()
