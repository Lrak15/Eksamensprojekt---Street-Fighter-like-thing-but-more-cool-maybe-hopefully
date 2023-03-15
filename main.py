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

    health_bar_background = (50, 50, 50)
    health_bar_red = (255, 0, 0)
    health_bar_green = (0, 255, 0)

    pygame.draw.rect(screen, health_bar_background, pygame.Rect(30, 30, 520, 50))
    pygame.draw.rect(screen, health_bar_red, pygame.Rect(40, 40, 500, 30))
    pygame.draw.rect(screen, health_bar_green, pygame.Rect(40, 40, 300, 30))

    pygame.display.flip()
    clock.tick(60)
