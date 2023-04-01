from Pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="knight", x=x , y=y, color=color )