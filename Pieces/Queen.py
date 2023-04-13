from Pieces.Bishop import Bishop
from Pieces.Piece import Piece
from Pieces.Rook import Rook
from Pieces.Bishop import Bishop

class Queen(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="queen", x=x , y=y, color=color )

    def getMoves(self, board):
        return Rook.getMoves(board) + Bishop.getMoves(board)