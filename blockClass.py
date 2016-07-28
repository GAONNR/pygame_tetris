import sys, os, math, random
import pygame
from pygame.locals import *

pygame.init()

class Block:
    def __init__(self, color, shape, location):
        self.image = color
        self.location = location
        self.static = False
        self.leftBlocks = 4

        self.blockArray = [[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]]

        if shape == 'I':
            self.blockArray[0][1] = 1    ###   X
            self.blockArray[1][1] = 1    ###   X
            self.blockArray[2][1] = 1    ###   X
            self.blockArray[3][1] = 1    ###   X
        elif shape == 'J':
            self.blockArray[0][1] = 1    ###   X
            self.blockArray[1][1] = 1    ###   X
            self.blockArray[2][0] = 1    ###  XX
            self.blockArray[2][1] = 1    ###
        elif shape == 'L':
            self.blockArray[0][1] = 1    ###   X
            self.blockArray[1][1] = 1    ###   X
            self.blockArray[2][1] = 1    ###   XX
            self.blockArray[2][2] = 1    ###
        elif shape == 'O':
            self.blockArray[0][1] = 1    ###   XX
            self.blockArray[0][2] = 1    ###   XX
            self.blockArray[1][1] = 1    ###
            self.blockArray[1][2] = 1    ###
        elif shape == 'S':
            self.blockArray[0][1] = 1    ###   XX
            self.blockArray[0][2] = 1    ###  XX
            self.blockArray[1][0] = 1    ###
            self.blockArray[1][1] = 1    ###
        elif shape == 'T':
            self.blockArray[0][0] = 1    ###  XTX
            self.blockArray[0][1] = 1    ###   X
            self.blockArray[0][2] = 1    ###
            self.blockArray[1][1] = 1    ###
        else: ###     'Z':
            self.blockArray[0][0] = 1    ###  XX
            self.blockArray[0][1] = 1    ###   XX
            self.blockArray[1][1] = 1    ###
            self.blockArray[1][2] = 1    ###

    def show(self, screen, BLOCK_WIDTH):
        for i in range(4):
            for j in range(4):
                if self.blockArray[i][j] > 0:
                    x, y = self.location
                    x += j * BLOCK_WIDTH
                    y += i * BLOCK_WIDTH

                    screen.blit(self.image, (x, y))

    def move(self, screenArray, BLOCK_WIDTH):
        if self.static:
            return False

        x, y = self.location
        arrayLocation = (x / BLOCK_WIDTH, y / BLOCK_WIDTH)

        ### remove the block
        for i in range(4):
            if (arrayLocation[1] + i) >= len(screenArray):
                break
            for j in range(4):
                x, y = arrayLocation
                if self.blockArray[i][j] > 0:
                    screenArray[y + i][x + j] = 0

        ### check if block is fit for new location. if it doesn't fit, self.static == True
        for i in range(4):
            for j in range(4):
                x, y = arrayLocation

                if (y + i + 1) >= len(screenArray) or (x + j) >= len(screenArray[0]):
                    if self.blockArray[i][j] == 0:
                        continue
                    else:
                        self.static = True
                        break

                if screenArray[y + i + 1][x + j] > 0 and self.blockArray[i][j] > 0:
                    self.static = True
                    break

            if self.static:
                break

        ### if block fits for new location, update location
        if not self.static:
            x, y = arrayLocation
            y += 1
            arrayLocation = (x, y)
            self.location = (x * BLOCK_WIDTH, y * BLOCK_WIDTH)
            print 'loc: ' + str(arrayLocation)

        ### write new location
        for i in range(4):
            if (arrayLocation[1] + i) >= len(screenArray):
                break
            for j in range(4):
                x, y = arrayLocation
                screenArray[y + i][x + j] += self.blockArray[i][j]

        if self.static:
            return True
        else:
            return False

    def isDead(self):
        if self.leftBlocks == 0:
            return True
        else:
            return False
