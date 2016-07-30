import sys, os, math, random
import pygame
from pygame.locals import *
from blockRotation import *

pygame.init()

class Block:
    def __init__(self, color, shape, location):
        self.color = color
        self.location = location
        self.static = False
        self.STATE = 0
        self.SHAPE = shape

        self.blockArr = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]

        self.blockArr = rotateBlock(shape, self.STATE)

    def move(self, screenArr, BLOCK_WIDTH, DIRECTION):
        if self.static:
            return True

        x, y = self.location
        dx, dy = DIRECTION

        ### remove the block in screenArr
        for i in range(4):
            if (y + i) >= screenArr.getHEIGHT():
                break
            if (y + i) < 0:
                continue
            for j in range(4):
                if (x + j) < 0 or (x + j) >= screenArr.getWIDTH():
                    continue
                if self.blockArr[i][j] > 0:
                    screenArr.write(x + j, y + i, -1)

        ### check if block is fit for new location. if it doesn't fit, self.static == True
        for i in range(4):
            if (y + i + dy) < 0:
                continue
            for j in range(4):
                if (y + i + dy) >= screenArr.getHEIGHT() or (x + j + dx) >= screenArr.getWIDTH() or (x + j + dx) < 0:
                    if self.blockArr[i][j] == 0:
                        continue
                    else:
                        self.static = True
                        break

                if screenArr.getXY(x + j + dx, y + i + dy) >= 0 and self.blockArr[i][j] > 0:
                    self.static = True
                    break

            if self.static:
                break

        ### if block fits for new location, update location
        if not self.static:
            x += dx
            y += dy
            self.location = (x, y)
            print 'loc: ' + str(self.location)

        ### write new location
        for i in range(4):
            if (y + i) < 0:
                continue
            if (y + i) >= screenArr.getHEIGHT():
                break
            for j in range(4):

                if (x + j) < 0 or (x + j) >= screenArr.getWIDTH():
                    continue
                if self.blockArr[i][j] > 0:
                    screenArr.write(x + j, y + i, self.color)

        ### prevent block stopping when there's no place to move in X direction
        if DIRECTION != (0, 1):
            self.static = False
            return False

        if self.static:
            return True
        else:
            return False

    def moveDown(self, screen, screenArr, BLOCK_WIDTH, GRAVITY):
        while True:
            if self.move(screenArr, BLOCK_WIDTH, GRAVITY):
                return

    def rotate(self, screenArr, BLOCK_WIDTH):
        tempArr = rotateBlock(self.SHAPE, (self.STATE + 1) % 4)

        x, y = self.location

        for i in range(4):
            if (y + i) < 0 or (y + i) >= screenArr.getHEIGHT():
                continue
            for j in range(4):
                if (x + j) < 0 or (x + j) >= screenArr.getWIDTH():
                    continue
                if self.blockArr[i][j] > 0:
                    screenArr.write(x + j, y + i, -1)

        for i in range(4):
            if (y + i) < 0 or (y + i) >= screenArr.getHEIGHT():
                continue
            for j in range(4):
                if (x + j) < 0 or (x + j) >= screenArr.getWIDTH():
                    continue
                if tempArr[i][j] > 0 and screenArr.getXY(x + j, y + i) >= 0:
                    return

        for i in range(4):
            if (y + i) < 0 or (y + i) >= screenArr.getHEIGHT():
                continue
            for j in range(4):
                if (x + j) < 0 or (x + j) >= screenArr.getWIDTH():
                    continue
                if tempArr[i][j] > 0:
                    screenArr.write(x + j, y + i, color)

        self.blockArr = tempArr
        self.STATE += 1
        self.STATE %= 4

    def getY(self):
        return self.location[1]


class Screen:
    def __init__(self, X, Y):
        self.arr = [[-1 for col in range(X)] for row in range(Y)]
        self.WIDTH = X
        self.HEIGHT = Y

    def write(self, x, y, color):
        self.arr[y][x] = color

    def getXY(self, x, y):
        return self.arr[y][x]

    def show(self, screen, BLOCK_WIDTH, images):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.arr[i][j] < 0:
                    continue

                y = i * BLOCK_WIDTH
                x = j * BLOCK_WIDTH

                screen.blit(images[self.arr[i][j]], (x, y))

    def lineClear(self, lineIdx):
        if lineIdx >= self.HEIGHT:
            return
        for X in range(self.WIDTH):
            if self.arr[lineIdx][X] < 0:
                return

        tempArr = [[-1 for col in range(self.WIDTH)] for row in range(self.HEIGHT)]
        for i in range(lineIdx + 1, self.HEIGHT):
            for j in range(self.WIDTH):
                tempArr[i][j] = self.arr[i][j]
        for i in range(lineIdx):
            for j in range(self.WIDTH):
                tempArr[i + 1][j] = self.arr[i][j]

        self.arr = tempArr

    def getWIDTH(self):
        return self.WIDTH
    def getHEIGHT(self):
        return self.HEIGHT
