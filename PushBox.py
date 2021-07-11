import pygame
import time
pygame.init()

surfaceWidth = 800
surfaceHeight = 600
x_blocks = 6
y_blocks = 6
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

displayList = [[1, 1, 1, 1, 1, 1],[1, 0, 0, 0, 4, 1], [1, 0, 3, 3, 0, 1],
               [1,0 ,0 ,1 ,0 ,1],[1 ,1 ,4 ,0 , 0 ,1], [1, 1, 1, 1, 1, 1]]

def drawBoxes(x, y):
    startX = (surfaceWidth - 52 * x_blocks) / 2
    startY = (surfaceHeight-52 * y_blocks)/2
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


playerX = 2
playerY = 1

wantX = playerX
wantY = playerY
winGame = False

directionBox = "left"

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


        if displayList[wantY][wantX] == 1:
            pass
        elif displayList[wantY][wantX] == 3 or displayList[wantY][wantX] == 5:
            if directionBox == "up":
                if displayList[wantY-1][wantX] == 1 or displayList[wantY-1][wantX] == 3 or displayList[wantY - 1][wantX] == 5:
                    pass
                elif displayList[wantY-1][wantX] == 4:
                    displayList[wantY][wantX] = 0
                    displayList[wantY - 1][wantX] = 5
                elif displayList[wantY-1][wantX] == 5:
                    displayList[wantY][wantX] = 4
                    displayList[wantY - 1][wantX] = 3
                else:
                    displayList[wantY][wantX] = 0
                    displayList[wantY-1][wantX] = 3

            elif directionBox == "down":
                if displayList[wantY + 1][wantX] == 1 or displayList[wantY + 1][wantX] == 3 or displayList[wantY + 1][wantX] == 5:
                    pass
                elif displayList[wantY+1][wantX] == 4:
                    displayList[wantY][wantX] = 0
                    displayList[wantY + 1][wantX] = 5
                elif displayList[wantY + 1][wantX] == 5:
                    displayList[wantY][wantX] = 4
                    displayList[wantY + 1][wantX] = 3
                else:
                    displayList[wantY][wantX] = 0
                    displayList[wantY+1][wantX] = 3
            elif directionBox == "left":
                if displayList[wantY][wantX - 1] == 1 or displayList[wantY][wantX - 1] == 3 or displayList[wantY][wantX-1] == 5:
                    pass

                elif displayList[wantY][wantX-1] == 4:
                    displayList[wantY][wantX] = 0
                    displayList[wantY][wantX-1] = 5
                elif displayList[wantY][wantX-1] == 5:
                    displayList[wantY][wantX] = 4
                    displayList[wantY][wantX-1] = 3
                else:
                    displayList[wantY][wantX] = 0
                    displayList[wantY][wantX-1] = 3
            elif directionBox == "right":
                if displayList[wantY][wantX + 1] == 1 or displayList[wantY][wantX + 1] == 3 or displayList[wantY][wantX+1] == 5:
                    pass
                elif displayList[wantY][wantX+1] == 4:
                    displayList[wantY][wantX] = 0
                    displayList[wantY][wantX+1] = 5
                elif displayList[wantY][wantX+1] == 5:
                    displayList[wantY][wantX] = 4
                    displayList[wantY][wantX+1] = 3
                else:
                    displayList[wantY][wantX] = 0
                    displayList[wantY][wantX+1] = 3




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



        pygame.display.update()
        clock.tick(60)

        if winGame:
            x_blocks = 7
            playerX = 1
            playerY = 2
            wantX = playerX
            wantY = playerY
            displayList = [[1, 1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1, 1], [1, 0, 0, 3, 0, 0, 1], [1, 0, 3, 0, 5, 4, 1],[1, 1, 0, 3, 4, 4, 1], [1, 1, 1, 1, 1, 1, 1]]
            for event in pygame.event.get():None