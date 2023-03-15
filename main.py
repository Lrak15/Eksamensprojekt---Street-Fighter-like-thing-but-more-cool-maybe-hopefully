import pygame
import math
pygame.init()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set up the drawing window
screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")
print(gameWindowWidth, gameWindowHeight)

from Player import PlayerClass

fighter_one = PlayerClass(screen, 101, 102, 103, 200, 1)
fighter_two = PlayerClass(screen, 101, 102, 103, 200, 1)

running = True
while running:
    screen.fill((4, 73, 96))

    for event in pygame.event.get():
        #QUIT GAME
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fighter_one.moveX += fighter_one.vel
            if event.key == pygame.K_LEFT:
                fighter_one.moveX -= fighter_one.vel
            if event.key == pygame.K_DOWN:
                fighter_one.moveY += fighter_one.vel
            if event.key == pygame.K_UP:
                fighter_one.moveY -= fighter_one.vel

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                fighter_one.moveX -= fighter_one.vel
            if event.key == pygame.K_LEFT:
                fighter_one.moveX += fighter_one.vel
            if event.key == pygame.K_DOWN:
                fighter_one.moveY -= fighter_one.vel
            if event.key == pygame.K_UP:
                fighter_one.moveY += fighter_one.vel


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                fighter_two.moveX += fighter_two.vel
            if event.key == pygame.K_a:
                fighter_two.moveX -= fighter_two.vel
            if event.key == pygame.K_s:
                fighter_two.moveY += fighter_two.vel
            if event.key == pygame.K_w:
                fighter_two.moveY -= fighter_two.vel

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                fighter_two.moveX -= fighter_two.vel
            if event.key == pygame.K_a:
                fighter_two.moveX += fighter_two.vel
            if event.key == pygame.K_s:
                fighter_two.moveY -= fighter_two.vel
            if event.key == pygame.K_w:
                fighter_two.moveY += fighter_two.vel

    fighter_one.update()
    fighter_one.draw()

    fighter_two.update()
    fighter_two.draw()
    pygame.display.update()
