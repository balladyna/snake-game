import pygame


class GameBoard:

    def __init__(self, items=()):
        self._l = items
        self._game_title = "Snake"
        self._size_of_square = 20
        self._number_of_squares = 40
        self._board = pygame.display.set_mode(
            (self._number_of_squares * self._size_of_square, self._number_of_squares * self._size_of_square))
        self._snake_icon = pygame.image.load("../assets/snake_icon.png")
        self._background = pygame.image.load("../assets/background_img.png")
        self._game_over_font = pygame.font.SysFont("freesansbold.ttf", 70)
        self._font = pygame.font.SysFont("freesansbold.ttf", 32)
        self._score_value = 0
        self._game_over_x = 10
        self._game_over_y = 10
        self._clock = pygame.time.Clock()

    def display_game_title(self):
        pygame.display.set_caption(self._game_title)

    def display_game_icon(self):
        pygame.display.set_icon(self._snake_icon)

    def draw_background(self):
        self._board.blit(self._background, (0, 0))

    def show_score(self):
        score = self._font.render("Score: {}".format(self._score_value), True, (255, 255, 255))
        self._board.blit(score, (self._game_over_x, self._game_over_y))

    def show_game_over_text(self):
        game_over_text = self._game_over_font.render("GAME OVER", True, (255, 255, 255))
        self._board.blit(game_over_text, (250, 250))

    def rise_score(self):
        self._score_value += 1

    def show_game_over(self):
        pause = True

        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.fill_color()
            self.show_score()
            self.show_game_over_text()
            pygame.display.update()

    def fill_color(self):
        self._board.fill((0, 0, 0))

    def get_board(self):
        return self._board

    def set_clock(self, tick):
        self._clock.tick(tick)
