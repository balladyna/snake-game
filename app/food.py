import pygame
import random
from pygame.math import Vector2


class Food:

    def __init__(self, items=()):
        self._l = items
        self._random_x_position = random.randint(0, 40 - 1)
        self._random_y_position = random.randint(0, 40 - 1)
        self._food_position = Vector2(self._random_x_position, self._random_y_position)
        self._food_rect = pygame.Rect(self._food_position.x * 20, self._food_position.y * 20, 20, 20)
        self._food_list = [pygame.image.load("../assets/candy.png").convert_alpha(),
                           pygame.image.load("../assets/candy-cane.png").convert_alpha(),
                           pygame.image.load("../assets/heart_candy.png").convert_alpha(),
                           pygame.image.load("../assets/orange_candy.png").convert_alpha()]

    def get_food_image(self):
        return random.choice(self._food_list)

    def draw_food(self, screen):
        self._food_rect = pygame.Rect(self._food_position.x * 20, self._food_position.y * 20, 20, 20)
        pygame.draw.rect(screen, (255, 255, 200), self._food_rect)

    def randomize(self):
        self._random_x_position = random.randint(0, 40 - 1)
        self._random_y_position = random.randint(0, 40 - 1)
        self._food_position = Vector2(self._random_x_position, self._random_y_position)

    def food_rect(self):
        return self._food_rect

    def food_collision(self, other):
        if self._food_rect.colliderect(other):
            return True

