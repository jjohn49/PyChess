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

    def __str__(self) -> str:
        return "name: " + self.name + "\ncolor: " + self.color + "\nAt position " + self.x + str(self.y)

    def setPosition(self, row, col):
        self.x = row
        self.y = col

    #placeholder function
    def getMoves(self, board):
        return []