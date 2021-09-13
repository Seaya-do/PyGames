import pygame,sys
from pygame.locals import *


FPS = 30 #초당 프레임
WINDOWWIDTH = 640 #윈도우 너비(픽셀단위)
WINDOWHEIGHT = 480 #윈도우 높이
REVEALSPEED = 8
BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDHEIGHT) %2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH -(BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2 )
YMARGIN = int((WINDOWHEIGHT -(BOARDHEIGHT *(BOXSIZE + GAPSIZE))) / 2)


#R G B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255 ,0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)


BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
OVAL = 'oval'


ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT,"Board is too big for the number of shapes/colors defined."


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

    mouseX = 0
    mouseY = 0
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None #첫 번째 상자를 클릭했을 때 (X,Y)값 저장

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:
        moseClicked = False

        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():  # 이벤트 처리 루프
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION :
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONUP :
                mouseX, mouseY = event.pos
                mouseClicked = True

        boxX , boxY = getBoxAtPixel(mouseX, mouseY)
        if boxX != None and boxY != None: #마우스가 현재 박스 위에 있다.
            if not revealedBoxes[boxX][boxY]:
                drawHighlightBox(boxX, boxY)
            if not revealedBoxes[boxX][boxY] and mouseClicked:
                revealedBoxesAnimation(mainBoard, [(boxX, boxY)])
                revealedBoxes[boxX][boxY] =True #상자를 보이는 것으로 설정
                if firstSelection == None:
                    firstSelection = (boxX, boxY)
                else: #현재의 상자가 두번째 클릭한 상자일 때, 두 아아콘이 맞는 짝인지 검사
                    icon1shape , icon1color = getShapeAndColor(mainBoard,firstSelection[0],firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxX, boxY)





