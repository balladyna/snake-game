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
        self._snake_tail = [Vector2(5, 10),
                            Vector2(6, 10),
                            Vector2(7, 10), Vector2(8, 10),
                            Vector2(9, 10), Vector2(10, 10),
                            Vector2(11, 10), Vector2(12, 10)
                            ]
        self._vector_direction = Vector2(1, 0)
        self.tail = []

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

    def check_last_direction(self, key):
        if key[pygame.K_UP]:
            self._vector_direction = Vector2(0, -1)

        elif key[pygame.K_DOWN]:
            self._vector_direction = Vector2(0, 1)

        elif key[pygame.K_RIGHT]:
            self._vector_direction = Vector2(1, 0)

        elif key[pygame.K_LEFT]:
            self._vector_direction = Vector2(-1, 0)

    def draw_tail(self, screen):
        self.turn_head_graphics()
        for index, rect in enumerate(self._snake_tail):
            x_position = int(rect.x * 15)
            y_position = int(rect.y * 15)
            rect_rec = pygame.Rect(x_position, y_position, 15, 15)
            if index == 0:
                screen.blit(self._snake_head_img, rect_rec)
            else:
                pygame.draw.rect(screen, (183, 111, 122), rect_rec)

    def move_tail(self):
        snake_tail_copy = self._snake_tail[:-1]
        snake_tail_copy.insert(0, snake_tail_copy[0] + self._vector_direction)
        self._snake_tail = snake_tail_copy[:]

    def turn_head_graphics(self):
        head = self._snake_tail[1] - self._snake_tail[0]
        if head == Vector2(1, 0):
            self._snake_head_img = self._snake_head_left_img
        elif head == Vector2(-1, 0):
            self._snake_head_img = self._snake_head_right_img
        elif head == Vector2(0, 1):
            self._snake_head_img = self._snake_head_up_img
        elif head == Vector2(0, -1):
            self._snake_head_img = self._snake_head_down_img


