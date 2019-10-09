from objects import *
import random
import pygame

fps = 120
colors = Color()

window = Window(fps=fps, background_color=colors.black)

control = Control()
formula = Formulas(window)
width = window.height
height = window.width
vel = Velocity(window)

ball = GameObject(
    window, 
    initial_speed_x=vel.random_velocity(300, 500),
    initial_speed_y=vel.random_velocity(300, 500),
    color=colors.white,
    x = random.randint(0, width),
    y = random.randint(0, height)
    )

game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

    window.update()
    ball.run()

    if ball.hit_top():
        ball.y_change *= -1
        # ball.x_change *= -1
        ball.y_change = ball.y_change / 2
        ball.x_change = ball.x_change / 2
    
    if ball.hit_bottom():
        ball.y_change *= -1
        # ball.x_change *= -1
        ball.y_change = ball.y_change / 2
        ball.x_change = ball.x_change / 2
    
    if ball.hit_right():
        # ball.y_change *= -1
        ball.x_change *= -1
        ball.y_change = ball.y_change / 2
        ball.x_change = ball.x_change / 2
    
    if ball.hit_left():
        # ball.y_change *= -1
        ball.x_change *= -1
        ball.y_change = ball.y_change / 2
        ball.x_change = ball.x_change / 2
    
    pygame.display.update()