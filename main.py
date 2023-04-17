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

pieceMoving = None
mouseX , mouseY = 0,0
dragging = False
currentMoves = []

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

    if board.board[col][row] != None:
        pieceToMove = board.board[col][row]
        #deletes the piece from the board 
        board.board[col][row] = None

    return pieceToMove
    
#Placeholder var for moving piece

def doesMoveCreateCheck(newBoard, colorMoving):
    if colorMoving == "white":
        return board.isWhiteInCheckWithBoard(board=newBoard)
    else:
        return board.isBlackInCheckWithBoard(board=newBoard)
    


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pieceMoving = getPiece(eventPosition=event.pos)
            if pieceMoving != None:
                print(pieceMoving)
                dragging = True
                currentMoves = pieceMoving.getMoves(board.board)
                print(currentMoves)
                mouseX, mouseY = event.pos

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouseX, mouseY = event.pos
                
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            row, col = findChessSquareFromMouse(event.pos)

            newBoard = board.board
            newBoard[col][row] = pieceMoving

            if currentMoves.__contains__((row, col)) and not doesMoveCreateCheck(newBoard, pieceMoving.getColor()):
                pieceMoving.setPosition(row, col)
                board.board[col][row] = pieceMoving
                currentMoves = []
                #print(board.isCheck())
            else:
                newBoard = board.board
                row, col = pieceMoving.getPosition()
                board.board[col][row] = pieceMoving
                currentMoves = []
            pieceMoving = None



        board.drawBoard(screen, dragging, pieceMoving, (mouseX, mouseY))
        pygame.display.flip()