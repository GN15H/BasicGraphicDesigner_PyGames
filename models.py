class Figure:
    def __init__(self, figureType, figureColor, figureThickness, figureFiller):
        self.figureType = figureType
        self.figureColor = figureColor
        self.figureThickness = figureThickness
        self.figureFiller = figureFiller

class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y