import pygame
import time
from Player import PlayerClass
from Hitbox import HitClass
from Game_controls import HealthBarClass

pygame.mixer.pre_init(44100, -16, 6, 2048)
pygame.init()



#set up the drawing window
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")
print(gameWindowWidth, gameWindowHeight)

#set framerate
clock = pygame.time.Clock()
FPS = 60

#load fighter spritesheets
fighter_one_sheet = pygame.image.load("assets/Billeder/ANIMATIONER - ÅRSPRØVE.png").convert_alpha()
fighter_two_sheet = pygame.image.load("assets/Billeder/ANIMATIONER - ÅRSPRØVE.png").convert_alpha()

#define fighter variables
fighter_SIZE = 800

fighter_one_SCALE = 0.25
fighter_one_OFFSET = [72, 56]
fighter_one_DATA = [fighter_SIZE, fighter_one_SCALE, fighter_one_OFFSET]
fighter_two_SCALE = 3
fighter_two_OFFSET = [112, 107]
fighter_two_DATA = [fighter_SIZE, fighter_two_SCALE, fighter_two_OFFSET]

#define number of steps in each animation
animation_steps = [3, 2, 2, 2, 3, 3, 3, 1]


#create two instances of the player class
fighter_one = PlayerClass(1, screen, 101, 500, 100, 200, False, fighter_one_DATA, fighter_one_sheet, animation_steps)
fighter_two = PlayerClass(2, screen, 1000, 700, 100, 200, True, fighter_two_DATA, fighter_two_sheet, animation_steps)

#create instances of the hitbox class
hitbox_fighterTwo_punch = HitClass(screen, 0, 0, 100, 20)

# create two instances of the health bar class
fighter_one_health_bar = HealthBarClass(gameWindowWidth, screen, 1)
fighter_two_health_bar = HealthBarClass(gameWindowWidth, screen, 1)

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

    """
    if collisionChecker(hitbox_fighterTwo_punch, fighter_one):
        fighter_one.color = (255, 0, 0)
    else:
        fighter_one.color = (1, 1, 1)
    """

    fighter_one.move(fighter_two)
    fighter_one.update()

    fighter_one.draw()
    fighter_two.draw()


    """
    fighter_one.gravity()
    fighter_one.update()
    

    fighter_two.gravity()
    fighter_two.update()
    fighter_two.draw()
    """

    #hitbox_fighterTwo_punch.update(fighter_two.xPos+100, fighter_two.yPos + fighter_two.height/2)
    #hitbox_fighterTwo_punch.draw()

    fighter_one_health_bar.draw_health_bars(screen, 100, 1920, (20, 20, 20), (30, 30, 30), (0, 0, 0), (255, 160, 12), 30, 25, 120, 45)

    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
