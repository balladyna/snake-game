import pygame
import game_board
import snake_head

# import snake_tail

pygame.init()

game_board = game_board.GameBoard()
snake_head = snake_head.SnakeHead()
# snake_tail = snake_tail.SnakeTail()


game_board.display_game_title()
game_board.display_game_icon()

running = True

screen_update = pygame.USEREVENT
pygame.time.set_timer(pygame.USEREVENT, 100)

while running:
    key_pressed = pygame.key.get_pressed()

    # draw board and fill with background img
    game_board.fill_color()
    game_board.draw_background()
    game_board.show_score()

    # draw snake head and tail
    snake_head.draw_tail(game_board.get_board())
    snake_head.move_tail()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == screen_update:
            snake_head.check_last_direction(key_pressed)
        # if event.type == pygame.KEYDOWN:
        #     snake_head.check_last_direction(key_pressed)
    # if snake_head.is_end_x(snake_head.get_snake_head_rect()) or snake_head.is_end_y(snake_head.get_snake_head_rect()):
    #     game_board.show_game_over()
    pygame.display.update()
    game_board.get_clock(25)

