class Settings:
    """all settings for Alien Invasion."""

    def __init__(self):
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings, speed slowed for smooth movement  and 3 lives per game
        self.ship_speed = 1.5
        self.ship_limit = 3

        # bullet settings, inccreasedd speed and numbber allowed for easier gameplay,  changed to red for visibillity
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 10

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1