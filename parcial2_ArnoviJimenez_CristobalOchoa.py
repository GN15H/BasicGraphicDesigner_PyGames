# Example file showing a basic pygame "game loop"
import math
import pygame
from entities import ColorType, FigureType, ThicknessType, FillerType
from models import Figure, Position


def drawRect(screen,figure, pos_arr):
    pygame.draw.rect(screen,figure.figureColor.value,(min(pos_arr[0].x,pos_arr[1].x),min(pos_arr[0].y,pos_arr[1].y), abs(pos_arr[0].x - pos_arr[1].x),abs(pos_arr[0].y - pos_arr[1].y)), 0 if figure.figureFiller.value else figure.figureThickness.value)
def drawLine(screen,figure, pos_arr):
    pygame.draw.line(screen,figure.figureColor.value,(pos_arr[0].x,pos_arr[0].y), (pos_arr[1].x,pos_arr[1].y),figure.figureThickness.value)
def drawDot(screen,figure, pos_arr):
    (x,y)= pygame.mouse.get_pos()
    pygame.draw.line(screen,figure.figureColor.value,(x,y), (x + 2,y + 2),figure.figureThickness.value)
def drawCircle(screen,figure,pos_arr):
    pygame.draw.circle(screen,figure.figureColor.value,(pos_arr[0].x, pos_arr[0].y),(math.sqrt((pos_arr[0].x - pos_arr[1].x)**2 + (pos_arr[0].y - pos_arr[1].y)**2)), 0 if figure.figureFiller.value else figure.figureThickness.value)
def drawTriangle(screen,figure,pos_arr):
    pygame.draw.polygon(screen, figure.figureColor.value,[(pos_arr[0].x,pos_arr[0].y),(pos_arr[1].x,pos_arr[1].y),(pos_arr[2].x,pos_arr[2].y)], 0 if figure.figureFiller.value else figure.figureThickness.value)
def drawEllipse(screen,figure, pos_arr):
    pygame.draw.ellipse(screen,figure.figureColor.value,(min(pos_arr[0].x,pos_arr[1].x),min(pos_arr[0].y,pos_arr[1].y), abs(pos_arr[0].x - pos_arr[1].x),abs(pos_arr[0].y - pos_arr[1].y)), 0 if figure.figureFiller.value else figure.figureThickness.value)


def drawExampleFigure(screen,figure):
    if figure.figureType == FigureType.RECT:
        drawRect(screen,figure,[Position(65,20),Position(200,100)])
    elif figure.figureType == FigureType.CIRCLE:
        drawCircle(screen,figure,[Position(120,60),Position(150,80)])
    elif figure.figureType == FigureType.TRIANGLE:
        drawTriangle(screen,figure,[Position(60,100),Position(180,100),Position(120,20)])
    elif figure.figureType == FigureType.LINE:
        drawLine(screen,figure,[Position(60,100),Position(190,20)])
    elif figure.figureType == FigureType.ELLIPSIS:
        drawEllipse(screen,figure,[Position(65,20),Position(200,100)])
    elif figure.figureType == FigureType.FREE:
        drawLine(screen,figure,[Position(60,100),Position(70,80)])
        drawLine(screen,figure,[Position(70,80),Position(75,75)])
        drawLine(screen,figure,[Position(75,75),Position(80,80)])
        drawLine(screen,figure,[Position(80,80),Position(90,90)])
        drawLine(screen,figure,[Position(90,90),Position(95,95)])
        drawLine(screen,figure,[Position(95,95),Position(105,90)])
        drawLine(screen,figure,[Position(105,90),Position(120,70)])
        drawLine(screen,figure,[Position(120,70),Position(140,60)])


def drawFigure(screen, figure, pos_arr):
    if figure.figureType == FigureType.RECT:
        drawRect(screen,figure,pos_arr)
    elif figure.figureType == FigureType.CIRCLE:
        drawCircle(screen,figure,pos_arr)
    elif figure.figureType == FigureType.TRIANGLE:
        drawTriangle(screen,figure,pos_arr)
    elif figure.figureType == FigureType.LINE:
        drawLine(screen,figure,pos_arr)
    elif figure.figureType == FigureType.ELLIPSIS:
        drawEllipse(screen,figure,pos_arr)
    elif figure.figureType == FigureType.FREE:
        drawDot(screen,figure,pos_arr)


def setFigureType(position,figure):
    if position.y <60:
        if position.x >355 and position.x < 440:
            figure.figureType = FigureType.LINE
        elif position.x > 440 and position.x < 525:
            figure.figureType = FigureType.RECT
        else:
            figure.figureType = FigureType.CIRCLE
    else:
        if position.x >325 and position.x < 440:
            figure.figureType = FigureType.FREE
        elif position.x > 440 and position.x < 525:
            figure.figureType = FigureType.ELLIPSIS
        else:
            figure.figureType = FigureType.TRIANGLE

def setFigureColor(position, figure):
    if position.y <60 and position.y >10:
        if position.x >670 and position.x < 755:
            figure.figureColor = ColorType.RED
        elif position.x > 755 and position.x < 840:
            figure.figureColor = ColorType.GREEN
        else:
            figure.figureColor = ColorType.BLUE
    elif position.y<110:
        if position.x >670 and position.x < 755:
            figure.figureColor = ColorType.CYAN
        elif position.x > 755 and position.x < 840:
            figure.figureColor = ColorType.YELLOW
        else:
            figure.figureColor = ColorType.MAGENTA

def setFigureFiller(position, figure):
    if position.y <60 and position.y > 10:
        figure.figureFiller = FillerType.FULL
    elif position.y <110:
        figure.figureFiller = FillerType.EMPTY

def setFigureThickness(position, figure):
    if position.x > 985 and position.x <1070:
        figure.figureThickness = ThicknessType.THIN
    elif position.x >1070 and position.x < 1155:
        figure.figureThickness = ThicknessType.NORMAL
    else:
        figure.figureThickness = ThicknessType.BOLD


def getClick(position, arr, figure):
    if position.y < 120:
        if position.x>355 and position.x<610:
            setFigureType(position, figure)
        elif position.x>670 and position.x<925:
            setFigureColor(position, figure)
        elif position.x>245 and position.x<295:
            setFigureFiller(position, figure)
        elif position.x>985 and position.x<1240:
            setFigureThickness(position,figure)
        arr.clear()
        return False
    else:
        if figure.figureType == FigureType.FREE:
            return not draw
        arr.append(position)
        if len(arr) >= figure.figureType.value[1]:
            return True
        else:
            return False


# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

figure = Figure(FigureType.FREE, ColorType.GREEN, ThicknessType.NORMAL, FillerType.FULL)
pos_arr = []

draw = False

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y)= pygame.mouse.get_pos()
            draw = getClick(Position(x,y),pos_arr,figure)
            print(len(pos_arr))

    #if events

    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    #main division
    pygame.draw.rect(screen,(220,220,220),(0,0,1280,120))
    
    #sections
    pygame.draw.rect(screen,(245,245,245),(40,10,255,100))
    pygame.draw.rect(screen,(245,245,245),(355,10,255,100))
    pygame.draw.rect(screen,(245,245,245),(670,10,255,100))
    pygame.draw.rect(screen,(245,245,245),(985,10,255,100))
    
    #show figure divisions
    pygame.draw.line(screen,(220,220,220),(220,10),(220,110),2)
    pygame.draw.line(screen,(220,220,220),(220,60),(294,60),2)

    #figure type divisions
    pygame.draw.line(screen,(220,220,220),(355,60),(610,60),2)
    pygame.draw.line(screen,(220,220,220),(440,10),(440,110),2)
    pygame.draw.line(screen,(220,220,220),(525,10),(525,110),2)

    #figure color divisions
    pygame.draw.line(screen,(220,220,220),(670,60),(925,60),2)
    pygame.draw.line(screen,(220,220,220),(755,10),(755,110),2)
    pygame.draw.line(screen,(220,220,220),(840,10),(840,110),2)

    #figure thickness divisions
    pygame.draw.line(screen,(220,220,220),(1070,10),(1070,110),2)
    pygame.draw.line(screen,(220,220,220),(1155,10),(1155,110),2)
    
    #figure thickness lines
    pygame.draw.line(screen,figure.figureColor.value,(995,60),(1060,60),2)
    pygame.draw.line(screen,figure.figureColor.value,(1080,60),(1150,60),4)
    pygame.draw.line(screen,figure.figureColor.value,(1165,60),(1230,60),6)

    #figure types
    pygame.draw.line(screen,ColorType.BLACK.value,(365,20),(430,50),2)
    pygame.draw.rect(screen,ColorType.BLACK.value,(450,20,70,30),2)
    pygame.draw.circle(screen,ColorType.BLACK.value,(570,35),20,2)
    pygame.draw.ellipse(screen,ColorType.BLACK.value,(450,70,70,30),2)
    pygame.draw.polygon(screen,ColorType.BLACK.value,[(570,70),(540,100),(600,100)],2)

    pygame.draw.line(screen,ColorType.BLACK.value,(365,90),(370,80),2)
    pygame.draw.line(screen,ColorType.BLACK.value,(370,80),(375,80),2)
    pygame.draw.line(screen,ColorType.BLACK.value,(375,80),(390,90),2)
    pygame.draw.line(screen,ColorType.BLACK.value,(390,90),(420,95),2)

    #color types
    pygame.draw.rect(screen,ColorType.RED.value,(680,20,70,30))
    pygame.draw.rect(screen,ColorType.GREEN.value,(765,20,70,30))
    pygame.draw.rect(screen,ColorType.BLUE.value,(850,20,70,30))
    pygame.draw.rect(screen,ColorType.CYAN.value,(680,70,70,30))
    pygame.draw.rect(screen,ColorType.YELLOW.value,(765,70,70,30))
    pygame.draw.rect(screen,ColorType.MAGENTA.value,(850,70,70,30))

    #filler types
    pygame.draw.rect(screen,ColorType.BLACK.value,(245,20,30,30),0)
    pygame.draw.rect(screen,ColorType.BLACK.value,(245,70,30,30),2)

    drawExampleFigure(screen,figure)

    if draw:
        drawFigure(screen, figure, pos_arr)
        if figure.figureType != FigureType.FREE:
            pos_arr.clear()
            draw=False

    pygame.display.flip()

    clock.tick(30)  # limits FPS to 30

pygame.quit()