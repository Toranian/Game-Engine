from objects import *
import pygame


color = Color()          # Ability to use colors without having to type in the RGB codes
control = Control()      # Keyboard controls
FPS = 60               # FPS doesn't matter, the speed and everything changes dynamically!


# Create a window class. You can change pretty much everything about it, but it has a bunch of default values.
window = Window(title="Demo Game", fps=FPS)
formula = Formulas(window)     # Physics formulas. Requires the window class as a parameter


# Set width and height variables to the windows defualt height and width
WIDTH = window.width
HEIGHT = window.height


# Create the player
# !!! The window paramater must be passed. It uses variables from it for calculations!!
player_speed = formula.velocity(150) # Speed can be passed in the object, but it's done here so it's more clear
player = GameObject(size=20, x=center(WIDTH), y=center(HEIGHT), color=color.rand_color(), window=window, speed=player_speed)


# Game loop time!
game_exit = False
while not game_exit:

    # Get all sorts of input from the user. These are called "events"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        
        # Move the player to where the mouse is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            
        
        # Detect if a key is pressed
        if control.key_down(event):

            if control.detect_key(event, "w"):
                # The player "speed" is defined as either "x_change" or "y_change"
                # the player coords are updated accordingly. 
                player.y_change -= player_speed
            
            if control.detect_key(event, "s"):
                player.y_change += player_speed

            if control.detect_key(event, "a"):
                player.x_change -= player_speed

            if control.detect_key(event, "d"):
                player.x_change += player_speed
        
        if control.key_up(event):

            if control.detect_key(event, "w"):
                player.y_change = 0

            if control.detect_key(event, "s"):
                player.y_change = 0
            
            if control.detect_key(event, "a"):
                player.x_change = 0

            if control.detect_key(event, "d"):
                player.x_change = 0

        
        # Update and draw all the objects
        window.update() # Window MUST be run first, or else it will draw over other objects.

        # Run the player object
        player.run() 

        # The move_to function can use velocity, time, or acceleration to get to it's destination!
        try:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player.move_to(mouse_x, mouse_y, time=1)
        except:
            pass

        # Update the displaye
        pygame.display.update()

game_exit()