import pygame

pygame.init()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set up the drawing window
screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])
pygame.display.set_caption("Street FIT")
print(gameWindowWidth, gameWindowHeight)

from Player import PlayerClass

clock = pygame.time.Clock()

fighter_one = PlayerClass(screen, 101, 102, 103, 200, 10)
fighter_two = PlayerClass(screen, 101, 102, 103, 200, 10)

def collisionChecker(firstGameObject, secondGameObject):
    if firstGameObject.xPos + firstGameObject.width > secondGameObject.xPos and firstGameObject.xPos < secondGameObject.xPos + secondGameObject.width and firstGameObject.yPos + firstGameObject.height > secondGameObject.yPos and firstGameObject.yPos < secondGameObject.yPos + secondGameObject.height:
        return True

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

    if collisionChecker(fighter_one, fighter_two):
        fighter_one.color = (255, 0, 0)
    else:
        fighter_one.color = (1, 1, 1)


    fighter_one.update()
    fighter_one.draw()

    fighter_two.update()
    fighter_two.draw()

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

    pygame.display.flip()
    clock.tick(60)
