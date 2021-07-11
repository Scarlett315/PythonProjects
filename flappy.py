import pygame
import time
from random import randint
from random import randrange

pygame.init()

#Setup
black = (0,0,0)
white = (255,255,255)
sunset = (253, 72, 47)
greenyellow = (184, 255, 0)
brightblue = (47, 228, 253)
orange = (255, 113, 0)
yellow = (255, 236, 0)
purple = (252, 67, 255)

colorChoices = [greenyellow, brightblue, orange, yellow, purple]

surfaceWidth = 800
surfaceHeight = 500
imgHeight = 30
imgWidth = 40

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption("Flying Turkey")
clock = pygame.time.Clock()

img = pygame.image.load('PyTurkey.png')

#Functions

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score:" + str(count), True, white)
    surface.blit(text, [0, 0])

def blocks(x_block, y_block, block_width, block_height, gap, colorChoice):
    pygame.draw.rect(surface, colorChoice, [x_block, y_block, block_width, block_height])
    pygame.draw.rect(surface, colorChoice, [x_block, y_block+block_height+gap, block_width, surfaceHeight])


def replayOrQuit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.key != pygame.K_SPACE:
            continue
        return event.key
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, sunset)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press spacebar to continue.', smallText)
    typTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()


    while replayOrQuit() == None:
        clock.tick()
    main()




def gameOver():
    msgSurface("Oh no!")


def turkey(x, y, image):
    surface.blit(image, (x,y))

#Main Loop
def main():
    x = 150
    y = 200
    y_move = 5

    x_block = surfaceWidth
    y_block = 0
    point_block = False

    block_width = 75
    block_height = randint(0, surfaceWidth/2)
    gap = imgHeight*6
    block_move = 5

    current_score = 0

    blockColor = colorChoices[randrange(0,len(colorChoices))]

    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5
        if y <= 0 and y_move < 0:
            y_move = 0
        y += y_move

        surface.fill(black)
        turkey(x,y,img)
        score(current_score)

        blocks(x_block, y_block, block_width, block_height, gap, blockColor)
        x_block -= block_move

        if y > surfaceHeight-40:
            gameOver()

        if x_block < (-1*block_width):
            point_block = False
            x_block = surfaceWidth
            block_height = randint(0, surfaceWidth/2)

        if x+imgWidth > x_block:
            if x < x_block+block_width:
                print('possibly within the bounderies of x')
                if y < block_height:
                    print("Y crossover UPPER!")
                    if x-imgWidth < block_width + x_block:
                        print('game over hit upper')
                        gameOver()

        if x+imgWidth > x_block:
            print("x crossover")
            if y+imgHeight > block_height+gap:
                print("possible y crossover")
                if x < block_width + x_block:
                    print("game over LOWER")
                    gameOver()

        if x > x_block + block_width and not point_block:
            point_block = True
            current_score += 1


        pygame.display.update()
        clock.tick(100)


main()
pygame.quit()
quit()