from Pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, x , y, color):
        Piece.__init__(self=self, name="rook", x=x , y=y, color=color )

    def getMoves(self, board):
        moves = []
        for col in board[self.y]:
            if board[col][self.y].isOccupied() != None:
                break

            moves.append((self.x, col))

        for row in ['a','b','c','d','e','f','g','h']:
            if board[self.y][row].isOccupied() != None:
                break

            moves.append((row, self.y))

        return moves



