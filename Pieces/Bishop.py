from Pieces import Piece


class Bishop(Piece):

    def __init__(self, x, y, color):
        Piece.__init__("bishop", x, y, color)