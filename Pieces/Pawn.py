from Pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="pawn", x=x , y=y, color=color )

    def getMoves(self, board):
        if(self.y == 2 and (board[self.y][chr(ord(self.x) + 1)]  == None) and (board[self.y][chr(ord(self.x) + 2)]  == None)):
            return []