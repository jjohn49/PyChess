from Board.Square import Square
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook
from Pieces.Knight import Knight


class Board:
    #Starting Board
     def __init__(self):

         self.board = {
             1:{
                 "a": Square(Rook(1, 1, "white"), "black"),
                 "b": Square(Knight(2, 1, "white"), "white"),
                 "c": Square(Bishop(3, 1, "white"), "black"),
                 "d": Square(Queen(4, 1, "white"), "white"),
                 "e": Square(King(5, 1, "white"), "black"),
                 "f": Square(Bishop(6, 1, "white"), "white"),
                 "g": Square(Knight(7, 1, "white"), "black"),
                 "h": Square(Rook(8, 1, "white"), "white"),
             },
             2:{
                 "a": Square(Pawn(1, 2, "white"), "white"),
                 "b": Square(Pawn(2, 2, "white"), "black"),
                 "c": Square(Pawn(3, 2, "white"), "white"),
                 "d": Square(Pawn(4, 2, "white"), "black"),
                 "e": Square(Pawn(5, 2, "white"), "white"),
                 "f": Square(Pawn(6, 2, "white"), "black"),
                 "g": Square(Pawn(7, 2, "white"), "white"),
                 "h": Square(Pawn(8, 2, "white"), "black"),
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
                 "a": Square(Pawn(1, 2, "black"), "black"),
                 "b": Square(Pawn(2, 2, "black"), "white"),
                 "c": Square(Pawn(3, 2, "black"), "black"),
                 "d": Square(Pawn(4, 2, "black"), "white"),
                 "e": Square(Pawn(5, 2, "black"), "black"),
                 "f": Square(Pawn(6, 2, "black"), "white"),
                 "g": Square(Pawn(7, 2, "black"), "black"),
                 "h": Square(Pawn(8, 2, "black"), "white"),
             },
             8:{
                 "a": Square(Rook(1, 1, "black"), "white"),
                 "b": Square(Knight(2, 1, "black"), "black"),
                 "c": Square(Bishop(3, 1, "black"), "white"),
                 "d": Square(Queen(4, 1, "black"), "black"),
                 "e": Square(King(5, 1, "black"), "white"),
                 "f": Square(Bishop(6, 1, "black"), "black"),
                 "g": Square(Knight(7, 1, "black"), "white"),
                 "h": Square(Rook(8, 1, "black"), "black"),
             },
         }

     def getBoard(self):
        return self.board

