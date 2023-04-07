import pygame
from Board.Board import Board
import math

from Board.Square import Square

pygame.init()
screen = pygame.display.set_mode([500, 500])

board = Board()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pieceMoving = None
mouseX , mouseY = 0,0
dragging = False

board.drawBoard(screen, dragging, pieceMoving, (mouseX, mouseY))

def findChessSquareFromMouse(mouse):
    x, y = mouse

    x = int(math.floor(x/100) * 100)
    y = int(math.floor(y/100) * 100)

    row, col = board.xyToChess((x,y))

    return row, col


def getPiece(eventPosition):

    pieceToMove = None

    row, col = findChessSquareFromMouse(eventPosition)

    if board.board[col][row].isOccupied() != None:
        pieceToMove = board.board[col][row].isOccupied()
        #deletes the piece from the board 
        board.board[col][row] = Square(None, board.board[col][row].color)

    return pieceToMove
    
#Placeholder var for moving piece


while True:
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:

            pieceMoving = getPiece(eventPosition=event.pos)
            if pieceMoving != None:
                dragging = True

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouseX, mouseY = event.pos
                
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            row, col = findChessSquareFromMouse(event.pos)
            pieceMoving.setPosition(row, col)
            board.board[col][row] = Square(pieceMoving, board.board[col][row].color)
            pieceMoving = None



        board.drawBoard(screen, dragging, pieceMoving, (mouseX, mouseY))
