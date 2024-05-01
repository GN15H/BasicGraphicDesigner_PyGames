from enum import Enum

class ColorType(Enum):
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    YELLOW = (255,255,0)
    CYAN = (0,255,255)
    MAGENTA = (255,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)

class FigureType(Enum):
    FREE = (1,2)
    LINE = (2,2)
    RECT = (3,2)
    CIRCLE = (4,2)
    ELLIPSIS = (5,2)
    TRIANGLE = (6,3)

class FillerType(Enum):
    FULL = True
    EMPTY = False

class ThicknessType(Enum):
    THIN = 2
    NORMAL = 4
    BOLD = 6

