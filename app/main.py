import pygame
import game_board
import snake_head
import snake_tail
import food

pygame.init()

game_board = game_board.GameBoard()
snake_head = snake_head.SnakeHead()
snake_tail = snake_tail.SnakeTail()
food = food.Food()

game_board.display_game_title()
game_board.display_game_icon()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 100)

game_board.set_clock(60)

running = True

while running:
    key_pressed = pygame.key.get_pressed()

    # draw board and fill with background img
    game_board.fill_color()
    game_board.draw_background()
    game_board.show_score()
    food.draw_food(game_board.get_board())

    snake_head.draw_snake(game_board.get_board(), snake_tail.get_snake_tail(), snake_tail.get_snake_head())

    if food.food_collision(snake_tail.get_snake_head()):
        snake_tail.add_new_segment()
        food.randomize()
        food.draw_food(game_board.get_board())
        game_board.rise_score()

    if snake_tail.snake_tail_collision():
        game_board.show_game_over()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == screen_update:
            snake_tail.move_snake()
            snake_tail.change_direction(key_pressed)

    pygame.display.update()
