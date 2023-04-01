class Square:

    def __init__(self, occupied ,color):
        self.occupied = occupied
        self.color = color

    #If empty should return none, else it will return a piece
    def isOccupied(self):
        return self.occupied

    def setOccupied(self, occupied):
        self.occupied = occupied