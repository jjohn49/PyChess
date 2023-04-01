from Pieces import Piece


class Knight(Piece):

    def __init__(self, x, y, color):
        Piece.__init__("knight", x, y, color)