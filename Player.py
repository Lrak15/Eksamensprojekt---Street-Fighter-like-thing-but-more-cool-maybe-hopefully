import pygame
import os
from pygame import mixer

class PlayerClass:
    xPos = 0
    yPos = 0
    width = 0
    height = 0
    punch_height = 20
    punch_width = 0
    color = (255, 1, 1)
    vel_y = 0
    jump = False
    attack = False




    def __init__(self, player, screen, x, y, width, height):
        self.Player = player
        self.screen = screen
        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]
        self.rect = pygame.Rect(x, y, width, height)

        self.jump_sfx = pygame.mixer.Sound("assets/lyd/SFX/jump.mp3")
        self.attack_sfx = pygame.mixer.Sound("assets/lyd/SFX/slå2.mp3")

    def soundeffects(self, sfx_type):
        if sfx_type == "jump":
            self.jump_sfx.play()
        elif sfx_type == "attack":
            self.attack_sfx.play()

    def move(self):
        speed = 10
        gravity = 3
        move_x = 0
        move_y = 0

        #horizontal movement
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            move_x = -speed
        elif key[pygame.K_d]:
            move_x = speed
        else:
            move_x = 0
        #vertival movement: Jump
        if not self.jump:
            if key[pygame.K_w]:
                self.soundeffects("jump")
                self.vel_y = -40
                self.jump = True


        #ATTACCKKKK

        if key[pygame.K_c]:
            self.soundeffects("attack")
            self.attack()


        self.vel_y += gravity
        move_y += self.vel_y

        #keep the player on the screen
        if self.rect.right + move_x > self.screenWidth:
            move_x = self.screenWidth - self.rect.right
        if self.rect.left + move_x < 0:
            move_x = -self.rect.x
        if self.rect.bottom + move_y > self.screenHeight:
            move_y = self.screenHeight - self.rect.bottom
            self.jump = False


        #update player
        self.rect.x += move_x
        self.rect.y += move_y


    def attack(self):
        attack_color = (0, 255, 0)
        attack_rect = pygame.Rect(self.rect.right, self.rect.y, self.rect.width * 2, self.rect.height)
        pygame.draw.rect(self.screen, attack_color, attack_rect)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos+125, self.punch_width, self.punch_height))
        pygame.draw.rect(self.screen, (1, 1, 1), pygame.Rect(self.rect.x-25, self.rect.top-10, 150, 20))
        pygame.draw.rect(self.screen, (1, 1, 1), pygame.Rect(self.rect.centerx-35, self.rect.top-60, 70, 50))

