from Pieces.Piece import Piece


class King(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="king", x=x , y=y, color=color )