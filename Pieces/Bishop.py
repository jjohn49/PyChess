from Pieces.Piece import Piece
from Board.Square import Square


class Bishop(Piece):
    def __init__(self, x, y, color):
        Piece.__init__(self=self, name="bishop", x=x , y=y, color=color )

    def getMoves(self, board):

        def getUpRightMoves():
            moves=[]
            x = self.x
            y = self.y

            while x!= 'i' and y != 9:
                if x == self.x and y == self.y:
                    x = chr(ord(x) + 1)
                    y = y + 1
                    continue

                square = board[y][x]

                if square.isOccupied() == None:
                    moves.append((x,y))
                    x = chr(ord(x) + 1)
                    y = y + 1
                    continue

                piece = square.isOccupied()

                if piece.getColor() != self.color:
                    moves.append((x,y))
                
                break
            return moves

        def getUpLeftMoves():
            moves = []
            x = self.x
            y = self.y

            while x!= chr(ord('a') - 1) and y != 9:
                if x == self.x and y == self.y:
                    x = chr(ord(x) - 1)
                    y = y + 1
                    continue

                square = board[y][x]

                if square.isOccupied() == None:
                    moves.append((x,y))
                    x = chr(ord(x) - 1)
                    y = y + 1
                    continue

                piece = square.isOccupied()

                if piece.getColor() != self.color:
                    moves.append((x,y))
                
                break

            return moves

        def getDownRightMoves():
            moves=[]
            x = self.x
            y = self.y

            while x!= 'i' and y != 0:
                
                if x == self.x and y == self.y:
                    x = chr(ord(x) + 1)
                    y = y - 1
                    continue

                square = board[y][x]

                if square.isOccupied() == None:
                    moves.append((x,y))
                    x = chr(ord(x) + 1)
                    y = y - 1
                    continue

                piece = square.isOccupied()

                if piece.getColor() != self.color:
                    moves.append((x,y))
                
                break
            return moves

        def getDownLeftMoves():
            moves=[]
            x = self.x
            y = self.y

            while x!= chr(ord('a')-1) and y != 0:
                if x == self.x and y == self.y:
                    x = chr(ord(x) - 1)
                    y = y - 1
                    continue

                square = board[y][x]

                if square.isOccupied() == None:
                    moves.append((x,y))
                    x = chr(ord(x) - 1)
                    y = y - 1
                    continue

                piece = square.isOccupied()

                if piece.getColor() != self.color:
                    moves.append((x,y))
                
                break
            return moves

        return getUpRightMoves() + getUpLeftMoves() + getDownRightMoves() + getDownLeftMoves()
