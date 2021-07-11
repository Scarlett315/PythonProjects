import pygame

pygame.init()

surfaceWidth = 637
surfaceHeight = 623
black = (0, 0, 0)
displayList = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Tic Tac Toe")

O = pygame.image.load("Tac.png")
X = pygame.image.load("Tic.png")
board = pygame.image.load("board2.png")
win = pygame.image.load("betterwin.png")
drawRed = True
currentplayer = 2


def draw(x, y, image):
    surface.blit(image, (x, y))


def drawBoxes(list, blockSize):
    draw(0, 0, board)
    startX = 40
    startY = 40
    currentx = startX
    currenty = startY
    for d in list:
        for d2 in d:
            if d2 == 0:
                pass
            if d2 == 1:
                draw(currentx, currenty, O)
            if d2 == 2:
                draw(currentx, currenty, X)
            currentx += blockSize + 40
        currenty += blockSize + 55
        currentx = startX


game_over = False
winning = False
while not game_over:
    wincount = 0
    layer = 0
    num = 0
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for e in displayList:
                for i in e:
                    if i == 0:
                        a = pygame.Rect(40 + ((150 + 40) * num), 40 + ((150 + 55) * layer), 150, 150)
                        b = a.collidepoint(x, y)
                        if b:
                            if drawRed:
                                displayList[layer][num] = 1
                                drawRed = False
                                currentplayer = 1
                            else:
                                displayList[layer][num] = 2
                                drawRed = True
                                currentplayer = 2

                        else:
                            pass
                    num += 1
                    if num == 3:
                        num = 0

                layer += 1


    for e in displayList:
        if e == [1, 1, 1] or e == [2, 2, 2]:
            winning = True
            break
    for x in range(2):
        if displayList[0][x] == currentplayer and displayList[1][x] == currentplayer and displayList[2][x] == currentplayer:
            winning = True
            break
    if displayList[0][0] == currentplayer and displayList[1][1] == currentplayer and displayList[2][2] == currentplayer:
        winning = True
        
    if displayList[0][2] == currentplayer and displayList[1][1] == currentplayer and displayList[2][0] == currentplayer:
        winning = True


    if winning:
        surface = pygame.display.set_mode((800, 600))
        draw(0, 0, win)



    if not winning:
        drawBoxes(displayList, 150)

    pygame.display.update()
    clock.tick(60)
