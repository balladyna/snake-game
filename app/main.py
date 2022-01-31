import pygame
import game_board

pygame.init()

pygame.display.set_caption("Snake")
icon = pygame.image.load("../assets/serpent.png")
pygame.display.set_icon(icon)

game_board = game_board.GameBoard()

running = True
while running:
    game_board.fill()
    game_board.blit()
    game_board.show_score()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_board.show_game_over()
    pygame.display.update()
