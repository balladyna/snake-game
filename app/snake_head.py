import pygame
from pygame.math import Vector2


class SnakeHead:

    def __init__(self, items=()):
        self._l = items
        self._snake_head_img = 0
        # self._snake_head_up_img = pygame.image.load("../assets/snake_head_up.png").convert_alpha()
        # self._snake_head_down_img = pygame.image.load("../assets/snake_head_down.png").convert_alpha()
        # self._snake_head_left_img = pygame.image.load("../assets/snake_head_left.png").convert_alpha()
        # self._snake_head_right_img = pygame.image.load("../assets/snake_head_right.png").convert_alpha()
        self._snake_head_up_img = pygame.image.load("../assets/tail.png").convert_alpha()
        self._snake_head_down_img = pygame.image.load("../assets/tail.png").convert_alpha()
        self._snake_head_left_img = pygame.image.load("../assets/tail.png").convert_alpha()
        self._snake_head_right_img = pygame.image.load("../assets/tail.png").convert_alpha()

    def draw_snake(self, screen, list, other):
        self.turn_head_graphics(list)
        for index, rect in enumerate(list):
            x_position = int(rect.x * 20)
            y_position = int(rect.y * 20)
            snake_segment_rect = pygame.Rect(x_position, y_position, 20, 20)
            if index == 0:
                screen.blit(self._snake_head_img, snake_segment_rect)
            # elif snake_segment_rect.right >= 750 or snake_segment_rect.left <= 50:
            #     self.pause()
            # elif snake_segment_rect.top >= 750 or snake_segment_rect.bottom <= 50:
            #     self.pause()
            else:
                pygame.draw.rect(screen, (183, 111, 122), snake_segment_rect)

    def turn_head_graphics(self, list):
        head = list[1] - list[0]
        if head == Vector2(1, 0):
            self._snake_head_img = self._snake_head_left_img
        elif head == Vector2(-1, 0):
            self._snake_head_img = self._snake_head_right_img
        elif head == Vector2(0, 1):
            self._snake_head_img = self._snake_head_up_img
        elif head == Vector2(0, -1):
            self._snake_head_img = self._snake_head_down_img



