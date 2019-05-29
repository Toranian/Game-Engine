from objects import *
from controls import *
import time
import pygame

# Vital Objects and variables
width = 1024
height = 768
FPS = 60

control = Control()

# Create the window object
window = Window(title="Epic Game", height=height, width=width, fps=FPS)

# Create the player object
player = GameObject(x=center_object(width), y=center_object(height), color=Color().orange, window=window)

# Game Loop variable
game_exit = False

# Main loop
while not game_exit:

    # Take in user created "events"
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            exit_game()

        if control.key_down(event):
            if control.detect_key(event, "w"):
                print("Hit!")

    ## Objects need to be updated here
    
    # Window needs to update first
    window.update()

    # Now all other objects can be run
    player.run()

    # Update the Pygame display
    pygame.display.update()


exit_game()
