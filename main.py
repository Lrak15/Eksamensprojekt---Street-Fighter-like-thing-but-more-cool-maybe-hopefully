import pygame
import time
from Player import PlayerClass
from Hitbox import HitClass
from Game_controls import HealthBarClass

pygame.mixer.pre_init(44100, -16, 6, 2048)
pygame.init()

pygame.mixer_music.load("assets/lyd/SFX/Streetfighter.mp3")
pygame.mixer_music.play(loops=-1)


#set up the drawing window
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")
print(gameWindowWidth, gameWindowHeight)

#set framerate
clock = pygame.time.Clock()
FPS = 60

#load fighter spritesheets
fighter_one_sheet = pygame.image.load("assets/Billeder/Sprite Sheet - Karl.png").convert_alpha()
fighter_two_sheet = pygame.image.load("assets/Billeder/Sprite Sheet - Phillip.png").convert_alpha()

# define fighter variables
fighter_SIZE = 800

fighter_SCALE = gameWindowHeight / 2250
fighter_OFFSET = [gameWindowWidth / 5, gameWindowHeight / 20]
fighter_DATA = [fighter_SIZE, fighter_SCALE, fighter_OFFSET]

# define number of steps in each animation
animation_steps = [3, 2, 2, 2, 3, 3, 3, 1]

fighter_one_startPos = [gameWindowWidth / 10, 500]
fighter_two_startPos = [gameWindowWidth - (gameWindowWidth / 10 + gameWindowWidth / 20)]

# create two instances of the player class
fighter_one = PlayerClass(1, screen, fighter_one_startPos[0], fighter_one_startPos[1], gameWindowWidth / 20, gameWindowHeight / 3, False, fighter_DATA, fighter_one_sheet, animation_steps)
fighter_two = PlayerClass(2, screen, fighter_two_startPos[0], 700, gameWindowWidth / 20, gameWindowHeight / 3, False, fighter_DATA, fighter_two_sheet, animation_steps)

# create two instances of the health bar class
health_bars = HealthBarClass(gameWindowWidth, screen, 1)

# load background image
bg_img = pygame.transform.scale(pygame.image.load("assets/Billeder/street_fighter_background.png"), (gameWindowWidth, gameWindowHeight))

#hitbox_fighterOne_punch = HitClass(screen, gameWindowWidth / 25, gameWindowWidth / 25)
hitbox_fighterOne_kick = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)

# hitbox_fighterTwo_punch = HitClass(screen, gameWindowWidth / 25, gameWindowWidth / 25)
# hitbox_fighterTwo_kick = HitClass(screen, gameWindowWidth / 25, gameWindowWidth / 25)
hitboxes = [hitbox_fighterOne_kick]

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


    fighter_one.move(fighter_two)
    fighter_two.move(fighter_two)

    fighter_one.update()
    fighter_two.update()



    fighter_one.draw()
    fighter_two.draw()



    hitbox_fighterOne_kick.update(fighter_one.xPos + gameWindowWidth / 12, fighter_one.yPos)


    if fighter_one.attacking:
        if fighter_one.kick and fighter_one.frame_index == 2:
            hitbox_fighterOne_kick.draw()
            if collisionChecker(hitbox_fighterOne_kick, fighter_two):
                fighter_two.color = (1, 255, 1)
                health_bars.player_two_health -= 1
                if health_bars.player_two_health > 127.5:
                    health_bars.player_two_health2 += 2
                else:
                    health_bars.player_two_health1 -= 2
        else:
            fighter_two.color = (255, 1, 1)


    """
    fighter_one.gravity()
    fighter_one.update()
    
    
    fighter_two.gravity()
    fighter_two.update()
    fighter_two.draw()
    """

    #hitbox_fighterTwo_punch.update(fighter_two.xPos+100, fighter_two.yPos + fighter_two.height/2)
    #hitbox_fighterTwo_punch.draw()

    health_bars.draw_health_bars(screen, health_bars.player_one_health, health_bars.player_two_health, gameWindowWidth, (100, 100, 100), (50, 50, 50), (0, 0, 0), (health_bars.player_one_health2, health_bars.player_one_health1, 0), (health_bars.player_two_health2, health_bars.player_two_health1, 0), int(gameWindowWidth / 50), int(gameWindowWidth / 200), int(gameWindowWidth / 3), 45)

    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
