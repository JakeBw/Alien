import sys
from settings import Settings
from ship import Ship
import game_functions as gf
import pygame
from pygame.sprite import Group

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # Set game window size
    pygame.display.set_caption(ai_settings.game_caption) # Set game window title
    ship = Ship(screen, ai_settings) #initialize the ship
    bullets = Group() # creating a group, similar to a list i think for the bullets.
    
    while(True):
        gf.check_events(ai_settings, screen, ship, bullets) 
        bullets.update() 
        gf.update_screen(ai_settings, screen, ship, bullets)    
        ship.update()
              
run_game()