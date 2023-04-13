from Pieces.Piece import Piece


class King(Piece):

    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="king", x=x , y=y, color=color )

    def getMoves(self, board):
        moves=[]
        
        #all moves to the right
        if chr(ord(self.x) + 1) != 'i':
            x = chr(ord(self.x) + 1)
            
            if self.y - 1 > 1 and (board[self.y-1][x].isOccupied() == None or board[self.y-1][x].isOccupied().getColor() != self.color):
                moves.append((x,self.y -1))

            if self.y + 1 < 9 and (board[self.y+1][x].isOccupied() == None or board[self.y+1][x].isOccupied().getColor() != self.color):
                moves.append((x,self.y + 1))

            if (board[self.y][x].isOccupied() == None or board[self.y][x].isOccupied().getColor() != self.color):
                moves.append((x,self.y))
                

        #all moves to the left
        if chr(ord(self.x) - 1) != chr(ord('a') - 1):
            x = chr(ord(self.x) - 1)
            
            if self.y - 1 > 0 and (board[self.y-1][x].isOccupied() == None or board[self.y-1][x].isOccupied().getColor() != self.color):
                moves.append((x,self.y -1))

            if self.y + 1 < 9 and (board[self.y+1][x].isOccupied() == None or board[self.y+1][x].isOccupied().getColor() != self.color):
                moves.append((x,self.y + 1))

            if (board[self.y][x].isOccupied() == None or board[self.y][x].isOccupied().getColor() != self.color):
                moves.append((x,self.y))

        #move 1 up 
        if self.y + 1 < 9 and (board[self.y+1][self.x].isOccupied() == None or board[self.y+1][self.x].isOccupied().getColor() != self.color):
                moves.append((self.x,self.y + 1))

        #move 1 down
        if self.y - 1 > 0 and (board[self.y-1][self.x].isOccupied() == None or board[self.y-1][self.x].isOccupied().getColor() != self.color):
                moves.append((self.x,self.y - 1))


        return moves
