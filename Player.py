import pygame


class PlayerClass:
    def __init__(self, player, screen, x, y, width, height, flip, data, spriteSheet, animationSteps):
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
        self.animationList = self.load_images(spriteSheet, animationSteps)
        self.action = 0  #0:idle #1:attack #2:block #3:duck #4:forward movement #5:backwards movement #6:kick #7:jump #8:been hit
        self.frameIndex = 0
        self.image = self.animationList[self.action][self.frameIndex]
        self.velY = 0

        self.updateTime = pygame.time.get_ticks()
        self.updateHurtTime = pygame.time.get_ticks()
        self.updateAttackTime = pygame.time.get_ticks()

        self.punchStunTime = data[3][0]
        self.kickStunTime = data[3][1]

        self.p1PunchCooldown = 1000
        self.p2PunchCooldown = 1000

        self.p1KickCooldown = 1500
        self.p2KickCooldown = 1500

        self.fwRunning = False
        self.bwRunning = False
        self.jump = False
        self.punch = False
        self.kick = False
        self.ducking = False
        self.blocking = False
        self.hurt = False
        self.punched = False
        self.kicked = False
        self.midAttack = False
        self.actionsList = [self.punch, self.kick, self.punched, self.kicked, self.blocking]

        self.screenWidth = self.screen.get_size()[0]
        self.screenHeight = self.screen.get_size()[1]
        self.rect = pygame.Rect(self.xPos, self.yPos, width, height)

        self.jumpSfx = pygame.mixer.Sound("assets/lyd/SFX/jump.mp3")
        self.attackSfx = pygame.mixer.Sound("assets/lyd/SFX/slå2.mp3")
        self.blockSfx = pygame.mixer.Sound("assets/lyd/SFX/Bloker.mp3")

    # Function for cutting out all the frames in the spritesheets. The second loop cycles through each frame in each
    # animation and put these individual frames into a list. The first loop takes the list from the second loop and
    # puts it into another list. It moves an animation down where the second loop begin again.
    def load_images(self, spriteSheet, animationSteps):
        # extract images from spritesheet
        animationList = []
        for y, animation in enumerate(animationSteps):
            tempImgList = []
            for x in range(animation):
                tempImg = spriteSheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                tempImgList.append(pygame.transform.scale(tempImg, (self.size * self.scale, self.size * self.scale)))
            animationList.append(tempImgList)
        return animationList

    # Handling all the movement relating to the players.
    def move(self, target):
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width, self.height)
        speed = 10
        gravity = 3
        moveX = 0
        moveY = 0
        # Resets the variables to False - they're only True when a button is being pressed.
        self.fwRunning = False
        self.bwRunning = False
        self.ducking = False

        # Variable so we don't have to type as much xD.
        key = pygame.key.get_pressed()

        # Makes sure that the fighters stop blocking when the button isn't being pressed.
        if not key[pygame.K_b] and self.player == 1:
            self.blocking = False
        if not key[pygame.K_p] and self.player == 2:
            self.blocking = False

        # Horizontal movement. The purpose of the all function is to make sure the figthers can't move if they're
        # in the middle of a move or have been hit. The way it is used it returns as False, if either of the bools in
        # self.actionList is True.
        self.actionsList = [self.punch, self.kick, self.punched, self.kicked, self.blocking]
        if all(not elem for elem in self.actionsList):
            # Handling controls for player 1.
            if self.player == 1:
                if key[pygame.K_a]:
                    if not self.flip:
                        self.bwRunning = True
                    else:
                        self.fwRunning = True
                    moveX = -speed

                elif key[pygame.K_d]:
                    if not self.flip:
                        self.fwRunning = True
                    else:
                        self.bwRunning = True
                    moveX = speed

                # Duck.
                elif key[pygame.K_s]:
                    self.ducking = True

                # Vertical movement: Jump.
                if not self.jump:
                    if key[pygame.K_w]:
                        self.jumpSfx.play()
                        self.velY = -40
                        self.jump = True

                # ATTACCKKKK; punch.
                if self.attack(self.p1PunchCooldown):
                    if key[pygame.K_c]:
                        self.attackSfx.play()
                        self.punch = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()

                # ATTACCKKKK; kick.
                if self.attack(self.p1KickCooldown):
                    if key[pygame.K_v]:
                        self.attackSfx.play()
                        self.kick = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()

                # BLOCK YOU DIMBUS.
                if key[pygame.K_b]:
                    self.blockSfx.play()
                    self.blocking = True

                # Flipping fighter if they move to the other side of the other fighter.
                if target.rect.centerx > self.rect.centerx:
                    self.flip = False
                else:
                    self.flip = True

            # Handling controls for player 2.
            if self.player == 2:
                if key[pygame.K_LEFT]:
                    if not self.flip:
                        self.bwRunning = True
                    else:
                        self.fwRunning = True
                    moveX = -speed

                elif key[pygame.K_RIGHT]:
                    if not self.flip:
                        self.fwRunning = True
                    else:
                        self.bwRunning = True
                    moveX = speed

                # Duck.
                elif key[pygame.K_DOWN]:
                    self.ducking = True

                # Vertical movement: Jump.
                if not self.jump:
                    if key[pygame.K_UP]:
                        self.jumpSfx.play()
                        self.velY = -40
                        self.jump = True

                # ATTACCKKKK; punch.
                if self.attack(self.p2PunchCooldown):
                    if key[pygame.K_i]:
                        self.punch = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()
                # ATTACCKKKK; kick.
                if self.attack(self.p2KickCooldown):
                    if key[pygame.K_o]:
                        self.kick = True
                        self.midAttack = True
                        self.updateAttackTime = pygame.time.get_ticks()

                # BLOCK YOU DIMBUS.
                if key[pygame.K_p]:
                    self.blocking = True

                # Flipping fighter if they move to the other side of the other fighter.
                if target.rect.centerx < self.rect.centerx:
                    self.flip = False
                else:
                    self.flip = True

        # Applying gravity to the fighters.
        self.velY += gravity
        moveY += self.velY

        # Keep the fighters on the screen.
        if self.rect.right + moveX > self.screenWidth:
            moveX = self.screenWidth - self.rect.right
        if self.rect.left + moveX < 0:
            moveX = -self.rect.x
        if self.rect.bottom + moveY > self.screenHeight - self.screenHeight / 20:
            moveY = self.screenHeight - (self.rect.bottom + self.screenHeight / 20)
            self.jump = False

        # Update fighter positions.
        self.xPos += moveX
        self.yPos += moveY

    # Function for updating the actions and animationframes for the fighters.
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
        elif self.fwRunning:
            self.update_action(4)  # running forwards
        elif self.bwRunning:
            self.update_action(5)  # running backwards
        else:
            self.update_action(0)  # idle

        # Changes to the next frame in the animation after one animation_cooldown.
        animationCooldown = 100
        self.image = self.animationList[self.action][self.frameIndex]
        if pygame.time.get_ticks() - self.updateTime > animationCooldown:
            self.frameIndex += 1
            self.updateTime = pygame.time.get_ticks()

        # The animation is being frozen in the last frame if you're blocking or ducking - if not it just loops. If were
        # at the last frame of the punching or kicking animation it resets bool back to False and the animation stops.
        if self.action == 2 or self.action == 3:
            self.frameIndex = len(self.animationList[self.action]) - 1
        else:
            if self.frameIndex >= len(self.animationList[self.action]):
                self.frameIndex = 0
                if self.action == 1 or self.action == 6:
                    self.punch = False
                    self.kick = False

    # Changes the current action and resets the frameIndex to zero so the new animation is being played from frame 0.
    # Also captures the time of when the actions change to be used for cycling through frames.
    def update_action(self, newAction):
        # Check if the new action is different to the previous one.
        if newAction != self.action:
            self.action = newAction
            # Update the animation settings.
            self.frameIndex = 0
            self.updateTime = pygame.time.get_ticks()

    # Function returning True after a certain amount of time has passed (cooldown) from the timeOfAction.
    def cooldown_resetter(self, cooldown, timeOfAction):
        if pygame.time.get_ticks() - timeOfAction > cooldown:
            return True
        else:
            return False

    # Uses the cooldown_resetter function to make sure the fighter who just been attacked can't move for a bit of time.
    def hurt_resetter(self):
        if self.punched:
            if self.cooldown_resetter(self.punchStunTime, self.updateHurtTime):
                self.punched = False

        elif self.kicked:
            if self.cooldown_resetter(self.kickStunTime, self.updateHurtTime):
                self.kicked = False

    # Uses the cooldown_resetter function to make sure the fighter who just attacked can't move for a bit of time.
    def attack(self, cooldown):
        if self.cooldown_resetter(cooldown, self.updateAttackTime):
            return True
        else:
            return False

    # Draws the current picture (frame) of the fighter.
    def draw(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        img = pygame.transform.flip(self.image, self.flip, False)
        self.screen.blit(img, (self.rect.x - (self.offset[0] * self.scale), self.rect.y - (self.offset[1] * self.scale)))
