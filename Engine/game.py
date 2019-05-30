from objects import *
import random
from controls import *
import pygame


fps = 120
color = Color()
window = Window(fps=fps)
control = Control()
formula = Formulas()
width = window.width
height = window.height

# player = GameObject(x=window.width/2-10, y=window.height/2-10, size=20, 
#                     color=color.black, window=window, speed=3)

player = GameObject(x=window.width/2-20, y=window.height/2-20, size=20, 
                    color=color.black, window=window, speed=3, mass=1)

player_speed = 3
player_gravity = 4

# fps = window.fps

large_mass = GameObject(
    size=100, 
    color=color.green, 
    window=window, speed=0.5,
    # x=random.randint(0, window.width),
    # y=random.randint(0, window.height),
    x = 0,
    y = 0,
    mass=3,
 )

player_speed = create_velocity(fps, 200, 1)
friction = create_velocity(fps, 75, 1)

particle_list = [ GameObject(size=10, color=color.rand_color(), speed=create_velocity(fps, 145, 1), window=window, x=random.randint(0, width), y=random.randint(0, height)) for i in range(1000) ]


print(formula.gravitational_attraction_g(player, large_mass))

game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     player.move_to(mouse_x, mouse_y, velocity=player_speed)
        
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
                # player.x_change -= friction
                player.x_change = 0

    


    mouse_x, mouse_y = pygame.mouse.get_pos()
    player.move_to(mouse_x, mouse_y, velocity=player_speed)

    # Window needs to update first
    window.update()

    # Draw the objects here!
    player.run()
    
    # particles

    count = 0
    for particle in particle_list:
        # if count == 0:
        #     particle.move_to(player.x, player.y)
        
        # else:
        #     particle.move_to(particle_list[random.randint(0, count)].x, particle_list[random.randint(0, count)].y, particle.speed)
        particle.move_to(random.randint(0, 1000), random.randint(0, height), particle.speed)

        count += 1
        particle.run()
    
    pygame.display.update()


exit_game()
