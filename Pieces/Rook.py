from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, x , y, color):
        Piece.__init__(self=self, name="rook", x=x , y=y, color=color )