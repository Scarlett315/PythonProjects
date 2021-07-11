import pygame
from random import randint

pygame.init()




surfaceWidth = 800
surfaceHeight = 400
bgWidth = 360
pipeHeight = 800
pipeWidth = 72
imgHeight = 30
imgWidth = 40

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

pipe = pygame.image.load("pipe.png")
background = pygame.image.load("background.png")
bird = [pygame.image.load("birdup.png"), pygame.image.load("birdmid.png"), pygame.image.load("birddown.png")]
strawberry = pygame.image.load("strawberry.png")

def draw(x, y, image):
    surface.blit(image, (x,y))


def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render("Score:" + str(count), True, (255, 255, 255))
    surface.blit(text, [0, 0])

def makeTextObjs(text, font):
    textSurface = font.render(text, True, (253, 72, 47))
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

def replayOrQuit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.key != pygame.K_SPACE:
            continue
        return event.key
    return None






def main():
    bgx = 0

    pipex = 800
    x = 150
    y = 200
    strawx = 180

    y_move = 5
    straw_move = 5
    bgx_move = -2
    pipeMove = -5

    pipeGap = randint(10, 270)

    current_score = 0

    point_block = False
    flap = 0
    straw_list = []

    game_over = False
    while not game_over:

        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5
                elif event.key == pygame.K_q:
                    straw_list.append([strawx, y])



            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5



        if y <= 0 and y_move < 0:
            y_move = 0
        y += y_move


        #drawing
        draw(bgx, 0, background)
        draw(bgx + bgWidth, 0, background)
        draw(bgx + bgWidth * 2, 0, background)
        draw(bgx + bgWidth * 3, 0, background)

        draw(pipex, pipeGap-340, pipe)

        for o in straw_list:
            draw(o[0], o[1], strawberry)
            if o[0] >= pipex:
                    if o[1] > pipeGap and o[1] < pipeGap+120:
                        continue
                    else:
                        point_block = False
                        pipex = surfaceWidth + pipex
                        pipeGap = randint(10, 270)
                        straw_list.remove(o)

        draw(x, y, bird[flap])
        score(current_score)



        if pipex <= -pipeWidth:
            point_block = False
            pipex = surfaceWidth
            pipeGap = randint(10, 270)

        if bgx <= -bgWidth:
            bgx = 0

        if y > surfaceHeight - 40:
            gameOver()

        if x+imgWidth > pipex:
            if x < pipex+pipeWidth:
                if y < pipeGap:
                    if x-imgWidth < pipeWidth + pipex:
                        gameOver()

        if x+imgWidth > pipex:
            if y+imgHeight > pipeGap+120:
                if x < pipeWidth + pipex:
                    gameOver()

        if x > pipex + pipeWidth and not point_block:
            point_block = True
            current_score += 1



        bgx += bgx_move
        pipex += pipeMove

        for o in straw_list:
            o[0] += straw_move

        flap = (flap+1)%3

        pygame.display.update()
        clock.tick(60)


main()
pygame.quit()
quit()
