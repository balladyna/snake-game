import pygame


class SnakeHead:

    def __init__(self, items=()):
        self._l = items
        self._snake_head_x = 400
        self._snake_head_y = 300
        self._snake_head_img = pygame.image.load("../assets/snake_head.png").convert_alpha()
        self._snake_head_rect = self._snake_head_img.get_rect(midbottom=(self._snake_head_x, self._snake_head_y))
        self._angle = 0
        self._last_direction = "up"

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

    def move(self):
        if self._last_direction == "up":
            self._snake_head_rect.top -= 3
        elif self._last_direction == "down":
            self._snake_head_rect.top += 3
        elif self._last_direction == "left":
            self._snake_head_rect.left -= 3
        elif self._last_direction == "right":
            self._snake_head_rect.right += 3

    def check_last_direction(self, key):
        if key[pygame.K_UP] and self._last_direction != "up":
            if self._last_direction == "down":
                self._angle = 180
            elif self._last_direction == "right":
                self._angle = 90
            elif self._last_direction == "left":
                self._angle = -90
            self._last_direction = "up"

        elif key[pygame.K_DOWN] and self._last_direction != "down":
            if self._last_direction == "up":
                self._angle = 180
            elif self._last_direction == "left":
                self._angle = 90
            elif self._last_direction == "right":
                self._angle = -90
            self._last_direction = "down"

        elif key[pygame.K_RIGHT] and self._last_direction != "right":
            if self._last_direction == "left":
                self._angle = 180
            elif self._last_direction == "down":
                self._angle = 90
            elif self._last_direction == "up":
                self._angle = -90
            self._last_direction = "right"

        elif key[pygame.K_LEFT] and self._last_direction != "left":
            if self._last_direction == "right":
                self._angle = 180
            elif self._last_direction == "up":
                self._angle = 90
            elif self._last_direction == "down":
                self._angle = -90
            self._last_direction = "left"

        self._snake_head_img = pygame.transform.rotate(self._snake_head_img, self._angle)
        self._angle = 0

    def get_snake_head_img(self):
        return self._snake_head_img

    def get_snake_head_rect(self):
        return self._snake_head_rect
