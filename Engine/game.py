from objects import *
import random
from controls import *

color = Color()
window = Window()
control = Control()

# player = GameObject(x=window.width/2-10, y=window.height/2-10, size=20, 
#                     color=color.black, window=window, speed=3)

player = GameObject(x=0, y=window.height/2-10, size=20, 
                    color=color.black, window=window, speed=3)

player_speed = 3
player_gravity = 4

fps = window.fps

enemy = GameObject(size=10, color=color.orange, window=window, speed=2)
large_mass = GameObject(
    size=100, 
    color=color.green, 
    window=window, speed=0.5,
    x=random.randint(0, window.width),
    y=random.randint(0, window.height)
 )

player_speed = create_velocity(fps, 150, 1)

game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game()
        
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     player.move_to(mouse_x, mouse_y, 2)
        
        if control.key_down(event):

            if control.detect_key(event, "w"):
                player.vector(0, -player_speed)
            
            if control.detect_key(event, "s"):
                player.vector(0, player_speed)
            

        # if event.type == pygame.KEYDOWN:
    
        #     if event.key == pygame.K_w:
        #         player.y_change = -player_speed

        #     if event.key == pygame.K_s:
        #         player.y_change = player_speed
            
        #     if event.key == pygame.K_a:
        #         player.x_change = -player_speed

        #     if event.key == pygame.K_d:
        #         player.x_change = player_speed
            
        
        # if event.type == pygame.KEYUP:
            
        #     if event.key == pygame.K_w:
        #         player.y_change = 0
                
        #     if event.key == pygame.K_s:
        #         player.y_change = 0
            
        #     if event.key == pygame.K_a:
        #         player.x_change = 0

        #     if event.key == pygame.K_d:
        #         player.x_change = 0

    # Window needs to update first
    window.update()

    # Draw the objects here!
    player.run()
    player.accelerate(-create_velocity(fps, 10, 1), 0)

    # Enemy 
    # enemy.move_to(player.x, player.y, 2)
    # enemy.run()

    # Large Mass
    # large_mass.move_to(enemy.x, enemy.y, 5)
    # large_mass.run()

    pygame.display.update()


exit_game()
