import pygame
import game_board_test
import random
import food_test

pygame.init()
game_board = game_board_test.GameBoard()
food = food_test.Food()

pygame.display.set_caption("Snake")
icon = pygame.image.load("../assets/serpent.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
game_board.board()
game_board.background()

food_list = [pygame.image.load("../assets/candy.png"),
             pygame.image.load("../assets/candy-cane.png"),
             pygame.image.load("../assets/heart_candy.png"),
             pygame.image.load("../assets/orange_candy.png")]

food_X = random.randint(40, 720)
food_Y = random.randint(40, 520)
new_food = random.choice(food_list)

play_game = False
timer = pygame.USEREVENT + 1
start = 0

# running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if play_game:
            if event.type == timer:
                game_board.blit(food.get_food_image(), food_X, food_Y)
        else:
            if event.type == pygame.K_SPACE:
                play_game = True
                start = int(pygame.get_ticks() / 1000)

    if play_game:
        game_board.fill()
        game_board.draw_background()
        game_board.show_score()
        game_board.show_game_over()
        pygame.display.update()
        clock.tick(60)
