import pygame
from pygame.math import Vector2


class Snake:

    def __init__(self, items=()):
        self._l = items
        self._snake_position = [Vector2(35, 1),
                                Vector2(36, 1),
                                Vector2(37, 1),
                                Vector2(38, 1)
                                ]
        self._head_position = self._snake_position[0]
        self._snake_direction = Vector2(-1, 0)
        self._last_direction = "left"
        self._head_rect = pygame.Rect(self._head_position.x * 20, self._head_position.y * 20, 20, 20)
        self._snake_head_img = pygame.image.load("../assets/head_img.png").convert_alpha()

    def draw(self, board):
        for index, rect in enumerate(self._snake_position):
            x_position = int(rect.x * 20)
            y_position = int(rect.y * 20)
            snake_segment_rect = pygame.Rect(x_position, y_position, 20, 20)
            if index != 0:
                pygame.draw.rect(board, (0, 90, 0), snake_segment_rect)
            # elif snake_segment_rect.right >= 750 or snake_segment_rect.left <= 50:
            #     self.pause()
            # elif snake_segment_rect.top >= 750 or snake_segment_rect.bottom <= 50:
            #     self.pause()
            else:
                self._head_rect = pygame.Rect(x_position, y_position, 20, 20)
                board.blit(self._snake_head_img, self._head_rect)

    def add_new_segment(self):
        snake_tail_copy = self._snake_position
        self._snake_position[-1] = snake_tail_copy[-1]
        snake_tail_copy.insert(len(self._snake_position), snake_tail_copy[-1])
        self._snake_position = snake_tail_copy[:]

    def move(self):
        snake_tail_copy = self._snake_position[:-1]
        snake_tail_copy.insert(0, snake_tail_copy[0] + self._snake_direction)
        self._snake_position = snake_tail_copy[:]
        self._head_position = self._snake_position[0]

    def set_direction_left(self):
        self._snake_direction = Vector2(-1, 0)
        self._last_direction = "left"

    def set_direction_right(self):
        self._snake_direction = Vector2(1, 0)
        self._last_direction = "right"

    def set_direction_up(self):
        self._snake_direction = Vector2(0, -1)
        self._last_direction = "up"

    def set_direction_down(self):
        self._snake_direction = Vector2(0, 1)
        self._last_direction = "down"

    def get_snake_position(self):
        return self._snake_position

    def get_last_direction(self):
        return self._last_direction

    def is_snake_tail_collision(self):
        for segment in self._snake_position[1:]:
            if segment == self._head_position:
                return True

    def is_food_collision(self, food_rect):
        return self._head_rect.colliderect(food_rect)
