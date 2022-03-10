import pygame
import random
from pygame.math import Vector2


class Food:

    def __init__(self, items=()):
        self._l = items
        self._food_position = Vector2(0, 0)
        self._randomize_position()
        self._food_rect = pygame.Rect(self._food_position.x * 20, self._food_position.y * 20, 20, 20)
        self._food_image = pygame.image.load("../assets/food.png").convert_alpha()

    def check_food_position(self, snake_position):
        checking = True
        while checking:
            checking = False
            for vector in snake_position:
                if vector.x == self._food_position.x and vector.y == self._food_position.y:
                    self._randomize_position()
                    checking = True
                    break
                else:
                    continue

    def _randomize_position(self):
        food_x_tmp = random.randint(0, 40 - 1)
        food_y_tmp = random.randint(0, 40 - 1)
        self._food_position = Vector2(food_x_tmp, food_y_tmp)

    def draw(self, board):
        food_x_tmp = self._food_position.x * 20
        food_y_tmp = self._food_position.y * 20
        self._food_rect = pygame.Rect(food_x_tmp, food_y_tmp, 20, 20)
        board.blit(self._food_image, self._food_rect)

    def get_food_rect(self):
        return self._food_rect
