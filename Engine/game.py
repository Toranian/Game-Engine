from objects import *
import random
from controls import *
import pygame


fps = 120
color = Color()
window = Window(fps=fps)
control = Control()
formula = Formulas(window)
width = window.width
height = window.height

# Create the player object
player = GameObject(x=window.width/2-20, y=window.height/2-20, size=20, 
                    color=color.black, window=window, mass=1)


player_speed = formula.velocity(200)


# Create the particle list
particle_list = [ GameObject(size=10, color=color.rand_color(), speed=formula.velocity(400), window=window, x=random.randint(0, width), y=random.randint(0, height)) for i in range(100) ]



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
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.move_to(mouse_x, mouse_y, time=0.3)

    # Window needs to update first
    window.update()

    # Draw the objects here!
    player.run()
    
    # particles
    count = 0
    for particle in particle_list:

        # Uncomment this for the particles to follow each other
        # if count == 0:
        #     particle.move_to(player.x, player.y, time=0.5)
        
        # else:
        #     particle.move_to(particle_list[random.randint(0, count)].x, particle_list[random.randint(0, count)].y, time=0.5)
        # count += 1

        # Make the particles move towards the mouse
        particle.move_to(mouse_x, mouse_y, random.uniform(0, particle.speed+5))


        particle.run()
    
    pygame.display.update()


exit_game()
