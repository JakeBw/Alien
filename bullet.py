import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height) # Set bullet dimensions
        self.rect.centerx = ship.rect.centerx # Set bullet start location to the ships center pos
        self.rect.top = ship.rect.top # Set the bullet to the top of the ship
        
        self.y = float(self.rect.y) # Converts self.y to a float
        
        self.color = ai_settings.bullet_colour # Set bullet colour
        self.speed_factor = ai_settings.bullet_speed_factor # Set bullet speed
        
    def update(self):
        self.y -= self.speed_factor 
        self.rect.y = self.y
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)