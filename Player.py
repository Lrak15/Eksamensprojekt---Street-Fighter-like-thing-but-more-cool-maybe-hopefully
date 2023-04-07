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

    def __init__(self, player, screen, x, y, width, height, flip, data, sprite_sheet, animation_steps):
        self.Player = player
        self.screen = screen
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  # 0:idle #1:attack #2:block #3:duck #4:forward movement #5:backwards movement #6:kick #7:jump
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time = pygame.time.get_ticks()

        self.attack_type = 0
        self.attack_cooldown = 0

        self.fw_running = False
        self.bw_running = False
        self.jump = False
        self.punch = False
        self.kick = False

        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]
        self.rect = pygame.Rect(x, y, width, height)

        self.jump_sfx = pygame.mixer.Sound("assets/lyd/SFX/jump.mp3")
        self.attack_sfx = pygame.mixer.Sound("assets/lyd/SFX/slå2.mp3")

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from spritesheet
        animation_list = []
        y = 0
        for animation in animation_steps:
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
            y += 1
        return animation_list



    def soundeffects(self, sfx_type):
        if sfx_type == "jump":
            self.jump_sfx.play()
        elif sfx_type == "attack":
            self.attack_sfx.play()

    def move(self, target):
        speed = 10
        gravity = 3
        move_x = 0
        move_y = 0
        self.fw_running = False
        self.bw_running = False


        #horizontal movement
        key = pygame.key.get_pressed()

        if not self.punch and not self.kick:
            if not self.flip:
                if key[pygame.K_a]:
                    move_x = -speed
                    self.bw_running = True
                elif key[pygame.K_d]:
                    move_x = speed
                    self.fw_running = True
                else:
                    move_x = 0
            else:
                if key[pygame.K_a]:
                    move_x = -speed
                    self.fw_running = True
                elif key[pygame.K_d]:
                    move_x = speed
                    self.bw_running = True
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
                #self.soundeffects("attack")
                self.punch = True
                #self.attack()
            elif key[pygame.K_v]:
                #self.soundeffects("attack")
                self.kick = True
               # self.attack()



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

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #update player
        self.rect.x += move_x
        self.rect.y += move_y

    def update(self):
        if self.jump:
            self.update_action(7)
        elif self.punch:
            self.update_action(1)
        elif self.kick:
            self.update_action(6)
        elif self.fw_running:
            self.update_action(4)
        elif self.bw_running:
            self.update_action(5)
        else:
            self.update_action(0)

        animation_cooldown = 250
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
            if self.action == 1 or self.action == 6:
                self.punch = False
                self.kick = False

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()



    def attack(self):
        attack_color = (0, 255, 0)
        attack_rect = pygame.Rect(self.rect.right, self.rect.y, self.rect.width * 2, self.rect.height)
        pygame.draw.rect(self.screen, attack_color, attack_rect)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos+125, self.punch_width, self.punch_height))
        img = pygame.transform.flip(self.image, self.flip, False)
        self.screen.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
