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

LOSE = False

pygame.init()

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True

def loadImages():
    blockTypes[0] = pygame.image.load('Block1.png')
    blockTypes[1] = pygame.image.load('Block2.png')
    blockTypes[2] = pygame.image.load('Block3.png')
    blockTypes[3] = pygame.image.load('Block4.png')

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

blockTypes = [0,0,0,0]
loadImages() ### load images of blocks. 0: Blue, 1: Red, 2: Yellow, 3: Green

block1 = Block(blockTypes[0], 'I', (180, 0))
block2 = Block(blockTypes[1], 'J', (120, 120))
block3 = Block(blockTypes[2], 'L', (240, 300))
block4 = Block(blockTypes[3], 'O', (60, 420))

testBlocks = [block1, block2, block3, block4]
screenArray = [[0 for col in range(12)] for row in range(20)]

while not LOSE:
    gameWindow.fill(BLACK)

    for block in testBlocks:
        block.show(gameWindow, BLOCK_WIDTH)
        block.move(screenArray, BLOCK_WIDTH)

    background.blit(gameWindow, (0, 60))
    screen.blit(background, (0, 0))

    pygame.display.update()
    clock.tick(FPS)

    if not handleEvents():
        pygame.quit()
        exit(0)
