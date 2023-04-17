from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Knight import Knight
import pygame


class Board:
    # Starting Board
    def __init__(self):

        self.board = {
            1: {
                "a": Rook('a', 1, "white"),
                "b": Knight('b', 1, "white"),
                "c": Bishop('c', 1, "white"),
                "d": Queen('d', 1, "white"),
                "e": King('e', 1, "white"),
                "f": Bishop('f', 1, "white"),
                "g": Knight('g', 1, "white"),
                "h": Rook('h', 1, "white"),
            },
            2: {
                "a": Pawn('a', 2, "white"),
                "b": Pawn('b', 2, "white"),
                "c": Pawn('c', 2, "white"),
                "d": Pawn('d', 2, "white"),
                "e": Pawn('e', 2, "white"),
                "f": Pawn('f', 2, "white"),
                "g": Pawn('g', 2, "white"),
                "h": Pawn('h', 2, "white"),
            },
            3: {
                "a": None,
                "b": None,
                "c": None,
                "d": None,
                "e": None,
                "f": None,
                "g": None,
                "h": None,
            },
            4: {
                "a": None,
                "b": None,
                "c": None,
                "d": None,
                "e": None,
                "f": None,
                "g": None,
                "h": None,
            },
            5: {
                "a": None,
                "b": None,
                "c": None,
                "d": None,
                "e": None,
                "f": None,
                "g": None,
                "h": None,
            },
            6: {
                "a": None,
                "b": None,
                "c": None,
                "d": None,
                "e": None,
                "f": None,
                "g": None,
                "h": None,
            },
            7: {
                "a": Pawn('a', 7, "black"),
                "b": Pawn('b', 7, "black"),
                "c": Pawn('c', 7, "black"),
                "d": Pawn('d', 7, "black"),
                "e": Pawn('e', 7, "black"),
                "f": Pawn('f', 7, "black"),
                "g": Pawn('g', 7, "black"),
                "h": Pawn('h', 7, "black"),
            },
            8: {
                "a": Rook('a', 8, "black"),
                "b": Knight('b', 8, "black"),
                "c": Bishop('c', 8, "black"),
                "d": Queen('d', 8, "black"),
                "e": King('e', 8, "black"),
                "f": Bishop('f', 8, "black"),
                "g": Knight('g', 8, "black"),
                "h": Rook('h', 8, "black"),
            },
        }

    def chessPositionToXY(self, coordinates):
        x, y = coordinates
        return ((ord(x) - 96) * 100) - 100, 700 - ((y * 100)-100)

    def xyToChess(self, coordinates):
        x, y = coordinates
        return chr(int(((x + 100) / 100) + 96)), 9 - int((y+100) / 100)

    def drawPiece(self, screen, piece, position):
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

        if piece.getName() == 'pawn' and piece.getColor() == "white":
            screen.blit(wPawn, position)

        elif piece.getName() == 'pawn' and piece.getColor() == "black":
            screen.blit(bPawn, position)

        elif piece.getName() == 'rook' and piece.getColor() == "white":
            screen.blit(wRook, position)

        elif piece.getName() == 'rook' and piece.getColor() == "black":
            screen.blit(bRook, position)

        elif piece.getName() == 'knight' and piece.getColor() == "white":
            screen.blit(wKnight, position)

        elif piece.getName() == 'knight' and piece.getColor() == "black":
            screen.blit(bKnight, position)

        elif piece.getName() == 'bishop' and piece.getColor() == "white":
            screen.blit(wBishop, position)

        elif piece.getName() == 'bishop' and piece.getColor() == "black":
            screen.blit(bBishop, position)

        elif piece.getName() == 'queen' and piece.getColor() == "white":
            screen.blit(wQueen, position)

        elif piece.getName() == 'queen' and piece.getColor() == "black":
            screen.blit(bQueen, position)

        elif piece.getName() == 'king' and piece.getColor() == "white":
            screen.blit(wKing, position)

        elif piece.getName() == 'king' and piece.getColor() == "black":
            screen.blit(bKing, position)

    def drawPieces(self, screen, dragging, pieceMoving, position):

        if dragging:
            self.drawMoves(screen, pieceMoving.getMoves(self.board))
            self.drawPiece(screen, pieceMoving, position)
            

        for row in range(8):
            for col in range(8):
                square = list(self.board[row+1].values())[col]

                if square == None:
                    continue

                piece = square

                self.drawPiece(screen, piece, self.chessPositionToXY(piece.getPosition()))
       
    def getBoard(self):
        return self.board

    def drawMoves(self, screen, moves):
        GRAY = (  128,   128, 128)
        for move in moves:
            x, y = self.chessPositionToXY(move)
            pygame.draw.circle(screen, GRAY, (x + 50, y + 50), 35)

    def drawBoard(self, screen, dragging, pieceMoving, position):
        # Define constants for the screen width and height
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 800

        _SIZE = 100

        WHITE = (176,196,222)
        BLACK = (65,105,225)

        screen.fill(WHITE)

        for row in range(8):
            for col in range(row % 2, 8, 2):
                pygame.draw.rect(screen, BLACK, (row * _SIZE, col * _SIZE, _SIZE, _SIZE))


        self.drawPieces(screen, dragging, pieceMoving, position)

        pygame.display.flip()

    #For the current board
    def getAllMovesForPlayer(self, color):
        self.getAllMovesForPlayerWithBoard(color, self.board)

    def getAllMovesForPlayerWithBoard(self, color, board):
        moves = []
        for col in board.values():
            for piece in col.values():
                if piece != None and piece.getColor() == color:
                    moves = moves + piece.getMoves(board)

        return moves 

    #For the current board
    def getKingsPositionForPlayer(self, color):
        self.getKingsPositionForPlayerWithBoard(color, self.board)

    def getKingsPositionForPlayerWithBoard(self, color, board):
        for col in board.values():
            for piece in col.values():
                if piece != None and piece.getName() == 'king' and piece.getColor() == color:
                    return piece.getPosition()

        return None 

    def isWhiteInCheckWithBoard(self, board):
        blackMoves = self.getAllMovesForPlayerWithBoard("black", board)
        whiteKingPos = self.getKingsPositionForPlayerWithBoard("white", board)

        return whiteKingPos in blackMoves

    #For the current board
    def isWhiteInCheck(self):
        return self.isWhiteInCheckWithBoard(self.board)

    def isBlackInCheckWithBoard(self, board):
        whiteMoves = self.getAllMovesForPlayerWithBoard("white", board)
        blackKingPos = self.getKingsPositionForPlayerWithBoard("black", board)

        return blackKingPos in whiteMoves

    #For the current board
    def isBlackInCheck(self):
        return self.isBlackInCheckWithBoard(self.board)

    #For the current board
    def isCheck(self):
        return self.isWhiteInCheck() or self.isBlackInCheck()

    def isCheckWithBoard(self, board):
        return self.isWhiteInCheckWithBoard(board) or self.isBlackInCheckWithBoard(board)




    

            
        

        


