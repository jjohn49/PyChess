import pygame
from Board.Board import Board

pygame.init()
screen = pygame.display.set_mode([500, 500])

board = Board().getBoard()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE = (255, 230, 153)
BLACK = (128,64,0)



def drawSquares(screen):
    x = 0
    y = 0
    screen.fill(WHITE)

    for row in board.values():
        for square in row.values():
            #print(square.color)
            if square.color == "black":
                #Problem is here
                pygame.draw.rect(screen, BLACK, pygame.Rect((x,y), (SCREEN_WIDTH/8,SCREEN_HEIGHT/8)))
            x = x + SCREEN_WIDTH/8
        y = y + 10
        pygame.display.flip()





# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
drawSquares(screen)
while True:

    x = 1