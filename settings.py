class Settings():
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.ship_speed_factor = 10
        self.ship_limit = 3
        self.game_caption = "Alien Invasion!"
        
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3
        
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 # 1 is right, -1 left