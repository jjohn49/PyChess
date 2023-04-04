from Board.Square import Square
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Knight import Knight
import pygame

class Board:
    #Starting Board
    def __init__(self):

        self.board = {
            1:{
                "a": Square(Rook('a', 1, "white"), "black"),
                "b": Square(Knight('b', 1, "white"), "white"),
                "c": Square(Bishop('c', 1, "white"), "black"),
                "d": Square(Queen('d', 1, "white"), "white"),
                "e": Square(King('e', 1, "white"), "black"),
                "f": Square(Bishop('f', 1, "white"), "white"),
                "g": Square(Knight('g', 1, "white"), "black"),
                "h": Square(Rook('h', 1, "white"), "white"),
            },
            2:{
                "a": Square(Pawn('a', 2, "white"), "white"),
                "b": Square(Pawn('b', 2, "white"), "black"),
                "c": Square(Pawn('c', 2, "white"), "white"),
                "d": Square(Pawn('d', 2, "white"), "black"),
                "e": Square(Pawn('e', 2, "white"), "white"),
                "f": Square(Pawn('f', 2, "white"), "black"),
                "g": Square(Pawn('g', 2, "white"), "white"),
                "h": Square(Pawn('h', 2, "white"), "black"),
            },
            3:{
                "a": Square(None, "black"),
                "b": Square(None, "white"),
                "c": Square(None, "black"),
                "d": Square(None, "white"),
                "e": Square(None, "black"),
                "f": Square(None, "white"),
                "g": Square(None, "black"),
                "h": Square(None, "white"),
            },
            4:{
                "a": Square(None, "white"),
                "b": Square(None, "black"),
                "c": Square(None, "white"),
                "d": Square(None, "black"),
                "e": Square(None, "white"),
                "f": Square(None, "black"),
                "g": Square(None, "white"),
                "h": Square(None, "black"),
            },
            5:{
                "a": Square(None, "black"),
                "b": Square(None, "white"),
                "c": Square(None, "black"),
                "d": Square(None, "white"),
                "e": Square(None, "black"),
                "f": Square(None, "white"),
                "g": Square(None, "black"),
                "h": Square(None, "white"),
            },
            6:{
                "a": Square(None, "white"),
                "b": Square(None, "black"),
                "c": Square(None, "white"),
                "d": Square(None, "black"),
                "e": Square(None, "white"),
                "f": Square(None, "black"),
                "g": Square(None, "white"),
                "h": Square(None, "black"),
            },
            7:{
                "a": Square(Pawn('a', 7, "black"), "black"),
                "b": Square(Pawn('b', 7, "black"), "white"),
                "c": Square(Pawn('c', 7, "black"), "black"),
                "d": Square(Pawn('d', 7, "black"), "white"),
                "e": Square(Pawn('e', 7, "black"), "black"),
                "f": Square(Pawn('f', 7, "black"), "white"),
                "g": Square(Pawn('g', 7, "black"), "black"),
                "h": Square(Pawn('h', 7, "black"), "white"),
            },
            8:{
                "a": Square(Rook('a', 8, "black"), "white"),
                "b": Square(Knight('b', 8, "black"), "black"),
                "c": Square(Bishop('c', 8, "black"), "white"),
                "d": Square(Queen('d', 8, "black"), "black"),
                "e": Square(King('e', 8, "black"), "white"),
                "f": Square(Bishop('f', 8, "black"), "black"),
                "g": Square(Knight('g', 8, "black"), "white"),
                "h": Square(Rook('h', 8, "black"), "black"),
            },
        }
    
    def chessPositionToXY(self, coordinates):
        (x,y) = coordinates
        return ((ord(x) - 96) * 100) - 100, (y * 100)-100

    def drawPieces(self, screen):
        wPawn = pygame.image.load('Pieces/PieceImages/White-Pawn.png')
        bPawn = pygame.image.load('Pieces/PieceImages/Black-Pawn.png')

        wRook = pygame.image.load('Pieces/PieceImages/White-Rook.png')
        bRook = pygame.image.load('Pieces/PieceImages/Black-Rook.png')

        wBishop = pygame.image.load('Pieces/PieceImages/White-Bishop.png')
        bBishop = pygame.image.load('Pieces/PieceImages/Black-Bishop.png')

        wKing = pygame.image.load('Pieces/PieceImages/White-King.png')
        bKing = pygame.image.load('Pieces/PieceImages/Black-King.png')

        wQueen = pygame.image.load('Pieces/PieceImages/White-Queen.png')
        bQueen = pygame.image.load('Pieces/PieceImages/Black-Queen.png')

        wKnight = pygame.image.load('Pieces/PieceImages/White-Knight.png')
        bKnight = pygame.image.load('Pieces/PieceImages/Black-Knight.png')

        for row in range(8):
            for col in range(8):
                square = list(self.board[row+1].values())[col]

                if square.isOccupied() == None:
                    continue

                piece = square.isOccupied()

                if piece.getName() == 'pawn' and piece.getColor() == "white":
                    screen.blit(wPawn, self.chessPositionToXY(piece.getPosition()))

                elif piece.getName() == 'pawn' and piece.getColor() == "black":
                    screen.blit(bPawn, self.chessPositionToXY(piece.getPosition()))

                elif piece.getName() == 'rook' and piece.getColor() == "white":
                    screen.blit(wRook, self.chessPositionToXY(piece.getPosition()))

                elif piece.getName() == 'rook' and piece.getColor() == "black":
                    screen.blit(bRook, self.chessPositionToXY(piece.getPosition()))

                elif piece.getName() == 'knight' and piece.getColor() == "white":
                    screen.blit(wKnight, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'knight' and square.isOccupied().getColor() == "black":
                    screen.blit(bKnight, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'bishop' and square.isOccupied().getColor() == "white":
                    screen.blit(wBishop, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'bishop' and square.isOccupied().getColor() == "black":
                    screen.blit(bBishop, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'queen' and square.isOccupied().getColor() == "white":
                    screen.blit(wQueen, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'queen' and square.isOccupied().getColor() == "black":
                    screen.blit(bQueen, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'king' and square.isOccupied().getColor() == "white":
                    screen.blit(wKing, self.chessPositionToXY(piece.getPosition()))

                elif square.isOccupied().getName() == 'king' and square.isOccupied().getColor() == "black":
                    screen.blit(bKing, self.chessPositionToXY(piece.getPosition()))



    def getBoard(self):
        return self.board

    def drawBoard(self, screen):
        # Define constants for the screen width and height
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800

        SQUARE_SIZE = 100

        WHITE = (176,196,222)
        BLACK = (65,105,225)

        screen.fill(WHITE)

        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(screen, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


        self.drawPieces(screen)

        pygame.display.flip()



