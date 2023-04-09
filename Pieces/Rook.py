from turtle import right
from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, x , y, color):
        Piece.__init__(self=self, name="rook", x=x , y=y, color=color )

    def getMoves(self, board):
        #print(self.getDownMoves(board) + self.getUpMoves(board) + self.getLeftMoves(board) + self.getRightMoves(board))
        return self.getDownMoves(board) + self.getUpMoves(board) + self.getLeftMoves(board) + self.getRightMoves(board)

    def getDownMoves(self,board):
        moves = []
        col = self.y
        while(col >= 1):
            if col == self.y:
                col = col - 1
                continue

            square = board[col][self.x]

            if square.isOccupied() != None:
                if square.isOccupied().getColor() != self.color:
                    moves.append((self.x, col))
                break

            moves.append((self.x, col))
            col = col - 1

        return moves

    def getUpMoves(self,board):
        moves = []
        col = self.y
        while(col <= 8):
            if col == self.y:
                col = col + 1
                continue

            square = board[col][self.x]

            if square.isOccupied() != None:
                if square.isOccupied().getColor() != self.color:
                    moves.append((self.x, col))
                break

            moves.append((self.x, col))
            col = col + 1

        return moves

    def getLeftMoves(self,board):
        moves=[]
        row = self.x
        while(row != chr(ord('a') - 1)):
            
            if row == self.x:
                row = chr(ord(row) - 1)
                continue

            square = board[self.y][row]

            if square.isOccupied() != None:
                if square.isOccupied().getColor() != self.color:
                    moves.append((row, self.y))
                break

            moves.append((row, self.y))
            row = chr(ord(row) - 1)

        return moves

    def getRightMoves(self,board):
        moves = []
        row = self.x
        while(row != 'i'):

            if row == self.x:
                row = chr(ord(row) + 1)
                continue

            square = board[self.y][row]

            if square.isOccupied() != None:
                if square.isOccupied().getColor() != self.color:
                    moves.append((row, self.y))
                break

            moves.append((row, self.y))
            row = chr(ord(row) + 1)
        return moves



