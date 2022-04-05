class milicia():

    def __init__(self, positionx, positiony, values):
        self.positionx = positionx
        self.positiony = positiony
        self.values = values
        self.siguiente = None
    
    def getPoder(self):
        return self.values
    