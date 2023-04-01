class Piece:

    def __init__(self, name, x, y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = color

    def getPosition(self):
        return self.x, self.y
