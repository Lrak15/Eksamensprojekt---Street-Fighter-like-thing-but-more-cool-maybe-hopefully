import pygame


class HealthBarClass:
    def __init__(self, gameWindowWidth, screen, x):
        self.window_width = gameWindowWidth
        self.display = screen
        # Define some health color things :)
        self.player_one_health = 255
        self.player_one_health1 = 255
        self.player_one_health2 = 0
        self.player_two_health = 255
        self.player_two_health1 = 255
        self.player_two_health2 = 0
        # Define health bar colors
        self.background_color = (100, 100, 100)
        self.outline_color = (50, 50, 50)
        self.black_color = (0, 0, 0)
        self.player_one_health_color = (self.player_one_health2, self.player_one_health1, 0)
        self.player_two_health_color = (self.player_two_health2, self.player_two_health1, 0)
        # Define screen spacings and lengths
        self.screen_spacing_1 = int(gameWindowWidth / 50)
        self.screen_spacing_2 = int(gameWindowWidth / 200)
        self.health_bar_length = int(gameWindowWidth / 3)

    def draw_health_bars(self, display, player_one_health, player_two_health, window_width, background_color, outline_color, black_color,
                         player_one_health_color, player_two_health_color, screen_spacing_1, screen_spacing_2, health_bar_length, xPos):
        # Draw player 1 health bar
        pygame.draw.rect(display, background_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, black_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, player_one_health_color, pygame.Rect(screen_spacing_1 + 3 * screen_spacing_2, screen_spacing_1 + 3 * screen_spacing_2, (health_bar_length - 6 * screen_spacing_2) * (player_one_health / 255), 3 * screen_spacing_2)) ##lol

        # Draw player 2 health bar
        pygame.draw.rect(display, background_color, pygame.Rect(window_width - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(window_width - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, black_color, pygame.Rect(window_width - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(window_width - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, player_two_health_color, pygame.Rect(window_width - health_bar_length - screen_spacing_1 + 3 * screen_spacing_2 - (health_bar_length - 6 * screen_spacing_2) * (player_two_health / 255 - 1), screen_spacing_1 + 3 * screen_spacing_2, (health_bar_length - 6 * screen_spacing_2) / (255 / player_two_health), 3 * screen_spacing_2))

    def player_one_punched(self):
        self.player_two_health -= 1
        if self.player_two_health > 127.5:
            self.player_two_health2 += 2
        else:
            self.player_two_health1 -= 2

    def player_two_punched(self):
        self.player_two_health -= 1
        if self.player_two_health > 127.5:
            self.player_two_health2 += 2
        else:
            self.player_two_health1 -= 2

    def player_one_kicked(self):
        self.player_two_health -= 2
        if self.player_two_health > 127.5:
            self.player_two_health2 += 4
        else:
            self.player_two_health1 -= 4

    def player_two_kicked(self):
        self.player_two_health -= 2
        if self.player_two_health > 127.5:
            self.player_two_health2 += 4
        else:
            self.player_two_health1 -= 4



class SkillpointUpgradeClass:
    def __init__(self, gameWindowWidth, screen):
        self.window_width = gameWindowWidth
        self.display = screen
        self.still_upgrading = True
        # Define player 1 skillpoint upgrade degrees
        self.player_1_health_upgrade = 0
        self.player_1_strength_upgrade = 0
        self.player_1_speed_upgrade = 0
        self.player_1_knockback_upgrade = 0
        self.player_1_stamina_upgrade = 0
        # Define player 1 skillpoint upgrade colors
        self.player_1_health_upgrade_color = (100 - 20 * self.player_1_health_upgrade, 105 + 30 * self.player_1_health_upgrade, 0)
        self.player_1_strength_upgrade_color = (100 - 20 * self.player_1_strength_upgrade, 105 + 30 * self.player_1_strength_upgrade, 0)
        self.player_1_speed_upgrade_color = (100 - 20 * self.player_1_speed_upgrade, 105 + 30 * self.player_1_speed_upgrade, 0)
        self.player_1_knockback_upgrade_color = (100 - 20 * self.player_1_knockback_upgrade, 105 + 30 * self.player_1_knockback_upgrade, 0)
        self.player_1_stamina_upgrade_color = (100 - 20 * self.player_1_stamina_upgrade, 105 + 30 * self.player_1_stamina_upgrade, 0)
        # Define player 2 skillpoint upgrade degrees
        self.player_2_health_upgrade = 0
        self.player_2_strength_upgrade = 0
        self.player_2_speed_upgrade = 0
        self.player_2_knockback_upgrade = 0
        self.player_2_stamina_upgrade = 0
        # Define player 2 skillpoint upgrade colors
        self.player_2_health_upgrade_color = (100 - 20 * self.player_2_health_upgrade, 105 + 30 * self.player_1_health_upgrade, 0)
        self.player_2_strength_upgrade_color = (100 - 20 * self.player_2_strength_upgrade, 105 + 30 * self.player_1_health_upgrade, 0)
        self.player_2_speed_upgrade_color = (100 - 20 * self.player_2_speed_upgrade, 105 + 30 * self.player_1_health_upgrade, 0)
        self.player_2_knockback_upgrade_color = (100 - 20 * self.player_2_knockback_upgrade, 105 + 30 * self.player_1_health_upgrade, 0)
        self.player_2_stamina_upgrade_color = (100 - 20 * self.player_2_stamina_upgrade, 105 + 30 * self.player_1_health_upgrade, 0)
        # Define amounts of upgrades
        self.player_1_remaining_upgrades = 10 # fordi han bedre
        self.player_2_remaining_upgrades = 5 # fordi han dårligere
        # Define screen spacings and lengths
        self.screen_spacing_1 = int(gameWindowWidth / 50)
        self.screen_spacing_2 = int(gameWindowWidth / 200)


    def draw_skillpoint_upgrade(self, display, player_1_health_upgrade, player_1_strength_upgrade,
                                player_1_speed_upgrade, player_1_knockback_upgrade, player_1_stamina_upgrade,
                                player_2_health_upgrade, player_2_strength_upgrade, player_2_speed_upgrade,
                                player_2_knockback_upgrade, player_2_stamina_upgrade, window_width, background_color,
                                outline_color, black_color, screen_spacing_1, screen_spacing_2, player_1_remaining_upgrades, player_2_remaining_upgrades):


        if self.still_upgrading:

            # Draw player 1 skillpoint upgrading screen
            pygame.draw.rect(display, background_color, pygame.Rect(5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1), screen_spacing_2)
            # Health upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_1_health_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Strength upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_1_strength_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Speed upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_1_speed_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Knockback upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_1_knockback_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Stamina upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_1_stamina_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)

            # Draw player 2 skillpoint upgrading screen
            pygame.draw.rect(display, background_color, pygame.Rect(window_width - 5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(window_width - 5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1), screen_spacing_2)
            # Health upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_2_health_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Strength upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_2_strength_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Speed upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_2_speed_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Knockback upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_2_knockback_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            # Stamina upgrade
            pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, self.player_2_stamina_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
            pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)

            number_checker = pygame.key.get_pressed()

            # player one skillpoint upgrades
            if player_1_remaining_upgrades > 0:
                if number_checker[pygame.K_1]:
                    player_1_health_upgrade += 1
                elif number_checker[pygame.K_2]:
                    player_1_strength_upgrade += 1
                elif number_checker[pygame.K_3]:
                    player_1_speed_upgrade += 1
                elif number_checker[pygame.K_4]:
                    player_1_knockback_upgrade += 1
                elif number_checker[pygame.K_5]:
                    player_1_stamina_upgrade += 1

            # player two skillpoint upgrades
            if player_2_remaining_upgrades > 0:
                if number_checker[pygame.K_6]:
                    player_2_health_upgrade += 1
                elif number_checker[pygame.K_7]:
                    player_2_strength_upgrade += 1
                elif number_checker[pygame.K_8]:
                    player_2_speed_upgrade += 1
                elif number_checker[pygame.K_9]:
                    player_2_knockback_upgrade += 1
                elif number_checker[pygame.K_0]:
                    player_2_stamina_upgrade += 1
