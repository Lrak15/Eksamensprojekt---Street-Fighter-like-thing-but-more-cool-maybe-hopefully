import pygame
import time
from Player import PlayerClass
from Hitbox import HitClass
from Game_controls import HealthBarClass

pygame.mixer.pre_init(44100, -16, 6, 2048)
pygame.mixer.init()
pygame.init()

pygame.mixer_music.load("assets/lyd/SFX/Streetfighter.mp3")
pygame.mixer.music.set_volume(0.7)
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
fighter_one_sheet = pygame.image.load("assets/Billeder/Updated Sprite Sheet - Karl.png").convert_alpha()
fighter_two_sheet = pygame.image.load("assets/Billeder/Updated Sprite Sheet - Phillip.png").convert_alpha()

# define fighter variables
fighter_SIZE = 800

fighter_SCALE = gameWindowHeight / 2250
fighter_OFFSET = [gameWindowWidth / 5, gameWindowHeight / 20]
fighterOneStunTimes = [100, 100]
fighterTwoStunTimes = [100, 100]

fighterOneDATA = [fighter_SIZE, fighter_SCALE, fighter_OFFSET, fighterOneStunTimes]
fighterTwoDATA = [fighter_SIZE, fighter_SCALE, fighter_OFFSET, fighterTwoStunTimes]

# define number of steps in each animation
animation_steps = [3, 2, 2, 2, 3, 3, 3, 1, 1]

fighter_one_startPos = [gameWindowWidth / 10, 500]
fighter_two_startPos = [gameWindowWidth - (gameWindowWidth / 10 + gameWindowWidth / 20)]

# create two instances of the player class (1= karl 2= Phillip)
fighter_one = PlayerClass(1, screen, fighter_one_startPos[0], fighter_one_startPos[1], gameWindowWidth / 20, gameWindowHeight / 3, False, fighterOneDATA, fighter_one_sheet, animation_steps)
fighter_two = PlayerClass(2, screen, fighter_two_startPos[0], 700, gameWindowWidth / 20, gameWindowHeight / 3, False, fighterTwoDATA, fighter_two_sheet, animation_steps)

# create two instances of the health bar class
health_bars = HealthBarClass(gameWindowWidth, screen, 1)

# load background image
bg_img = pygame.transform.scale(pygame.image.load("assets/Billeder/street_fighter_background.png"), (gameWindowWidth, gameWindowHeight))

# Definening the hitbox for punch and kick attack.
hitbox_fighterOne = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)

hitbox_fighterTwo_punch = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)
hitbox_fighterTwo_kick = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)

'''Defining collisionchecker'''
def collision_checker(firstGameObject, secondGameObject):
    if firstGameObject.xPos + firstGameObject.width > secondGameObject.xPos and firstGameObject.xPos < secondGameObject.xPos + secondGameObject.width and firstGameObject.yPos + firstGameObject.height > secondGameObject.yPos and firstGameObject.yPos < secondGameObject.yPos + secondGameObject.height:
        return True
def hitbox_flipper(flip, hitbox_xPos, hitbox_offset):
    new_hitbox_offset = 0
    if flip:
        new_hitbox_offset -= (hitbox_xPos + hitbox_offset)
    else:
        return(hitbox_xPos)
    return(new_hitbox_offset)

'''Bruger funktioner til at checke om man tager damage '''
def take_damage(attacker, hitbox, whoOuch):
    lenght = len(attacker.animationList[attacker.action])
    lastElement = lenght - 1

    if collision_checker(hitbox, whoOuch) and attacker.frameIndex == lastElement:
        if attacker.punch and attacker == fighter_one:
            health_bars.player_two_health -= 2
            fighter_two.punched = True
            fighter_two.updateHurtTime = pygame.time.get_ticks()
            if health_bars.player_two_health > 127.5:
                health_bars.player_two_health2 += 2
            else:
                health_bars.player_two_health1 -= 2

        elif attacker.punch and attacker == fighter_two:
            health_bars.player_one_health -= 1
            fighter_one.punched = True
            fighter_one.updateHurtTime = pygame.time.get_ticks()
            if health_bars.player_one_health > 127.5:
                health_bars.player_one_health2 += 2
            else:
                health_bars.player_one_health1 -= 2

        elif attacker.kick and attacker == fighter_one:
            health_bars.player_two_health -= 2
            fighter_two.kicked = True
            fighter_two.updateHurtTime = pygame.time.get_ticks()
            if health_bars.player_two_health > 127.5:
                health_bars.player_two_health2 += 4
            else:
                health_bars.player_two_health1 -= 4

        elif attacker.kick and attacker == fighter_two:
            health_bars.player_one_health -= 2
            fighter_one.kicked = True
            fighter_one.updateHurtTime = pygame.time.get_ticks()
            if health_bars.player_one_health > 127.5:
                health_bars.player_one_health2 += 4
            else:
                health_bars.player_one_health1 -= 4

def hitbox_handler():
    hitbox_fighterOne_offset = hitbox_flipper(fighter_one.flip, gameWindowWidth / 18, gameWindowWidth / 32)
    hitbox_fighterOne.update(fighter_one.rect.centerx + hitbox_fighterOne_offset, fighter_one.yPos)

    hitbox_fighterTwo_punch_offset = hitbox_flipper(fighter_two.flip, -gameWindowWidth / 15, gameWindowWidth / 32)
    hitbox_fighterTwo_punch.update(fighter_two.rect.centerx + hitbox_fighterTwo_punch_offset, fighter_two.yPos + gameWindowHeight / 30)

    hitbox_fighterTwo_kick_offset = hitbox_flipper(fighter_two.flip, -gameWindowWidth / 9.5, gameWindowWidth / 32)
    hitbox_fighterTwo_kick.update(fighter_two.rect.centerx + hitbox_fighterTwo_kick_offset, fighter_two.yPos + gameWindowHeight / 8)

# Funktion der resetter "fighter" 1 og 2
def damage_handler():
    take_damage(fighter_one, hitbox_fighterOne, fighter_two)
    take_damage(fighter_two, hitbox_fighterTwo_punch, fighter_one)
    take_damage(fighter_two, hitbox_fighterTwo_kick, fighter_one)

    fighter_one.hurt_resetter()
    fighter_two.hurt_resetter()



running = True
while running:
    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        # QUIT GAME
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        elif event.type == pygame.QUIT:
            running = False

    # running functions for moving the fighters
    fighter_one.move(fighter_two)
    fighter_two.move(fighter_one)

    # running functions for updating the fighters positions
    fighter_one.update()
    fighter_two.update()

    # running functions for drawing the fighters
    fighter_one.draw()
    fighter_two.draw()

    # handling the positions of the hitboxes
    hitbox_handler()

    # applying damage
    damage_handler()

    health_bars.draw_health_bars(screen, health_bars.player_one_health, health_bars.player_two_health, gameWindowWidth, (100, 100, 100), (50, 50, 50), (0, 0, 0), (health_bars.player_one_health2, health_bars.player_one_health1, 0), (health_bars.player_two_health2, health_bars.player_two_health1, 0), int(gameWindowWidth / 50), int(gameWindowWidth / 200), int(gameWindowWidth / 3), 45)

    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
