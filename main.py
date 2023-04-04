import pygame
from Board.Board import Board

pygame.init()
screen = pygame.display.set_mode([500, 500])

board = Board()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board.drawBoard(screen)

while True:
    for events in pygame.event:
        # Something

    pygame.display.flip()