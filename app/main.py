import pygame
import game_board
import snake_head

pygame.init()

game_board = game_board.GameBoard()
snake_head = snake_head.SnakeHead()

game_board.display_game_title()
game_board.display_game_icon()

running = True

while running:
    key_pressed = pygame.key.get_pressed()

    # draw board and fill with background img
    game_board.fill_color()
    game_board.draw_background()
    game_board.show_score()

    # draw snake head
    game_board.get_board().blit(snake_head.get_snake_head_img(), snake_head.get_snake_head_rect())
    snake_head.move()
    snake_head.check_last_direction(key_pressed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if snake_head.is_end_x(snake_head.get_snake_head_rect()) or snake_head.is_end_y(snake_head.get_snake_head_rect()):
        game_board.show_game_over()
    pygame.display.update()
    game_board.get_clock(60)
