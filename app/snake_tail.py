import pygame
from pygame.math import Vector2
import math

from pygame.locals import *

class SnakeTail:

    def __init__(self, items=()):
        self._l = items
        self._snake_tail = [Vector2(5, 10),
                            Vector2(6, 10),
                            Vector2(7, 10), Vector2(8, 10),
                            Vector2(9, 10), Vector2(10, 10),
                            Vector2(11, 10), Vector2(12, 10)
                            ]
        self._vector_direction = Vector2(1, 0)
        self._last_direction = "right"

    def move_tail(self):
        snake_tail_copy = self._snake_tail[:-1]
        snake_tail_copy.insert(0, snake_tail_copy[0] + self._vector_direction)
        self._snake_tail = snake_tail_copy[:]

    def check_last_direction(self, key):
        if key[pygame.K_UP]:
            if self._last_direction != "down":
                self._vector_direction = Vector2(0, -1)
                self._last_direction = "up"

        elif key[pygame.K_DOWN]:
            if self._last_direction != "up":
                self._vector_direction = Vector2(0, 1)
                self._last_direction = "down"

        elif key[pygame.K_RIGHT]:
            if self._last_direction != "left":
                self._vector_direction = Vector2(1, 0)
                self._last_direction = "right"

        elif key[pygame.K_LEFT]:
            if self._last_direction != "right":
                self._vector_direction = Vector2(-1, 0)
                self._last_direction = "left"

    def get_snake_tail(self):
        return self._snake_tail
