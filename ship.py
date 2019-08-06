import pygame

class Ship():
    
    def __init__(self, screen, ai_settings):
        
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp') # Load our ship image.
        
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect() # Get screen dimensions? X/Y etc
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        
        self.moving_right = False
        self.moving_left = False
        
    def blitme(self):
        self.screen.blit(self.image, self.rect) # Draw the image to screen using Blit.
        
    def update(self):
         if self.moving_right and self.rect.right < self.screen_rect.right: # Move the ship +x on right and -x on left based on speed factor.
            self.center += self.ai_settings.ship_speed_factor
         if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
         self.rect.centerx = self.center
        

        
        