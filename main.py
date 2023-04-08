import pygame
import time
from Player import PlayerClass
from Hitbox import HitClass

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
fighter_one_sheet = pygame.image.load("assets/Billeder/Sprite Sheet - Karl.png").convert_alpha()
fighter_two_sheet = pygame.image.load("assets/Billeder/Sprite Sheet - Phillip.png").convert_alpha()

#define fighter variables
fighter_SIZE = 800

fighter_one_SCALE = 0.25
fighter_one_OFFSET = [72, 56]
fighter_one_DATA = [fighter_SIZE, fighter_one_SCALE, fighter_one_OFFSET]
fighter_two_SCALE = 0.25
fighter_two_OFFSET = [72, 56]
fighter_two_DATA = [fighter_SIZE, fighter_two_SCALE, fighter_two_OFFSET]

#define number of steps in each animation
animation_steps = [3, 2, 2, 2, 3, 3, 3, 1]


#create two instances of the player class
fighter_one = PlayerClass(1, screen, 101, 500, 100, 200, False, fighter_one_DATA, fighter_one_sheet, animation_steps)
fighter_two = PlayerClass(2, screen, 1000, 700, 100, 200, False, fighter_two_DATA, fighter_two_sheet, animation_steps)

#create instances of the hitbox class
hitbox_fighterTwo_punch = HitClass(screen, 0, 0, 100, 20)

health = 255
health1 = 255
health2 = 0

# Define skillpoint upgrade degrees
player_1_health_upgrade = 0
player_1_strength_upgrade = 0
player_1_speed_upgrade = 0
player_1_knockback_upgrade = 0
player_1_stamina_upgrade = 0

player_2_health_upgrade = 0
player_2_strength_upgrade = 0
player_2_speed_upgrade = 0
player_2_knockback_upgrade = 0
player_2_stamina_upgrade = 0

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

    fighter_one.move(fighter_two)
    fighter_two.move(fighter_one)

    fighter_one.update()
    fighter_two.update()

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

# Define health bar colors
    background_color = (100, 100, 100)
    outline_color = (50, 50, 50)
    black_color = (0, 0, 0)
    health_color = (health2, health1, 0)

# Define screen spacings and lengths
    screen_spacing_1 = int(gameWindowWidth / 50)
    screen_spacing_2 = int(gameWindowWidth / 200)
    health_bar_length = int(gameWindowWidth / 3)

# Draw player 1 health bar
    pygame.draw.rect(screen, background_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
    pygame.draw.rect(screen, outline_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, black_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
    pygame.draw.rect(screen, outline_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_color, pygame.Rect(screen_spacing_1 + 3 * screen_spacing_2, screen_spacing_1 + 3 * screen_spacing_2, (health_bar_length - 6 * screen_spacing_2) * (health / 255), 3 * screen_spacing_2))

# Draw player 2 health bar
    pygame.draw.rect(screen, background_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
    pygame.draw.rect(screen, outline_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, black_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
    pygame.draw.rect(screen, outline_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_color, pygame.Rect(gameWindowWidth - health_bar_length - screen_spacing_1 + 3 * screen_spacing_2 - (health_bar_length - 6 * screen_spacing_2) * (health / 255 - 1), screen_spacing_1 + 3 * screen_spacing_2, (health_bar_length - 6 * screen_spacing_2) / (255 / health), 3 * screen_spacing_2))

# Define skillpoint upgrade colors
    player_1_health_upgrade_color = (100 - 20 * player_1_health_upgrade, 105 + 30 * player_1_health_upgrade, 0)
    player_1_strength_upgrade_color = (100 - 20 * player_1_strength_upgrade, 105 + 30 * player_1_strength_upgrade, 0)
    player_1_speed_upgrade_color = (100 - 20 * player_1_speed_upgrade, 105 + 30 * player_1_speed_upgrade, 0)
    player_1_knockback_upgrade_color = (100 - 20 * player_1_knockback_upgrade, 105 + 30 * player_1_knockback_upgrade, 0)
    player_1_stamina_upgrade_color = (100 - 20 * player_1_stamina_upgrade, 105 + 30 * player_1_stamina_upgrade, 0)

    player_2_health_upgrade_color = (100 - 20 * player_2_health_upgrade, 105 + 30 * player_1_health_upgrade, 0)
    player_2_strentgh_upgrade_color = (100 - 20 * player_2_strength_upgrade, 105 + 30 * player_1_health_upgrade, 0)
    player_2_speed_upgrade_color = (100 - 20 * player_2_speed_upgrade, 105 + 30 * player_1_health_upgrade, 0)
    player_2_knockback_upgrade_color = (100 - 20 * player_2_knockback_upgrade, 105 + 30 * player_1_health_upgrade, 0)
    player_2_stamina_upgrade_color = (100 - 20 * player_2_stamina_upgrade, 105 + 30 * player_1_health_upgrade, 0)

# Draw player 1 skillpoint upgrading screen
    pygame.draw.rect(screen, background_color, pygame.Rect(5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1))
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1), screen_spacing_2)
    # Health upgrade
    pygame.draw.rect(screen, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, player_1_health_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    # Strength upgrade
    pygame.draw.rect(screen, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, player_1_strength_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    # Speed upgrade
    pygame.draw.rect(screen, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, player_1_speed_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    # Knockback upgrade
    pygame.draw.rect(screen, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, player_1_knockback_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    # Stamina upgrade
    pygame.draw.rect(screen, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, player_1_stamina_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
    pygame.draw.rect(screen, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)

    # Draw player 2 skillpoint upgrading screen


    pygame.event.pump()
    pygame.display.flip()

pygame.quit()
