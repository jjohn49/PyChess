from Pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="pawn", x=x , y=y, color=color )

    def getMoves(self, board):
        moves = []

        #2 up from starting position
        if(self.y == 2 and (board[self.y][chr(ord(self.x) + 2)]  == None)):
            moves.append((self.y , chr(ord(self.x) + 2) ))

        #Makes sure that the pawn is not at the end of the board
        #Might not be needed now that I think about it because when a pawn gets to the end of the board it becomes a new piece
        if not self.y == 8:

            #1 up
            if board[self.y][chr(ord(self.x) + 1)]  == None:
                moves.append(( self.y , chr(ord(self.x) + 2) ))

            #1 up and 1 right
            if self.x != 'h' and board[self.y + 1][chr(ord(self.x) + 1)] != None and board[self.y + 1][chr(ord(self.x) + 1)].getColor() == "black":
                moves.append(  ( self.y + 1 ,chr(ord(self.x) + 1) ) )

            #1 up and to the left
            if self.x != 'a' and board[self.y - 1][chr(ord(self.x) - 1)] != None and board[self.y - 1][chr(ord(self.x) - 1)].getColor() == "black":
                moves.append(  ( self.y - 1 ,chr(ord(self.x) - 1) ) )

        return moves