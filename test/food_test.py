import pygame
import random


class Food:

    def __init__(self, items=()):
        self._l = items
        self._food_list = [pygame.image.load("../assets/candy.png"),
                           pygame.image.load("../assets/candy-cane.png"),
                           pygame.image.load("../assets/heart_candy.png"),
                           pygame.image.load("../assets/orange_candy.png")]

    def get_food_image(self):
        return random.choice(self._food_list)

