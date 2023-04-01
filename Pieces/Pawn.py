from Pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="pawn", x=x , y=y, color=color )

    def getMoves(self, board):
        #code to check if it can move 1, 2, take, enpassant, or can't move
        return 0