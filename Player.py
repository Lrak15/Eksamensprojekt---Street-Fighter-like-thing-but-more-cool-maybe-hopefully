import pygame


class PlayerClass:
    xPos = 0
    yPos = 0
    width = 0
    height = 0
    vel = 0
    color = (1, 1, 1)
    moveX = 0
    moveY = 0

    def __init__(self, screen, x, y, width, height, vel):
        self.screen = screen
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        self.vel = vel
        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]

    def update(self):
        self.xPos = self.xPos + self.moveX
        self.yPos = self.yPos + self.moveY

        if self.width + self.xPos > self.screenWidth:
            self.xPos = self.screenWidth - self.width
        if self.xPos < 0:
            self.xPos = 0
        if self.yPos + self.height > self.screenHeight:
            self.yPos = self.screenHeight - self.height
        if self.yPos < 0:
            self.yPos = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height))
