import pygame


class GameControlClass:
    def __init__(self, gameWindowWidth, screen):
        self.windowWidth = gameWindowWidth
        self.display = screen
        # Define some health color things :)
        self.health = 255
        self.health1 = 255
        self.health2 = 0
        # Define player 1 skillpoint upgrade degrees
        self.player_1_health_upgrade = 0
        self.player_1_strength_upgrade = 0
        self.player_1_speed_upgrade = 0
        self.player_1_knockback_upgrade = 0
        self.player_1_stamina_upgrade = 0
        # Define player 2 skillpoint upgrade degrees
        self.player_2_health_upgrade = 0
        self.player_2_strength_upgrade = 0
        self.player_2_speed_upgrade = 0
        self.player_2_knockback_upgrade = 0
        self.player_2_stamina_upgrade = 0
        # Define health bar colors
        self.background_color = (100, 100, 100)
        self.outline_color = (50, 50, 50)
        self.black_color = (0, 0, 0)
        self.health_color = (self.health2, self.health1, 0)
        # Define screen spacings and lengths
        self.screen_spacing_1 = int(gameWindowWidth / 50)
        self.screen_spacing_2 = int(gameWindowWidth / 200)
        self.health_bar_length = int(gameWindowWidth / 3)

    def draw_health_bars(self, display, health, windowWidth, background_color, outline_color, black_color,
                         health_color, screen_spacing_1, screen_spacing_2, health_bar_length):
        # Draw player 1 health bar
        pygame.draw.rect(display, background_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, black_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, health_color, pygame.Rect(screen_spacing_1 + 3 * screen_spacing_2, screen_spacing_1 + 3 * screen_spacing_2, (health_bar_length - 6 * screen_spacing_2) * (health / 255), 3 * screen_spacing_2))

        # Draw player 2 health bar
        pygame.draw.rect(display, background_color, pygame.Rect(windowWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(windowWidth - health_bar_length - screen_spacing_1, screen_spacing_1, health_bar_length, 9 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, black_color, pygame.Rect(windowWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2))
        pygame.draw.rect(display, outline_color, pygame.Rect(windowWidth - health_bar_length - screen_spacing_1 + 2 * screen_spacing_2, screen_spacing_1 + 2 * screen_spacing_2, health_bar_length - 4 * screen_spacing_2, 5 * screen_spacing_2), screen_spacing_2)
        pygame.draw.rect(display, health_color, pygame.Rect(windowWidth - health_bar_length - screen_spacing_1 + 3 * screen_spacing_2 - (health_bar_length - 6 * screen_spacing_2) * (health / 255 - 1), screen_spacing_1 + 3 * screen_spacing_2, (health_bar_length - 6 * screen_spacing_2) / (255 / health), 3 * screen_spacing_2))

    def draw_skillpoint_upgrade(self, display, player_1_health_upgrade, player_1_strength_upgrade,
                                player_1_speed_upgrade, player_1_knockback_upgrade, player_1_stamina_upgrade,
                                player_2_health_upgrade, player_2_strength_upgrade, player_2_speed_upgrade,
                                player_2_knockback_upgrade, player_2_stamina_upgrade, windowWidth, background_color,
                                outline_color, black_color, screen_spacing_1, screen_spacing_2):
        # Define skillpoint upgrade colors
        player_1_health_upgrade_color = (100 - 20 * player_1_health_upgrade, 105 + 30 * player_1_health_upgrade, 0)
        player_1_strength_upgrade_color = (100 - 20 * player_1_strength_upgrade, 105 + 30 * player_1_strength_upgrade, 0)
        player_1_speed_upgrade_color = (100 - 20 * player_1_speed_upgrade, 105 + 30 * player_1_speed_upgrade, 0)
        player_1_knockback_upgrade_color = (100 - 20 * player_1_knockback_upgrade, 105 + 30 * player_1_knockback_upgrade, 0)
        player_1_stamina_upgrade_color = (100 - 20 * player_1_stamina_upgrade, 105 + 30 * player_1_stamina_upgrade, 0)

        player_2_health_upgrade_color = (100 - 20 * player_2_health_upgrade, 105 + 30 * player_1_health_upgrade, 0)
        player_2_strength_upgrade_color = (100 - 20 * player_2_strength_upgrade, 105 + 30 * player_1_health_upgrade, 0)
        player_2_speed_upgrade_color = (100 - 20 * player_2_speed_upgrade, 105 + 30 * player_1_health_upgrade, 0)
        player_2_knockback_upgrade_color = (100 - 20 * player_2_knockback_upgrade, 105 + 30 * player_1_health_upgrade, 0)
        player_2_stamina_upgrade_color = (100 - 20 * player_2_stamina_upgrade, 105 + 30 * player_1_health_upgrade, 0)

        # Draw player 1 skillpoint upgrading screen
        pygame.draw.rect(display, background_color, pygame.Rect(5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1), screen_spacing_2)
        # Health upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_1_health_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Strength upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_1_strength_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Speed upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_1_speed_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Knockback upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_1_knockback_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Stamina upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_1_stamina_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)

        # Draw player 2 skillpoint upgrading screen
        pygame.draw.rect(display, background_color, pygame.Rect(windowWidth - 5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(windowWidth - 5 * screen_spacing_1, 8 * screen_spacing_1, 11 * screen_spacing_1, 11 * screen_spacing_1), screen_spacing_2)
        # Health upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_2_health_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 8 * screen_spacing_1 + 2 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Strength upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_2_strength_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 9 * screen_spacing_1 + 3 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Speed upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_2_speed_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 10 * screen_spacing_1 + 4 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Knockback upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_2_knockback_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 11 * screen_spacing_1 + 5 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        # Stamina upgrade
        pygame.draw.rect(display, black_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 10 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, player_2_stamina_upgrade_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, player_1_health_upgrade * 2 * screen_spacing_1, screen_spacing_1))
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 2 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 4 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 6 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)
        pygame.draw.rect(display, outline_color, pygame.Rect(5 * screen_spacing_1 + 2 * screen_spacing_2 + 8 * screen_spacing_1, 12 * screen_spacing_1 + 6 * screen_spacing_2, 2 * screen_spacing_1, screen_spacing_1), screen_spacing_2)