import sys, os, math, random
import pygame
from pygame.locals import *
from blockClass import *

FPS = 3
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLOCK_WIDTH = 30
SCREEN_SIZE = (360, 680)

GRID_SIZE_X = 12 ### X GRID 12
GRID_SIZE_Y = 20 ### Y GRID 20

GRAVITY = (0, 1)
MOVE_LEFT = (-1, 0)
MOVE_RIGHT = (1, 0)

LOSE = False

pygame.init()

def handleEvents(block, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                block.move(screenArr, BLOCK_WIDTH, MOVE_RIGHT)
            elif event.key == K_LEFT:
                block.move(screenArr, BLOCK_WIDTH, MOVE_LEFT)
            elif event.key == K_DOWN:
                block.moveDown(screen, screenArr, BLOCK_WIDTH, GRAVITY)
            elif event.key == K_UP:
                block.rotate(screenArr, BLOCK_WIDTH)
            else:
                continue

    return True

def loadImages():
    colors[0] = pygame.image.load('Block1.png')
    colors[1] = pygame.image.load('Block2.png')
    colors[2] = pygame.image.load('Block3.png')
    colors[3] = pygame.image.load('Block4.png')

screen = pygame.display.set_mode(SCREEN_SIZE) ### MAKE SCREEN
clock = pygame.time.Clock()

background = pygame.Surface(SCREEN_SIZE) ### BACKGROUND LAYER
background.fill(GRAY) ### BLACK COLOR

titleFont = pygame.font.Font('Hack-Bold.ttf', 24) ### LOAD FONT
titleSurface = titleFont.render('Welcome to the Tetris!!', True, WHITE) ### Welcome to the Tetris!!

gameWindow = pygame.Surface((360, 600)) ### MAIN WINDOW FOR GAME
gameWindow.fill(BLACK)

background.blit(gameWindow, (0, 60))
background.blit(titleSurface, (20, 20))
screen.blit(background, (0, 0))
pygame.display.update()

colors = [0,0,0,0]
loadImages() ### load images of blocks. 0: Blue, 1: Red, 2: Yellow, 3: Green

screenArr = Screen(GRID_SIZE_X, GRID_SIZE_Y)

shapes = ['I', 'J', 'L', 'O', 'S', 'T', 'Z']
FIRSTLOCATION = (5, -4)

randomColor = random.randrange(4)
currentBlock = Block(randomColor, random.choice(shapes), FIRSTLOCATION)

while not LOSE:
    if not handleEvents(currentBlock, gameWindow):
        pygame.quit()
        exit(0)

    gameWindow.fill(BLACK)

    if currentBlock.move(screenArr, BLOCK_WIDTH, GRAVITY):
        randomColor = random.randrange(4)
        currentBlock = Block(randomColor, random.choice(shapes), FIRSTLOCATION)

        if currentBlock.move(screenArr, BLOCK_WIDTH, GRAVITY):
            LOSE = True

    screenArr.show(gameWindow, BLOCK_WIDTH, colors)
    background.blit(gameWindow, (0, 60))
    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit(0)
