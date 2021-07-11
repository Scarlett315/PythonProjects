import pygame
import random

pygame.init()

surfaceWidth = 1024
surfaceHeight = 768

sideLength = int(input("Side length of the board "))
bombNum = int(input("Number of bombs "))


surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Minesweeper")

#Randomize the location of bombs
def makeBombs():
    bolist = []
    bombCount = 0
    while bombCount < bombNum:
        a = random.randint(0, sideLength -1)
        b = random.randint(0, sideLength -1)
        if [a, b] in bolist:
            continue
        else:
            bolist.append([a, b])
            bombCount+= 1
    return bolist

def findFlag(covList):
    numOfFlags = 0
    for flagc in covList:
        for flagco in flagc:
            if flagco == 2:
                numOfFlags += 1
    return numOfFlags

#Create the map
clist = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
def makeNewMap():
    bolist = makeBombs()
    disList = []
    for e in range(sideLength):
        l = []
        for i in range(sideLength):
            l.append(0)
        disList.append(l)
    for r in bolist:
        print(r)
        disList[r[0]][r[1]] = -1
    for x in range(sideLength):
        for y in range(sideLength):
            if disList[x][y] != -1:
                bocount = 0
                for c in clist:
                    if x + c[0] >= 0 and y + c[1] >= 0 and x + c[0] <= sideLength - 1 and y + c[1] <= sideLength - 1:
                        if disList[x + c[0]][y + c[1]] == -1:
                            bocount += 1
                disList[x][y] = bocount

    return (disList, bolist)

displayList = []
coverList = []

#add to coverList
for e in range(sideLength):
    j = []
    for i in range(sideLength):
        j.append(1)
    coverList.append(j)


(displayList, blist) = makeNewMap()


#Pictures
one = pygame.image.load("minesweeper/1.png")
two = pygame.image.load("minesweeper/2.png")
three = pygame.image.load("minesweeper/3.png")
four = pygame.image.load("minesweeper/4.png")
five = pygame.image.load("minesweeper/5.png")
six = pygame.image.load("minesweeper/6.png")
seven = pygame.image.load("minesweeper/7.png")
eight = pygame.image.load("minesweeper/8.png")
blank = pygame.image.load("minesweeper/BlankSquare.png")
bmine = pygame.image.load("minesweeper/MineBlack.png")
rmine = pygame.image.load("minesweeper/MineRed.png")
flag = pygame.image.load("minesweeper/NewFlag.png")
bluesquare = pygame.image.load("minesweeper/BlueSquare.png")
YouLose = pygame.image.load("minesweeper/MSYouLose.png")
YouWin = pygame.image.load("betterwin.png")

def draw(x, y, image):
    surface.blit(image, (x, y))

for m in displayList:
    print(m)

#draw according to displayList and coverList
def drawBoxes(list, colist):
    startX = (surfaceWidth - (35*sideLength))/2
    startY = (surfaceHeight - (35*sideLength))/2
    drawX = startX
    drawY = startY
    for i in range(len(list)):
        l = list[i]
        k = colist[i]
        for j in range(len(l)):
            o = l[j]
            if 0 == k[j]:
                if o == -1:
                    draw(drawX, drawY, bmine)
                elif o == -2:
                    draw(drawX, drawY, rmine)
                elif o == 0:
                    draw(drawX, drawY, blank)
                elif o == 1:
                    draw(drawX, drawY, one)
                elif o == 2:
                    draw(drawX, drawY, two)
                elif o == 3:
                    draw(drawX, drawY, three)
                elif o == 4:
                    draw(drawX, drawY, four)
                elif o == 5:
                    draw(drawX, drawY, five)
                elif o == 6:
                    draw(drawX, drawY, six)
                elif o == 7:
                    draw(drawX, drawY, seven)
                elif o == 8:
                    draw(drawX, drawY, eight)
            elif k[j] == 2:
                draw(drawX, drawY, flag)

            else:
                draw(drawX, drawY, bluesquare)


            drawX += 35
        drawY += 35
        drawX = startX

#Game loop
flagCount = 0
Left = 1
Right = 3
game_over = False
firstClick = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)
        #Left click
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and event.button == Left:
            print("left")
            x, y = event.pos
            for e in range(len(displayList)):
                d = displayList[e]
                for i in range(len(d)):
                        a = pygame.Rect((surfaceWidth - (35*sideLength))/2 + 35*i, (surfaceHeight - (35*sideLength))/2 + 35*e, 35, 35)
                        b = a.collidepoint(x, y)
                        if b:
                            #First click, check if there is a bomb on that space
                            if firstClick and displayList[e][i] != 0:
                                while displayList[e][i] != 0:
                                    (displayList, blist) = makeNewMap()
                                    print("bomb ded")
                            firstClick = False
                            #Click on an empty space
                            if displayList[e][i] == 0:
                                coverList[e][i] = 0
                                zlist = [[e, i]]
                                while len(zlist) != 0:
                                    q = zlist.pop(0)
                                    for m in clist:
                                        qm0 = q[0] + m[0]
                                        qm1 = q[1] + m[1]
                                        if 0 <= qm0 <= sideLength-1 and 0 <= qm1 <= sideLength-1:
                                            z = displayList[qm0][qm1]

                                            if z == 0 and coverList[qm0][qm1] != 0:
                                                zlist.append([qm0, qm1])
                                                coverList[qm0][qm1] = 0
                                            elif z == -1:
                                                pass
                                            else:
                                                coverList[qm0][qm1] = 0
                            #Game over
                            if displayList[e][i] == -1 and coverList[e][i] != 0:
                                displayList[e][i] = -2
                                game_over = True
                                for e2 in blist:
                                    coverList[e2[0]][e2[1]] = 0
                                draw(512 - 225/2, 600, YouLose)



                            else:
                                coverList[e][i] = 0
        #Place flags(right click)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and event.button == Right:
            print("right")
            x1, y1 = event.pos
            for e1 in range(len(displayList)):
                d1 = displayList[e1]
                for i1 in range(len(d1)):
                    a1 = pygame.Rect((surfaceWidth - (35*sideLength))/2 + 35*i1, (surfaceHeight - (35*sideLength))/2 + 35*e1, 35, 35)
                    b1 = a1.collidepoint(x1, y1)
                    if b1 and coverList[e1][i1] == 1:
                        coverList[e1][i1] = 2
                    elif b1 and coverList[e1][i1] == 2:
                        coverList[e1][i1] = 1

    flagCount = findFlag(coverList)
    #Win game
    coverCount = 0
    for win in coverList:
        for win1 in win:
            if win1 == 1:
                coverCount += 1

    if coverCount == 0 and flagCount == bombNum:
        game_over = True
        draw(212, 200, YouWin)

    drawBoxes(displayList, coverList)

    pygame.display.update()
    clock.tick(60)