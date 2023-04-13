from Pieces.Piece import Piece


class Bishop(Piece):
    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="bishop", x=x , y=y, color=color )

    def getMoves(self, board):
        return 

    def getUpRightMoves(self, board):
        x = self.x
        y = self.y