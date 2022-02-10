import pygame


class GameBoard:

    def __init__(self, items=()):
        self._l = items
        self._background = pygame.image.load("../assets/grass.png")
        self._board = pygame.display.set_mode((800, 600))
        self._font = pygame.font.SysFont("freesansbold.ttf", 32)
        self._game_over_font = pygame.font.SysFont("freesansbold.ttf", 70)
        self._score_value = 0
        self._clock = pygame.time.Clock()

    def show_score(self):
        text_X = 10
        text_Y = 10
        score = self._font.render("Score: {}".format(self._score_value), True, (255, 255, 255))
        self.blit(score, text_X, text_Y)

    def game_over_info(self):
        game_over_text = self._game_over_font.render("GAME OVER", True, (255, 255, 255))
        self.blit(game_over_text, 250, 250)

    def fill(self):
        self._board.fill((0, 0, 0))

    def blit_background(self):
        self.blit(self._background, 0, 0)

    def score_up(self):
        self._score_value = self._score_value + 1

    def clock(self, tick):
        return self._clock.tick(tick)

    def get_board(self):
        return self._board

    def game_over(self):
        pause = True

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.fill()
            self.show_score()
            self.game_over_info()
            pygame.display.update()

    def blit(self, image, x, y):
        self._board.blit(image, (x, y))

