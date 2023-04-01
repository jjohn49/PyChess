from Pieces import Piece


class Rook(Piece):

    def __init__(self, x , y, color):
        Piece.__init__("rook", x , y, color)