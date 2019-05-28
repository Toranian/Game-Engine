from objects import *

master = Master()
color = Color()
window = Window()

player = GameObject(x=window.width/2-10, y=window.height/2-10, size=20, 
                    color=color.black, window=window)
player_speed = 3
player_gravity = 4
fall = True

game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player.move_to(mouse_x, mouse_y)
        
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

    window.update()

    # Draw the objects here!
    player.run()

    pygame.display.update()
    # CLOCK.tick(60)


pygame.quit()
quit()
