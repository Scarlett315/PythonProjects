import pygame
from random import randint

pygame.init()

x = 0
pipex = 800


surfaceWidth = 800
surfaceHeight = 400
imgWidth = 360
pipeHeight = 800
pipeWidth = 72

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
clock = pygame.time.Clock()

pipe = pygame.image.load("pipe.png")
background = pygame.image.load("background.png")
def draw(x, y, image):
    surface.blit(image, (x,y))

game_over = False

pipeGap = randint(10, 390)
while not game_over:
    x_move = -2
    pipeMove = -5

    draw(x, 0, background)
    draw(x + imgWidth, 0, background)
    draw(x + imgWidth * 2, 0, background)
    draw(x + imgWidth * 3, 0, background)

    draw(pipex, pipeGap-340, pipe)

    if pipex <= -pipeWidth:
        pipex = surfaceWidth
        pipeGap = randint(10, 270)

    if x <= -imgWidth:
        x = 0
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    x += x_move
    pipex += pipeMove


    clock.tick(60)
