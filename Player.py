import pygame

class PlayerClass:

    punch_height = 20
    punch_width = 0
    color = (255, 1, 1)
    vel_y = 0
    color_green = (1, 255, 1)

    def __init__(self, player, screen, x, y, width, height, flip, data, sprite_sheet, animation_steps):
        self.player = player
        self.screen = screen
        self.xPos = x
        self.yPos = y
        self.width = width
        self.height = height
        self.size = data[0]
        self.scale = data[1]
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
        self.ducking = False
        self.attacking = False

        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]
        self.rect = pygame.Rect(self.xPos, self.yPos, width, height)

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
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.scale, self.size * self.scale)))
            animation_list.append(temp_img_list)
            y += 1
        return animation_list



    def soundeffects(self, sfx_type):
        if sfx_type == "jump":
            self.jump_sfx.play()
        elif sfx_type == "attack":
            self.attack_sfx.play()

    def move(self, target):
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        speed = 10
        gravity = 3
        move_x = 0
        move_y = 0
        self.fw_running = False
        self.bw_running = False


        #horizontal movement
        key = pygame.key.get_pressed()

        if not self.punch and not self.kick:
            if self.player == 1:
                if key[pygame.K_a]:
                    if not self.flip:
                        self.bw_running = True
                    else:
                        self.fw_running = True
                    move_x = -speed

                elif key[pygame.K_d]:
                    if not self.flip:
                        self.fw_running = True
                    else:
                        self.bw_running = True
                    move_x = speed

                #duck
                elif key[pygame.K_s]:
                    self.ducking = True


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
                    self.attacking = True
                    #self.attack()
                elif key[pygame.K_v]:
                    #self.soundeffects("attack")
                    self.kick = True
                    self.attacking = True
                   # self.attack()

                if target.rect.centerx > self.rect.centerx:
                    self.flip = False
                else:
                    self.flip = True



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
        self.xPos += move_x
        self.yPos += move_y

    def update(self):
        if self.jump:
            self.update_action(7) #jumping
        elif self.punch:
            self.update_action(1) #punching
        elif self.kick:
            self.update_action(6) #kicking
        elif self.ducking:
            self.update_action(3) #ducking
        elif self.fw_running:
            self.update_action(4) #running forwards
        elif self.bw_running:
            self.update_action(5) #running backwards
        else:
            self.update_action(0) #idle


        animation_cooldown = 100
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

    def hitbox(self):
        box_xPos = self.rect.x + 500 * self.scale
        box_yPos = self.rect.y - 50 * self.scale
        box_width = self.scale * 175
        box_height = self.scale * 225
        hitbox_kick_rect = pygame.Rect(box_xPos, box_yPos, box_width, box_height)
        if self.kick:
            if self.frame_index == 2:
                pygame.draw.rect(self.screen, self.color_green, hitbox_kick_rect, 3, 1)




    def attack(self):
        attack_color = (0, 255, 0)
        attack_rect = pygame.Rect(self.rect.right, self.rect.y, self.rect.width * 2, self.rect.height)
        pygame.draw.rect(self.screen, attack_color, attack_rect)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.xPos, self.yPos+125, self.punch_width, self.punch_height))
        img = pygame.transform.flip(self.image, self.flip, False)
        self.screen.blit(img, (self.rect.x - (self.offset[0] * self.scale), self.rect.y - (self.offset[1] * self.scale)))
