import pygame
import time
pygame.init()

surfaceWidth = 680
surfaceHeight = 880
black = (0, 0, 0)

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

board = pygame.image.load("board.png")
blueblock = pygame.image.load("blueblock.png")

def draw(x, y, image):
    surface.blit(image, (x, y))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    draw(0, 0, board)
    pygame.display.update()
    clock.tick(60)

