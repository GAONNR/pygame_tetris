import pygame
from pygame.locals import *

pygame.init()

class Bird:
    def __init__(self, imageName, location, spd):
        self.imageName = imageName
        self.location = location
        self.spd = spd

        self.image = pygame.image.load(imageName)

    def move(self):
        X, Y = self.location
        X += self.spd
        self.location = (X, Y)

    def show(self):
        screen.blit(self.image, self.location)
        self.move()


width, height = 640, 480
screen = pygame.display.set_mode((width, height))

bird1 = Bird('bird1.png', (0, 50), 10)
bird2 = Bird('bird2.png', (100, 150), 25)
bird3 = Bird('bird3.png', (50, 250), 15)

birds = [bird1, bird2, bird3]

FPS = 30
clock = pygame.time.Clock()

while True:
    screen.fill((255, 255, 255))

    for bird in birds:
        bird.show()

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:  ## also pygame.QUIT
            pygame.quit()
            exit(0)
