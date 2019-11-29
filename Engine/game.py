from objects import *
import random
from controls import *
import pygame


# Important variables and class instances
fps = 120
color = Color()
window = Window(fps=fps, background_color=(24, 24, 24))
control = Control()
formula = Formulas(window)
width = window.width
height = window.height

# Create the player object
player = GameObject(x=window.width/2-20, y=height-20, size=20, color=color.orange, window=window, mass=1)
player_speed = formula.velocity(150)


# Create the particle list
particle_list = [ GameObject(size=10, color=(64, 113, 179), speed=formula.velocity(random.randint(400, 550)), window=window, x=random.randint(0, width), y=random.randint(0, height)) for i in range(100) ]

# Create the object to test collisions
overlap = GameObject(size=100, color=color.orange, window=window)


game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # player.move_to(mouse_x, mouse_y, time=0.5)
            
            if event.button == 3:
                print("right click")
        
        
        
            
    
    # Window needs to update first
    window.update()

    
    # particles
    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.move_to(mouse_x, mouse_y)
    player.run()
    
    pygame.draw.polygon(window.game_display, color.blue, ((player.x-10, player.y-10), (player.x+10, player.y+10), (player.x+25, player.y-25)))
    
    count = 0
    # for particle in particle_list:
    #     # Uncomment this for the particles to follow each other
    #     if count == 0:
    #         particle.move_to(mouse_x, mouse_y)
        
    #     else:
    #         particle.move_to(random.randint(0, width), random.randint(0, height), time=10)
    #     count += 1

    #     # Make the particles move towards the mouse
    #     particle.move_to(mouse_x, mouse_y, random.uniform(0, particle.speed+5))
    #     particle.run()



    
    pygame.display.update()


exit_game()
