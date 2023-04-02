class Piece:

    def __init__(self, name, x, y, color):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.isCaptured = False

    def getPosition(self):
        return self.x, self.y

    def move(self, x, y):
        self.x = x
        self.y = y
    def getName(self):
        return self.name

    def getColor(self):
        return self.color