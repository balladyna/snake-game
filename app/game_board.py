import pygame


class GameBoard:

    def __init__(self, items=()):
        self.l = items
        self._background = pygame.image.load("../assets/grass.png")
        self._board = pygame.display.set_mode((800, 600))
        self._font = pygame.font.SysFont("freesansbold.ttf", 32)
        self._game_over_font = pygame.font.SysFont("freesansbold.ttf", 70)
        self._score_value = 0

    def show_score(self):
        text_X = 10
        text_Y = 10
        score = self._font.render("Score: {}".format(self._score_value), True, (255, 255, 255))
        self._board.blit(score, (text_X, text_Y))

    def show_game_over(self):
        game_over_text = self._game_over_font.render("GAME OVER", True, (255, 255, 255))
        self._board.blit(game_over_text, (250, 250))

    def fill(self):
        self._board.fill((0, 0, 0))

    def blit(self):
        self._board.blit(self._background, (0, 0))

    def score_up(self):
        self._score_value = self._score_value + 1
