import pygame
import game_board
import snake
import food


pygame.init()

game_board = game_board.GameBoard()
snake = snake.Snake()
food = food.Food()


game_board.display_game_title()
game_board.display_game_icon()

pygame.time.set_timer(pygame.USEREVENT, 100)

game_board.set_clock(90)

food.check_food_position(snake.get_snake_position())

running = True

while running:
    game_board.fill_color()
    game_board.draw_background()

    snake.draw(game_board.get_board())
    food.draw(game_board.get_board())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            snake.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.get_last_direction() != "right":
                snake.set_direction_left()
            elif event.key == pygame.K_RIGHT and snake.get_last_direction() != "left":
                snake.set_direction_right()
            elif event.key == pygame.K_UP and snake.get_last_direction() != "down":
                snake.set_direction_up()
            elif event.key == pygame.K_DOWN and snake.get_last_direction() != "up":
                snake.set_direction_down()

    if snake.is_food_collision(food.get_food_rect()):
        game_board.hiss_sound()
        snake.add_new_segment()
        food.check_food_position(snake.get_snake_position())
        game_board.rise_score()

    if snake.is_snake_tail_collision() or snake.is_border_collision():
        game_board.show_game_over()

    game_board.show_win_game()
    game_board.show_score()
    pygame.display.update()
