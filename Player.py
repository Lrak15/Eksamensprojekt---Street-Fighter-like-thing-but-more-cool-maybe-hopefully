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
        self.animationList = self.load_images(sprite_sheet, animation_steps)
        self.action = 0  #0:idle #1:attack #2:block #3:duck #4:forward movement #5:backwards movement #6:kick #7:jump #8:been hit
        self.frameIndex = 0
        self.image = self.animationList[self.action][self.frameIndex]

        self.updateTime = pygame.time.get_ticks()
        self.updateHurtTime = pygame.time.get_ticks()
        self.updateAttackTime = pygame.time.get_ticks()

        self.punchStunTime = data[3][0]
        self.kickStunTime = data[3][1]

        self.p1PunchCooldown = 1000
        self.p2PunchCooldown = 1000

        self.p1KickCooldown = 1500
        self.p2KickCooldown = 1500

        self.fw_running = False
        self.bw_running = False
        self.jump = False
        self.punch = False
        self.kick = False
        self.ducking = False
        self.blocking = False
        self.fighter_one_stunned = False
        self.fighter_two_stunned = False
        self.hurt = False
        self.punched = False
        self.kicked = False
        self.midAttack = False
        self.actionsList = [self.punch, self.kick, self.punched, self.kicked, self.blocking]

        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]
        self.rect = pygame.Rect(self.xPos, self.yPos, width, height)

        self.jump_sfx = pygame.mixer.Sound("assets/lyd/SFX/jump.mp3")
        self.attack_sfx = pygame.mixer.Sound("assets/lyd/SFX/slå2.mp3")

    def load_images(self, sprite_sheet, animation_steps):
        # extract images from spritesheet
        animationList = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.scale, self.size * self.scale)))
            animationList.append(temp_img_list)
        print(animationList)
        return animationList
    def soundeffects(self, sfx_type):
        if sfx_type == self.jump:
            self.jump_sfx.play()
        elif sfx_type == self.punch:
            self.attack_sfx.play()

    def move(self, target):
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        speed = 10
        gravity = 3
        move_x = 0
        move_y = 0
        self.fw_running = False
        self.bw_running = False
        self.ducking = False

        # horizontal movement
        key = pygame.key.get_pressed()

        if not key[pygame.K_b] and self.player == 1:
            self.blocking = False
        if not key[pygame.K_p] and self.player == 2:
            self.blocking = False

        self.actionsList = [self.punch, self.kick, self.punched, self.kicked, self.blocking]
        if all(not elem for elem in self.actionsList):
            # handling controls for player 1
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

                # duck
                elif key[pygame.K_s]:
                    self.ducking = True

                # vertical movement: Jump
                if not self.jump:
                    if key[pygame.K_w]:
                        self.soundeffects(self.jump)
                        self.vel_y = -40
                        self.jump = True

                # ATTACCKKKK; punch
                if self.attack(self.p1PunchCooldown):
                    if key[pygame.K_c]:
                        self.punch = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()
                        self.soundeffects(self.punch)

                # ATTACCKKKK; kick
                if self.attack(self.p1KickCooldown):
                    if key[pygame.K_v]:
                        self.kick = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()

                # BLOCK YOU DIMBUS
                if key[pygame.K_b]:
                    self.blocking = True
                    self.soundeffects("Bloker")

                # flipping fighter if they move to the other side of the other fighter
                if target.rect.centerx > self.rect.centerx:
                    self.flip = False
                else:
                    self.flip = True

            # handling controls for player 2
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    if not self.flip:
                        self.bw_running = True
                    else:
                        self.fw_running = True
                    move_x = -speed

                elif key[pygame.K_RIGHT]:
                    if not self.flip:
                        self.fw_running = True
                    else:
                        self.bw_running = True
                    move_x = speed

                # duck
                elif key[pygame.K_DOWN]:
                    self.ducking = True

                # vertical movement: Jump
                if not self.jump:
                    if key[pygame.K_UP]:
                        self.soundeffects("jump")
                        self.vel_y = -40
                        self.jump = True

                # ATTACCKKKK; punch
                if self.attack(self.p2PunchCooldown):
                    if key[pygame.K_i]:
                        self.punch = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()
                # ATTACCKKKK; kick
                if self.attack(self.p2KickCooldown):
                    if key[pygame.K_o]:
                        self.kick = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()

                # BLOCK YOU DIMBUS
                if key[pygame.K_p]:
                    self.blocking = True

                # flipping fighter if they move to the other side of the other fighter
                if target.rect.centerx < self.rect.centerx:
                    self.flip = False
                else:
                    self.flip = True


        # applying gravity to the fighters
        self.vel_y += gravity
        move_y += self.vel_y

        # keep the player on the screen
        if self.rect.right + move_x > self.screenWidth:
            move_x = self.screenWidth - self.rect.right
        if self.rect.left + move_x < 0:
            move_x = -self.rect.x
        if self.rect.bottom + move_y > self.screenHeight - self.screenHeight / 20:
            move_y = self.screenHeight - (self.rect.bottom + self.screenHeight / 20)
            self.jump = False

        # update player
        self.xPos += move_x
        self.yPos += move_y

    def update(self):
        if self.jump:
            self.update_action(7)  # jumping
        elif self.punch:
            self.update_action(1)  # punching
        elif self.kick:
            self.update_action(6)  # kicking
        elif self.ducking:
            self.update_action(3)  # ducking
        elif self.blocking:
            self.update_action(2)  # blocking
        elif self.punched or self.kicked:
            self.update_action(8)  # been hit
        elif self.fw_running:
            self.update_action(4)  # running forwards
        elif self.bw_running:
            self.update_action(5)  # running backwards
        else:
            self.update_action(0)  # idle

        animation_cooldown = 100
        self.image = self.animationList[self.action][self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime > animation_cooldown:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()

        if self.action == 2 or self.action == 3:
            self.frameIndex = len(self.animationList[self.action]) - 1
        else:
            if self.frameIndex >= len(self.animationList[self.action]):
                self.frameIndex = 0
                if self.action == 1 or self.action == 6:
                    self.punch = False
                    self.kick = False

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # update the animation settings
            self.frameIndex = 0
            self.updateTime = pygame.time.get_ticks()

    def cooldown_resetter(self, cooldown, timeOfAction):
        if pygame.time.get_ticks() - timeOfAction > cooldown:
            return True
        else:
            return False

    def hurt_resetter(self):
        if self.punched:
            if self.cooldown_resetter(self.punchStunTime, self.updateHurtTime):
                self.punched = False

        elif self.kicked:
            if self.cooldown_resetter(self.kickStunTime, self.updateHurtTime):
                self.kicked = False

    def attack(self, cooldown):
        if self.cooldown_resetter(cooldown, self.updateAttackTime):
            return True
        else:
            return False

    def draw(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        img = pygame.transform.flip(self.image, self.flip, False)
        self.screen.blit(img, (self.rect.x - (self.offset[0] * self.scale), self.rect.y - (self.offset[1] * self.scale)))
