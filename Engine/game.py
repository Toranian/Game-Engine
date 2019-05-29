from objects import *
import random

master = Master()
color = Color()
window = Window()

player = GameObject(x=window.width/2-10, y=window.height/2-10, size=20, 
                    color=color.black, window=window, speed=3)
player_speed = 3
player_gravity = 4
fall = True

enemy = GameObject(size=10, color=color.orange, window=window, speed=2)
large_mass = GameObject(
    size=100, 
    color=color.green, 
    window=window, speed=0.5,
    x=random.randint(0, window.width),
    y=random.randint(0, window.height)
 )

game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            master.exit_game()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player.move_to(mouse_x, mouse_y, 2)
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                player.y_change = -player_speed

            if event.key == pygame.K_s:
                player.y_change = player_speed
            
            if event.key == pygame.K_a:
                player.x_change = -player_speed

            if event.key == pygame.K_d:
                player.x_change = player_speed
    
        
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_w:
                player.y_change = 0
                
            if event.key == pygame.K_s:
                player.y_change = 0
            
            if event.key == pygame.K_a:
                player.x_change = 0

            if event.key == pygame.K_d:
                fall = True
                player.x_change = 0

    # Window needs to update first
    window.update()

    # Draw the objects here!
    player.run()

    # Enemy 
    enemy.move_to(large_mass.x, large_mass.y, 2)
    enemy.run()

    # Large Mass
    large_mass.move_to(enemy.x, enemy.y, 5)
    large_mass.run()

    pygame.display.update()


master.exit_game()
