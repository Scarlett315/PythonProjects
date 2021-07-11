import pygame
import time
pygame.init()

EMPTY = 0
BARRIER = 1
BOX = 3
GREENX = 4
REDBOX = 5

state = "in game"

surfaceWidth = 800
surfaceHeight = 600
black = (0, 0, 0)

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Push Box")

#Pictures
empty = pygame.image.load("floor.png")
barrier = pygame.image.load("wall.png")
player = pygame.image.load("dude.png")
box = pygame.image.load("box.png")
greenx = pygame.image.load("target.png")
redx = pygame.image.load("box_on_target.png")
win = pygame.image.load("betterwin.png")
x_blocks = 0
y_blocks = 0
PuzzleCount = 1


def readLevel(level):
    typeL = []

    p = "Puzzles/Puzzle" + str(level)
    puzzles = open(p, "r")
    currentP = puzzles.read().splitlines()
    split1 = currentP[0].split(",")
    width = int(split1[0])
    height = int(split1[1])
    split2 = currentP[1].split(",")
    playerx = int(split2[0])
    playery = int(split2[1])
    for i in currentP[2:height+2]:
        split3 = i.split(",")
        insideL = []
        for o in split3:
            insideL.append(int(o))
        typeL.append(insideL)
    return ((width, height), (playerx, playery), typeL)


def drawBoxes(x, y):
    startX = (surfaceWidth - 52 * x_blocks) / 2
    startY = (surfaceHeight - 52 * y_blocks)/2
    drawX = startX
    drawY = startY
    for l in displayList:
        for o in l:
            if o == 0:
                draw(drawX, drawY, empty)
            elif o == 1:
                draw(drawX, drawY, barrier)
            elif o == 3:
                draw(drawX, drawY, box)
            elif o == 4:
                draw(drawX, drawY, greenx)
            elif o == 5:
                draw(drawX, drawY, redx)
            drawX += 52
        drawY += 52
        drawX = startX
    draw(startX + 52*x, startY + 52*y, player)

def draw(x, y, image):
    surface.blit(image, (x, y))
    #print(x, y)

def push(list, boxX, boxY, dirX, dirY):
    if list[boxY + dirY][boxX + dirX] == BARRIER or list[boxY + dirY][boxX + dirX] == BOX or list[boxY + dirY][boxX + dirX] == REDBOX:
        pass
    elif list[boxY + dirY][boxX + dirX] == GREENX:
        if list[boxY][boxX] == BOX:
            list[boxY][boxX] = EMPTY
        else:
            list[boxY][boxX] = GREENX
        list[boxY + dirY][boxX + dirX] = REDBOX
    else:
        if list[boxY][boxX] == BOX:
            list[boxY][boxX] = EMPTY
        else:
            list[boxY][boxX] = GREENX
        list[boxY + dirY][boxX + dirX] = BOX

def makeTextObjs(text, font):
    textSurface = font.render(text, True, (253, 72, 47))
    return textSurface, textSurface.get_rect()



playerX = 0
playerY = 0
directionBox = "left"

((x_blocks, y_blocks), (playerX, playerY), displayList) = readLevel(PuzzleCount)
wantX = playerX
wantY = playerY
winGame = False

game_over = False
while not game_over:


        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    wantY = playerY -1
                    wantX = playerX
                    directionBox = "up"
                elif event.key == pygame.K_DOWN:
                    wantY = playerY +1
                    wantX = playerX
                    directionBox = "down"
                elif event.key == pygame.K_LEFT:
                    wantX = playerX -1
                    wantY = playerY
                    directionBox = "left"
                elif event.key == pygame.K_RIGHT:
                    wantX = playerX +1
                    wantY = playerY
                    directionBox = "right"
                elif event.key == pygame.K_SPACE:
                    ((x_blocks, y_blocks), (playerX, playerY), displayList) = readLevel(PuzzleCount)
                    wantX = playerX
                    wantY = playerY

        if displayList[wantY][wantX] == 1:
            pass
        elif displayList[wantY][wantX] == 3 or displayList[wantY][wantX] == 5:
            if directionBox == "up":
                push(displayList, wantX, wantY, 0, -1)
            elif directionBox == "down":
                push(displayList, wantX, wantY, 0, 1)
            elif directionBox == "left":
                push(displayList, wantX, wantY, -1, 0)
            elif directionBox == "right":
                push(displayList, wantX, wantY, 1, 0)
        else:
            playerX = wantX
            playerY = wantY

        for e in displayList:
            if 3 in e or 4 in e:
                winGame = False
                break
            else:
                pass
            winGame = True


        surface.fill(black)
        drawBoxes(playerX, playerY)
        if state == "in game":
            smallText = pygame.font.Font('freesansbold.ttf', 20)
            typTextSurf, typTextRect = makeTextObjs('Press spacebar to restart.', smallText)
            typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 250)
            surface.blit(typTextSurf, typTextRect)
        elif state == "transitioning":
            smallText = pygame.font.Font('freesansbold.ttf', 20)
            typTextSurf, typTextRect = makeTextObjs('Puzzle complete', smallText)
            typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 250)
            surface.blit(typTextSurf, typTextRect)
            counter -= 1
            if counter == 0:
                PuzzleCount += 1
                try:
                    ((x_blocks, y_blocks), (playerX, playerY), displayList) = readLevel(PuzzleCount)
                    wantX = playerX
                    wantY = playerY
                    state = "in game"
                    winGame = False
                except:
                    state = "win"
        elif state == "win":
            draw(0, 0, win)

        pygame.display.update()
        clock.tick(60)

        if winGame and state == "in game":
            state = "transitioning"
            counter = 60


#Just did this for 200 lines :P