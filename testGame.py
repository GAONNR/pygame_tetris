import pygame
from pygame.locals import *

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

FPS = 30
clock = pygame.time.Clock()

player = pygame.image.load('player_test.png')
playerX = 0

while True:
    screen.fill((255, 255, 255))
    screen.blit(player, (playerX, 200))

    playerX += 10
    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:  ## also pygame.QUIT
            pygame.quit()
            exit(0)
