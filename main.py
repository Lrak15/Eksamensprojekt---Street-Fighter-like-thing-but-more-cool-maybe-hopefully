import pygame
import time
from Player import PlayerClass
from Hitbox import HitClass
from Game_controls import GameControlClass
from Game_controls import draw_health_bars
from Game_controls import draw_skillpoint_upgrade


pygame.mixer.pre_init(44100, -16, 6, 2048)
pygame.init()



# set up the drawing window
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")
print(gameWindowWidth, gameWindowHeight)

# set framerate
clock = pygame.time.Clock()
FPS = 60

draw_skillpoint_upgrade(screen, gameWindowWidth)

# create two instances of the player class
fighter_one = PlayerClass(1, screen, 101, 500, 100, 200)
fighter_two = PlayerClass(2, screen, 1000, 700, 100, 200)

# create instances of the hitbox class
hitbox_fighterTwo_punch = HitClass(screen, 0, 0, 100, 20)

# load background image
bg_img = pygame.image.load("assets/Billeder/Holstebro.jpg")


def collisionChecker(firstGameObject, secondGameObject):
    if firstGameObject.xPos + firstGameObject.width > secondGameObject.xPos and firstGameObject.xPos < secondGameObject.xPos + secondGameObject.width and firstGameObject.yPos + firstGameObject.height > secondGameObject.yPos and firstGameObject.yPos < secondGameObject.yPos + secondGameObject.height:
        return True


running = True
while running:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        # QUIT GAME
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_h:

                player_1_health_upgrade += 1
                player_1_strength_upgrade += 1
                player_1_speed_upgrade += 1
                player_1_knockback_upgrade += 1
                player_1_stamina_upgrade += 1

                health -= 15
                if health > 127.5:
                    health2 += 30
                else:
                    health1 -= 30
                    if health < 30:
                        health1 = 255

        elif event.type == pygame.QUIT:
            running = False

    """
    if collisionChecker(hitbox_fighterTwo_punch, fighter_one):
        fighter_one.color = (255, 0, 0)
    else:
        fighter_one.color = (1, 1, 1)
    """

    fighter_one.move()
    fighter_one.draw()

    fighter_two.draw()


    """
    fighter_one.gravity()
    fighter_one.update()
    

    fighter_two.gravity()
    fighter_two.update()
    fighter_two.draw()
    """

    hitbox_fighterTwo_punch.update(fighter_two.xPos+100, fighter_two.yPos + fighter_two.height/2)
    hitbox_fighterTwo_punch.draw()

    draw_health_bars(screen, gameWindowWidth)

    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
