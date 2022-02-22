import pygame
import math
from pygame.locals import *

class SnakeTail(pygame.sprite.Sprite):

    def __init__(self, items=()):
        pygame.sprite.Sprite.__init__(self)
        self._l = items
        self._snake_tail_x = x
        self._snake_tail_y = y
        self._change_x = 0
        self._change_y = 0
        self._frame = 0
        self._snake_tail = [pygame.image.load("../assets/tail.png").convert_alpha(), pygame.image.load("../assets/tail.png").convert_alpha()
                            ]
        self._angle = 0



