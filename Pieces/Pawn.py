from Pieces.Piece import Piece

class Pawn(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="pawn", x=x , y=y, color=color )

    def getMoves(self, board):
        moves = []

        if self.color == "white":
            offset = 1
        else:
            offset = -1

        #2 up from starting position

        if(self.color == 'white' and self.y == 2 and (board[self.y + (offset * 2)][self.x]  == None)):
            moves.append((chr(ord(self.x)), self.y + (2*offset)  ))

        elif(self.color == 'black' and self.y == 7 and (board[self.y + (offset * 2)][self.x]  == None)):
            moves.append((chr(ord(self.x)), self.y + (2*offset)  ))

        #Makes sure that the pawn is not at the end of the board
        #Might not be needed now that I think about it because when a pawn gets to the end of the board it becomes a new piece
        if not self.y == 8 or self.y == 1:

            #1 up
            if board[self.y + offset][self.x]  == None:
                moves.append((self.x, self.y + offset))

            #1 up and 1 right
            if self.x != 'h' and board[self.y + offset][chr(ord(self.x) + 1)] != None and board[self.y + offset][chr(ord(self.x) + 1)].getColor() != self.color:
                moves.append( (chr(ord(self.x) + 1), self.y + offset ) )

            #1 up and to the left
            if self.x != 'a' and board[self.y + offset][chr(ord(self.x) - 1)] != None and board[self.y + offset][chr(ord(self.x) - 1)].getColor() != self.color:
                moves.append(  (chr(ord(self.x) - 1), self.y + offset , ) )

        #print(moves)

        return moves