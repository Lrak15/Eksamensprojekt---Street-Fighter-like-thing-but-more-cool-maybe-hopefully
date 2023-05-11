import pygame

class HitClass:
    newxPos = 0
    newyPos = 0

    def __init__(self, screen, x, y, width, height):
        self.screen = screen
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        self.color = (1, 255, 1)

    def update(self, newxPos, newyPos):
        self.xPos = newxPos
        self.yPos = newyPos

    def draw(self, ):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height), 3, 1)
