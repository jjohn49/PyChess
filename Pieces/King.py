from Pieces import Piece


class King(Piece):

    def __init__(self, x, y, color):
        Piece.__init__("king", x, y, color)