import pygame


class Control:
    
    def __init__(self):
        pass

    def key_down(self, event):
        if event.type == pygame.KEYDOWN:
            return True
        else:
            return False

    def key_up(self, event):
        if event.type == pygame.KEYUP:
            return True
        else:
            return False

    def detect_key(self, event, key):  
        if key == "w":
            if event.key == pygame.K_w:
                return True
        if key == "s":
            if event.key == pygame.K_s:
                return True
        if key == "a":
            if event.key == pygame.K_a:
                return True

        if key == "d":
            if event.key == pygame.K_d:
                return True
    