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

    @staticmethod
    def is_end_x(im):
        if 50 > im.right or im.left > 750:
            return True
        else:
            return False

    @staticmethod
    def is_end_y(im):
        if 50 > im.bottom or im.top > 550:
            return True
        else:
            return False

    def draw_tail(self, screen, list):
        self.turn_head_graphics(list)
        for index, rect in enumerate(list):
            x_position = int(rect.x * 25)
            y_position = int(rect.y * 25)
            rect_rec = pygame.Rect(x_position, y_position, 25, 25)
            if index == 0:
                screen.blit(self._snake_head_img, rect_rec)
            else:
                pygame.draw.rect(screen, (183, 111, 122), rect_rec)

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


