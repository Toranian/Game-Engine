from objects import *
import pygame
import random

# class instances
color = Color()
window = Window(fps=60, title="Pong", background_color=color.black)
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
p_speed = formula.velocity(200)

# Ball variables
b_size = 15
b_speeds = [formula.velocity(200), formula.velocity(-200)]

# Scores
scores = [0, 0]

# Create the game objects
ball = GameObject(x=center(WIDTH - center(b_size)), y=center(HEIGHT - center(b_size)), color=color.white, window=window, size=b_size, initial_speed_x=random.choice(b_speeds), initial_speed_y=random.choice(b_speeds), bounds=False)
paddle_left = GameObject(x=p_buffer-p_width, y=center(HEIGHT - p_height), height=p_height, width=p_width, window=window, color=color.white)
paddle_right = GameObject(x=WIDTH-p_buffer, y=center(HEIGHT - p_height), height=p_height, width=p_width, window=window, color=color.white)
paddles = [paddle_left, paddle_right]

# print(pygame.font.get_fonts())

# Game loop time!
game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()

        if control.key_down(event):

            if control.detect_key(event, "w"):
                paddle_left.y_change = -p_speed

            if control.detect_key(event, "s"):
                paddle_left.y_change = p_speed
            
            if control.detect_key(event, "up"):
                paddle_right.y_change = -p_speed
            
            if control.detect_key(event, "down"):
                paddle_right.y_change = p_speed
            
            
        
        if control.key_up(event):

            if control.detect_key(event, "w"):
                paddle_left.y_change = 0
            
            if control.detect_key(event, "s"):
                paddle_left.y_change = 0
            
            if control.detect_key(event, "up"):
                paddle_right.y_change = 0
            
            if control.detect_key(event, "down"):
                paddle_right.y_change = 0

    # Test if the ball will hit the window sides
    if ball.hit_top():
        ball.y_change *= -1
    
    if ball.hit_bottom():
        ball.y_change *= -1
    
    if ball.hit_right():
        ball.stop()
        scores[0] += 1


        # Reset left paddle
        paddle_left.x = p_buffer-p_width
        paddle_left.y = center(HEIGHT - p_height)

        # Reset right paddle
        paddle_right.x = WIDTH-p_buffer
        paddle_right.y = center(HEIGHT - p_height)

        # Move ball to center
        ball.x = center(WIDTH - center(b_size))
        ball.y = center(HEIGHT - center(b_size))
        ball.x_change = random.choice(b_speeds)
        ball.y_change = random.choice(b_speeds)
    
    if ball.hit_left():
        ball.stop()
        scores[1] += 1

        # Reset left paddle
        paddle_left.x = p_buffer-p_width
        paddle_left.y = center(HEIGHT - p_height)

        # Reset right paddle
        paddle_right.x = WIDTH-p_buffer
        paddle_right.y = center(HEIGHT - p_height)

        # Move ball to center
        ball.x = center(WIDTH - center(b_size))
        ball.y = center(HEIGHT - center(b_size))
        ball.x_change = random.choice(b_speeds)
        ball.y_change = random.choice(b_speeds)
    

    window.update()
    ball.run()
    paddle_left.run()
    paddle_right.run()

    # Check if the ball hits the paddle. Increases the speed by 15% each time too!
    if ball.collide(paddle_left):
        ball.x_change *= -1.15
        p_speed = abs(ball.x_change)
    if ball.collide(paddle_right):
        ball.x_change *= -1.15
        p_speed = abs(ball.x_change)

    # If the paddle hits the top, the change is set to zero
    for paddle in paddles:
        if paddle.hit_top():
            paddle.y = 0
        if paddle.hit_bottom():
            paddle.y = HEIGHT - p_height

    # Player One score
    text_to_screen(window, scores[0], 0, 0)

    # Player Two score
    text_to_screen(window, scores[1], WIDTH - 30, 0)


    pygame.display.update()


exit_game()
