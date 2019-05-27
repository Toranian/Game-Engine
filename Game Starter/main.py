import pygame
pygame.init()
import random
from settings import *
import game_objects
import time

level = game_objects.Level(140)
healthbar = game_objects.Healthbar(100, 200, 40)
player = game_objects.Player(level, healthbar)
bullet = game_objects.Bullet(player)
# obstacle = game_objects.Obstacle(player, x=500, y=300)

speed = player.speed
game_exit = False
jump = False
create_bullet = False

# wallpaper = pygame.image.load('background.png')

while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # healthbar.damage(1)
            create_bullet = True

        # keydown movement events
        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_ESCAPE:
                game_exit = True

            # Move left
            if event.key == pygame.K_d:
                player.direction(speed, 0)

            # Move right
            if event.key == pygame.K_a:
                player.direction(-speed, 0)

            # Jump
            if event.key == pygame.K_SPACE:
                if player.y >= player.level.floor - player.size:
                    player.jump_speed = player.jump_speed_control
                    jump = True


        if event.type == pygame.KEYUP:

            if event.key == pygame.K_d:
                player.direction(0, 0)
            if event.key == pygame.K_a:
                player.direction(0, 0)



    # GAME_DISPLAY.blit(wallpaper, (0, 0))
    GAME_DISPLAY.fill(DARKGREY)

    if jump:

        player.direction(player.x_change, -player.jump_speed)
        player.move()
        # player.update()
        player.jump_speed -= player.decrement

        if player.jump_speed <= 0:
            player.jump_speed = 0
            player.gravity = True
            jump = False

    if create_bullet:
        bullet.trace(mouse_x, mouse_y)
        bullet.update()
        bullet.trace(player.x, player.y)


    level.update()
    player.move()
    player.fall()
    # obstacle.run()
    # player.run()



    pygame.display.update()
    CLOCK.tick(60)



pygame.quit()
quit()
