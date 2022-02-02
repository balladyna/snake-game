import pygame
from pygame.math import Vector2


class SnakeTail:

    def __init__(self, items=()):
        self._l = items
        self._snake_tail = [Vector2(35, 1),
                            Vector2(36, 1),
                            Vector2(37, 1),
                            Vector2(38, 1)
                            ]
        self._snake_direction = Vector2(-1, 0)
        self._last_direction = "left"
        self._head_x_position = int(self._snake_tail[0].x * 20)
        self._head_y_position = int(self._snake_tail[0].y * 20)
        self._head_rect = pygame.Rect(self._head_x_position, self._head_y_position, 20, 20)
        self._segment = False

    def move_snake(self):
        snake_tail_copy = self._snake_tail[:-1]
        snake_tail_copy.insert(0, snake_tail_copy[0] + self._snake_direction)
        self._snake_tail = snake_tail_copy[:]

    def add_new_segment(self):
        snake_tail_copy = self._snake_tail
        self._snake_tail[-1] = snake_tail_copy[-1]
        snake_tail_copy.insert(len(self._snake_tail), snake_tail_copy[-1])
        self._snake_tail = snake_tail_copy[:]
        self._segment = False

    def change_direction(self, key):
        if key[pygame.K_UP]:
            if self._last_direction != "down":
                self._snake_direction = Vector2(0, -1)
                self._last_direction = "up"

        elif key[pygame.K_DOWN]:
            if self._last_direction != "up":
                self._snake_direction = Vector2(0, 1)
                self._last_direction = "down"

        elif key[pygame.K_RIGHT]:
            if self._last_direction != "left":
                self._snake_direction = Vector2(1, 0)
                self._last_direction = "right"

        elif key[pygame.K_LEFT]:
            if self._last_direction != "right":
                self._snake_direction = Vector2(-1, 0)
                self._last_direction = "left"

    def get_snake_tail(self):
        return self._snake_tail

    def snake_tail_collision(self):
        for segment in self._snake_tail[1:]:
            if segment == self._snake_tail[0]:
                return True

    def get_snake_head(self):
        self._head_x_position = int(self._snake_tail[0].x * 20)
        self._head_y_position = int(self._snake_tail[0].y * 20)
        self._head_rect = pygame.Rect(self._head_x_position, self._head_y_position, 20, 20)
        return self._head_rect


