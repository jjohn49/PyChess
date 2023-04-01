from Pieces import Piece


class Queen(Piece):

    def __init__(self, x, y, color):
        Piece.__init__("queen", x, y, color)