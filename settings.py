class Settings():
    
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)
        self.ship_limit = 3
        self.game_caption = "Alien Invasion!"
        
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 100
        
        self.alien_points = 50
        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        
        
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1 # 1 is right, -1 is left
        
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        