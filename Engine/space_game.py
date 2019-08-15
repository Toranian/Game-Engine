from objects import *
import random
# from controls import *
import pygame


# Important variables and class instances
fps = 120
color = Color()
# window = Window(fps=fps, background_color=color.black)
window = Window(fps=fps, background_image="space.jpeg")

control = Control()
formula = Formulas(window)
width = window.width
height = window.height

# Create the player object
player = GameObject(x=window.width/2-20, y=height-20, size=20, color=color.orange, window=window, mass=1)
player_speed = formula.velocity(250)


particle_speeds = [formula.velocity(-100), formula.velocity(100)]

# Create the particle list
particle_list = [ GameObject(size=20, 
                            # color=color.white,
                            sprite="asteroid.png",  

                            window=window, 
                            x=random.randint(0, width), 
                            y=random.randint(10+player.height, height), 
                            initial_speed_x=random.uniform(particle_speeds[0], particle_speeds[1]),
                            initial_speed_y=random.uniform(particle_speeds[0], particle_speeds[1]),
                            ) 
                for i in range(50) ]

# Create the object to test collisions
overlap = GameObject(size=100, color=color.orange, window=window)

# Bullets
bullet_list = []
bullet_speed = formula.velocity(100)

# Score
score = 0

game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                new_bullet = GameObject(x=player.x, y=player.y, size=10, color=color.red, window=window, bounds=False)
                bullet_list.append(new_bullet)
                new_bullet.move_to(mouse_x, mouse_y)
        
        if control.key_down(event):
            if control.detect_key(event, "w"):
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
            
        
    # Window needs to update first
    window.update()
    # Draw the objects here!
    player.run()
    text_to_screen(window, score, center(width), 10, color=color.white)

    # particles
    for bullet in bullet_list:   
        bullet.run()
    

    particle_count = 0
    for particle in particle_list:
        particle.run()
        
        # Test if the bullet collides with a particle
        for bullet in bullet_list:
            if bullet.collide(particle):
                del particle_list[particle_list.index(particle)]
                del bullet_list[bullet_list.index(bullet)]
                score += 1

    pygame.display.update()

exit_game()
