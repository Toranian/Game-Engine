from objects import *
import random
from controls import *
import pygame


# Important variables and class instances
fps = 120
color = Color()
window = Window(fps=fps, background_color=color.black)
control = Control()
formula = Formulas(window)
width = window.width
height = window.height

# Create the player object
player = GameObject(x=window.width/2-20, y=height-20, size=20, color=color.orange, window=window, mass=1)
player_speed = formula.velocity(150)


# Create the particle list
particle_list = [ GameObject(size=10, color=color.white, speed=formula.velocity(400), window=window, x=random.randint(0, width), y=random.randint(10+player.height, height)) for i in range(100) ]

# Create the object to test collisions
overlap = GameObject(size=100, color=color.orange, window=window)


game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        
        
        if control.key_down(event):

            if control.detect_key(event, "w"):
                # player.vector(0, -player_speed)
                player.y_change -= player_speed
            
            if control.detect_key(event, "s"):
                # player.vector(0, player_speed)
                player.y_change += player_speed

            if control.detect_key(event, "a"):
                # player.vector(-player_speed, 0)
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
            
            

    

    # Make the player follow the mouse
    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # player.move_to(mouse_x, mouse_y, time=0.3)

    # Window needs to update first
    window.update()

    # Draw the objects here!
    player.run()
    # overlap.run()
    # if overlap.collide(player):
    #     print("collision!")
    
    # particles
    count = 0
    for particle in particle_list:
        # pass
        # Uncomment this for the particles to follow each other
        # if count == 0:
        #     particle.move_to(player.x, player.y, time=0.2)
        
        # else:
        #     particle.move_to(particle_list[random.randint(0, count)].x, particle_list[random.randint(0, count)].y, time=0.1)
        # count += 1

        # Make the particles move towards the mouse
        # particle.move_to(mouse_x, mouse_y, random.uniform(0, particle.speed+5))
        particle.run()

        particle.y_change = formula.velocity(random.randint(50, 200))

        if particle.collide(player):
            print("Game over!")
            exit_game()


    
    pygame.display.update()


exit_game()
