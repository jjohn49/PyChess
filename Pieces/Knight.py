from Pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="knight", x=x , y=y, color=color )

    def getMoves(self, board):
        moves = []

        #3 left, 1 up
        if (ord(self.x) - 2) >= ord('a') and self.y + 1 <= 8:
            square = board[self.y + 1][chr(ord(self.x) - 2)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) - 2), self.y + 1))

        #3 left, 1 down
        if (ord(self.x) - 2) >= ord('a') and self.y - 1 >= 1:
            square = board[self.y - 1][chr(ord(self.x) - 2)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) - 2), self.y - 1))

        #3 right, 1 up
        if (ord(self.x) + 2) <= ord('h') and self.y + 1 <= 8:
            square = board[self.y + 1][chr(ord(self.x) + 2)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) + 2), self.y + 1))

        #3 right, 1 down
        if (ord(self.x) + 2) <= ord('h') and self.y - 1 >= 1:
            square = board[self.y - 1][chr(ord(self.x) + 2)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) + 2), self.y - 1))

        #1 left, 3 up
        if (ord(self.x) - 1) >= ord('a') and self.y + 2 <= 8:
            square = board[self.y + 2][chr(ord(self.x) - 1)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) - 1), self.y + 2))

        #1 right, 3 up
        if (ord(self.x) + 1) <= ord('h') and self.y + 2 <= 8:
            square = board[self.y + 2][chr(ord(self.x) + 1)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) + 1), self.y + 2))

        #1 left, 3 down
        if (ord(self.x) - 1) >= ord('a') and self.y - 2 >= 1:
            square = board[self.y - 2][chr(ord(self.x) - 1)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) - 1), self.y - 2))

        #1 right, 3 down
        if (ord(self.x) + 1) <= ord('h') and self.y - 2 >= 1:
            square = board[self.y - 2][chr(ord(self.x) + 1)]
            if  square == None or square.getColor() != self.color:
                moves.append((chr(ord(self.x) + 1), self.y - 2))

        return moves


        

