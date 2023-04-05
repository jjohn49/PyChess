import pygame
from Board.Board import Board
import math

pygame.init()
screen = pygame.display.set_mode([500, 500])

board = Board()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

board.drawBoard(screen)

dragging = False
pieceToMove = None

while True:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            '''
            for row in board.board.values():
                for square in row.values():
                    piece = square.isOccupied()
                    print(piece)
                    if piece == None:
                        continue

                    print("Pieces coordinates = " + str(board.chessPositionToXY(piece.getPosition())))
                    print("Mouse clicked at " + str(event.pos))

                    if board.chessPositionToXY(piece.getPosition()) == event.pos:
                        print("Clicked on " + piece)
                        dragging = True'''

            clickX, clickY = event.pos

            clickX = int(math.floor(clickX/100) * 100)
            clickY = int(math.floor(clickY/100) * 100)

            row, col = board.xyToChess((clickX,clickY))

            if board.board[col][row].isOccupied() != None:
                pieceToMove = 




                    

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
