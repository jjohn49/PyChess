from Pieces.Piece import Piece

class Queen(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="queen", x=x , y=y, color=color )