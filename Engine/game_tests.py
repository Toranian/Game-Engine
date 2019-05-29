from objects import *
from controls import *
import time

width = 1024
height = 768
FPS = 60

window = Window(title="Epic Game", height=height, width=width, fps=FPS)

player = GameObject(x=center_object(width), y=center_object(height), color=Color().orange, window=window)


