from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, x , y, color):
        Piece.__init__(self=self, name="rook", x=x , y=y, color=color )

    def getMoves(self, board):
        moves = []
        for col in board:
            if col == self.y:
                continue 

            if board[col][self.x].isOccupied() != None:
                print(col)
                print(self.x)
                if board[col][self.x].isOccupied().getColor() != self.color:
                    moves.append((self.x,col))
                break

            moves.append((self.x, col))

        for row in ['a','b','c','d','e','f','g','h']:
            if row == self.x:
                continue 

            if board[self.y][row].isOccupied() != None:
                if board[self.y][row].isOccupied().getColor() != self.color:
                    moves.append((row,self.y))
                break

            moves.append((row, self.y))

        print(moves)

        return moves



