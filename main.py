# Import all the important libraries and classes from external documents.
import pygame
from Player import PlayerClass
from Hitbox import HitClass
from Game_controls import HealthBarClass
from Game_controls import SkillpointUpgradeClass

# Initiate pygame and pygames built in mixer.
pygame.mixer.pre_init(44100, -16, 6, 2048)
pygame.mixer.init()
pygame.init()

# Load background music.
pygame.mixer_music.load("assets/lyd/SFX/Streetfighter.mp3")
pygame.mixer.music.set_volume(50)
pygame.mixer_music.play(loops=-1)

# Set up the drawing window.
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")

# Set framerate.
clock = pygame.time.Clock()
FPS = 60

# Load fighter spritesheets.
fighterOneSheet = pygame.image.load("assets/Billeder/Updated Sprite Sheet - Karl.png").convert_alpha()
fighterTwoSheet = pygame.image.load("assets/Billeder/Updated Sprite Sheet - Phillip.png").convert_alpha()

# Define fighter variables.
fighterSIZE = 800
fighterSCALE = gameWindowHeight / 2250
fighterOFFSET = [gameWindowWidth / 5, gameWindowHeight / 20]
fighterOneStunTimes = [100, 100]
fighterTwoStunTimes = [100, 100]

# Collect the fighter variables into a list for each fighter.
fighterOneDATA = [fighterSIZE, fighterSCALE, fighterOFFSET, fighterOneStunTimes]
fighterTwoDATA = [fighterSIZE, fighterSCALE, fighterOFFSET, fighterTwoStunTimes]

# Define number of steps in each animation.
animationSteps = [3, 2, 2, 2, 3, 3, 3, 1, 1]

# Define the startpositions of each fighter.
fighterOneStartPos = [gameWindowWidth / 10, 0]
fighterTwoStartPos = [gameWindowWidth - (gameWindowWidth / 10 + gameWindowWidth / 20), 0]

# Create two instances of the player class (1= Karl, 2= Phillip).
fighterOne = PlayerClass(1, screen, fighterOneStartPos[0], fighterTwoStartPos[1], gameWindowWidth / 20, gameWindowHeight / 3, False, fighterOneDATA, fighterOneSheet, animationSteps)
fighterTwo = PlayerClass(2, screen, fighterTwoStartPos[0], fighterTwoStartPos[1], gameWindowWidth / 20, gameWindowHeight / 3, False, fighterTwoDATA, fighterTwoSheet, animationSteps)

# Create an instances of the health bar class.
health_bars = HealthBarClass(gameWindowWidth, screen, 1)

# Create an instances of the skill point upgrade class.
skill_point_upgrade = SkillpointUpgradeClass(gameWindowWidth, screen)

# Load background image.
bgImg = pygame.transform.scale(pygame.image.load("assets/Billeder/street_fighter_background.png"), (gameWindowWidth, gameWindowHeight))

# Create three instances of the hitbox class. One for each of fighter twos moves but only one for fighter one since
# their moves hit in the same place.
hitboxFighterOne = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)
hitboxFighterTwoPunch = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)
hitboxFighterTwoKick = HitClass(screen, gameWindowWidth / 23, gameWindowWidth / 23)


# Defining the function that is able to check for collisions between two objects.
def collision_checker(firstGameobject, secondGameobject):
    if firstGameobject.xPos + firstGameobject.width > secondGameobject.xPos and firstGameobject.xPos < secondGameobject.xPos + secondGameobject.width and firstGameobject.yPos + firstGameobject.height > secondGameobject.yPos and firstGameobject.yPos < secondGameobject.yPos + secondGameobject.height:
        return True


# Function for flipping hitboxes depending on what way the players are facing.
def hitbox_flipper(flip, hitboxXPos, hitboxOffset):
    newHitboxOffset = 0
    if flip:
        newHitboxOffset -= (hitboxXPos + hitboxOffset)
    else:
        return hitboxXPos
    return newHitboxOffset


# Creating a function for checking whether a player is taking damage and what attack they're being hit by.
def take_damage(attacker, hitbox, whoOuch):
    lenght = len(attacker.animationList[attacker.action])
    lastElement = lenght - 1

    if collision_checker(hitbox, whoOuch) and attacker.frameIndex == lastElement:
        if attacker.punch and attacker == fighterOne:
            fighterTwo.punched = True
            fighterTwo.updateHurtTime = pygame.time.get_ticks()
            health_bars.player_two_punched(fighterTwo.blocking)

        elif attacker.punch and attacker == fighterTwo:
            fighterOne.punched = True
            fighterOne.updateHurtTime = pygame.time.get_ticks()
            health_bars.player_one_punched(fighterOne.blocking)

        elif attacker.kick and attacker == fighterOne:
            fighterTwo.kicked = True
            fighterTwo.updateHurtTime = pygame.time.get_ticks()
            health_bars.player_two_kicked(fighterTwo.blocking)

        elif attacker.kick and attacker == fighterTwo:
            fighterOne.kicked = True
            fighterOne.updateHurtTime = pygame.time.get_ticks()
            health_bars.player_one_kicked(fighterOne.blocking)


# Collecting all the different functions being run in order to control the hixboxes into one.
# Makes sure that the hitboxes follow the player when moving.
def hitbox_handler():
    hitboxFighterOneOffset = hitbox_flipper(fighterOne.flip, gameWindowWidth / 18, gameWindowWidth / 32)
    hitboxFighterOne.update(fighterOne.rect.centerx + hitboxFighterOneOffset, fighterOne.yPos)

    hitboxFighterTwoPunchOffset = hitbox_flipper(fighterTwo.flip, -gameWindowWidth / 15, gameWindowWidth / 32)
    hitboxFighterTwoPunch.update(fighterTwo.rect.centerx + hitboxFighterTwoPunchOffset, fighterTwo.yPos + gameWindowHeight / 30)

    hitboxFighterTwoKickOffset = hitbox_flipper(fighterTwo.flip, -gameWindowWidth / 9.5, gameWindowWidth / 32)
    hitboxFighterTwoKick.update(fighterTwo.rect.centerx + hitboxFighterTwoKickOffset, fighterTwo.yPos + gameWindowHeight / 8)


# Collective function that takes care of the different take_damage functions between the different fighters and
# hitboxes. Also makes sure that the fighters hurt_resetter function have been started, so they won't be frozen forever.
def damage_handler():
    take_damage(fighterOne, hitboxFighterOne, fighterTwo)
    take_damage(fighterTwo, hitboxFighterTwoPunch, fighterOne)
    take_damage(fighterTwo, hitboxFighterTwoKick, fighterOne)

    fighterOne.hurt_resetter()
    fighterTwo.hurt_resetter()


# The main loop. Only runs when 'running' is true.
running = True
while running:
    # Sets the tickrate to 60 FPS and draws our background image.
    clock.tick(FPS)
    screen.blit(bgImg, (0, 0))

    # Listen for key events to QUIT the game and close upgrading screen.
    for event in pygame.event.get():
        # QUIT GAME
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                skill_point_upgrade.still_upgrading = False
        elif event.type == pygame.QUIT:
            running = False

    # Running functions for moving the fighters.
    fighterOne.move(fighterTwo)
    fighterTwo.move(fighterOne)

    # Running functions for updating the fighters positions.
    fighterOne.update()
    fighterTwo.update()

    # Running functions for drawing the fighters.
    fighterOne.draw()
    fighterTwo.draw()

    # Handling the positions of the hitboxes.
    hitbox_handler()

    # Applying damage.
    damage_handler()

    # Draw/update health bars
    health_bars.draw_health_bars(screen, health_bars.player_one_health, health_bars.player_two_health, gameWindowWidth, (100, 100, 100), (50, 50, 50), (0, 0, 0), (health_bars.player_one_health2, health_bars.player_one_health1, 0), (health_bars.player_two_health2, health_bars.player_two_health1, 0), int(gameWindowWidth / 50), int(gameWindowWidth / 200), int(gameWindowWidth / 3), 45)

    # Draw/update skill point upgrade screen
    skill_point_upgrade.draw_skillpoint_upgrade(screen, skill_point_upgrade.player_1_health_upgrade, skill_point_upgrade.player_1_strength_upgrade, skill_point_upgrade.player_1_speed_upgrade, skill_point_upgrade.player_1_knockback_upgrade, skill_point_upgrade.player_1_stamina_upgrade, skill_point_upgrade.player_2_health_upgrade, skill_point_upgrade.player_2_strength_upgrade, skill_point_upgrade.player_2_speed_upgrade, skill_point_upgrade.player_2_knockback_upgrade, skill_point_upgrade.player_2_stamina_upgrade, gameWindowWidth, health_bars.background_color, health_bars.outline_color, health_bars.black_color, int(gameWindowWidth / 50), int(gameWindowWidth / 200))

    # Pushes the drawings to the screen, so they can be shown.
    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
