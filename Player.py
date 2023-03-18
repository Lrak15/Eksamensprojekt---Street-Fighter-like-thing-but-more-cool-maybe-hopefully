import pygame




class PlayerClass:
    xPos = 0
    yPos = 0
    width = 0
    height = 0
    vel = 0
    color = (1, 1, 1)
    moveX = 0
    moveY = 0

    def __init__(self, screen, x, y, width, height, vel):
        self.screen = screen
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        self.vel = vel
        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]

    def update(self):
        self.xPos = self.xPos + self.moveX
        self.yPos = self.yPos + self.moveY

        if self.width + self.xPos > self.screenWidth:
            self.xPos = self.screenWidth - self.width
        if self.xPos < 0:
            self.xPos = 0
        if self.yPos + self.height > self.screenHeight:
            self.yPos = self.screenHeight - self.height
        if self.yPos < 0:
            self.yPos = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos, self.width, self.height))


gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode([gameWindowWidth, gameWindowHeight])



# Define health bar colors
health_bar_background_color = (100, 100, 100)
health_bar_outline_color = (0, 0, 0)
health_bar_red_color = (255, 0, 0)
health_bar_green_color = (0, 255, 0)

# Define screen spacings and lengths
screen_spacing_1 = int(gameWindowWidth / 50)
screen_spacing_2 = int(gameWindowWidth / 200)
health_bar_length = int(gameWindowWidth / 3)

def draw_health_bars(screenWidth):


    # Draw player 1 health bar
    pygame.draw.rect(screen, health_bar_background_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_red_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_green_color, pygame.Rect(screen_spacing_1 + 3 * screen_spacing_2, screen_spacing_1 + 3 * screen_spacing_2, 300, 3 * screen_spacing_2))

    # Draw player 2 health bar
    pygame.draw.rect(screen, health_bar_background_color, pygame.Rect(screenWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(screenWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_red_color, pygame.Rect(screenWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
    pygame.draw.rect(screen, health_bar_outline_color, pygame.Rect(screenWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
    pygame.draw.rect(screen, health_bar_green_color, pygame.Rect(screenWidth - health_bar_length - screen_spacing_1 + 3 * screen_spacing_2, screen_spacing_1 + 3 * screen_spacing_2, 300, 3 * screen_spacing_2))
