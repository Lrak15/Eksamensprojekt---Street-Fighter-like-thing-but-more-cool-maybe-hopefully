import pygame

class HitClass:
# Defining x og y positionen og farveeeee
    def __init__(self, screen, width, height):
        self.screen = screen
        self.xPos = 0
        self.yPos = 0
        self.width = width
        self.height = height
        self.color = (1, 255, 1)

    def update(self, newxPos, newyPos):
        self.xPos = newxPos
        self.yPos = newyPos

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height), 3, 1)
