import pygame
import time

from Player import PlayerClass
from Hitbox import HitClass

pygame.init()

#set up the drawing window
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")
print(gameWindowWidth, gameWindowHeight)

#set framerate
clock = pygame.time.Clock()
FPS = 60

#create two instances of the player class
fighter_one = PlayerClass(screen, 101, 500, 103, 200)
fighter_two = PlayerClass(screen, 101, 102, 103, 200)

#create instances of the hitbox class
hitbox_fighterTwo_punch = HitClass(screen, 0, 0, 100, 20)

#load background image
bg_img = pygame.image.load("assets/Billeder/Holstebro.jpg")

def collisionChecker(firstGameObject, secondGameObject):
    if firstGameObject.xPos + firstGameObject.width > secondGameObject.xPos and firstGameObject.xPos < secondGameObject.xPos + secondGameObject.width and firstGameObject.yPos + firstGameObject.height > secondGameObject.yPos and firstGameObject.yPos < secondGameObject.yPos + secondGameObject.height:
        return True


running = True
while running:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        #QUIT GAME
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False



        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                fighter_one.moveX += fighter_one.vel
            if event.key == pygame.K_LEFT:
                fighter_one.moveX -= fighter_one.vel
            if event.key == pygame.K_DOWN:
                fighter_one.duck()
            if event.key == pygame.K_UP:
                if fighter_one.yPos == gameWindowHeight - fighter_one.height:
                    fighter_one.moveY = 20

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                fighter_one.moveX -= fighter_one.vel
            if event.key == pygame.K_LEFT:
                fighter_one.moveX += fighter_one.vel
            if event.key == pygame.K_DOWN:
                fighter_one.height += fighter_one.height


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                fighter_two.moveX += fighter_two.vel
            if event.key == pygame.K_a:
                fighter_two.moveX -= fighter_two.vel
            if event.key == pygame.K_s:
                fighter_two.moveY += fighter_two.vel
            if event.key == pygame.K_w:
                if fighter_two.yPos == gameWindowHeight - fighter_two.height:
                    fighter_two.moveY = 20
            if event.key == pygame.K_SPACE:
                fighter_two.punch_width = 200

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                fighter_two.moveX -= fighter_two.vel
            if event.key == pygame.K_a:
                fighter_two.moveX += fighter_two.vel
            if event.key == pygame.K_s:
                fighter_two.moveY -= fighter_two.vel
            if event.key == pygame.K_w:
                fighter_two.moveY += fighter_two.vel
            if event.key == pygame.K_SPACE:
                fighter_two.punch_width = 0
            """

    """
    if collisionChecker(hitbox_fighterTwo_punch, fighter_one):
        fighter_one.color = (255, 0, 0)
    else:
        fighter_one.color = (1, 1, 1)
    """

    fighter_one.move()
    fighter_one.draw()


    """
    fighter_one.gravity()
    fighter_one.update()
    

    fighter_two.gravity()
    fighter_two.update()
    fighter_two.draw()
    """

    hitbox_fighterTwo_punch.update(fighter_two.xPos+100, fighter_two.yPos + fighter_two.height/2)
    hitbox_fighterTwo_punch.draw()
# Define health bar colors
    health_bar_background_color = (100, 100, 100)
    health_bar_outline_color = (0, 0, 0)
    health_bar_red_color = (255, 0, 0)
    health_bar_green_color = (0, 255, 0)

# Define screen spacings and lengths
    screen_spacing_1 = int(gameWindowWidth/50)
    screen_spacing_2 = int(gameWindowWidth/200)
    health_bar_length = int(gameWindowWidth/3)

# Draw player 1 health bar
    pygame.draw.rect(screen, health_bar_background_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9*screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9*screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_red_color, pygame.Rect(screen_spacing_1 + 2*screen_spacing_2, screen_spacing_1 + 2*screen_spacing_2, health_bar_length - 4*screen_spacing_2, 5*screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(screen_spacing_1 + 2*screen_spacing_2, screen_spacing_1 + 2*screen_spacing_2, health_bar_length - 4*screen_spacing_2, 5*screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_green_color, pygame.Rect(screen_spacing_1 + 3*screen_spacing_2, screen_spacing_1 + 3*screen_spacing_2, 300, 3*screen_spacing_2))

# Draw player 2 health bar
    pygame.draw.rect(screen, health_bar_background_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9*screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_red_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1 + 2*screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_green_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1 + 3*screen_spacing_2, screen_spacing_1 + 3 * screen_spacing_2, 300, 3 * screen_spacing_2))

    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
