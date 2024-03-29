import sys
from settings import Settings
from ship import Ship
import game_functions as gf
import pygame
from pygame.sprite import Group
from alien import Alien
from gamestats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # Set game window size
    pygame.display.set_caption(ai_settings.game_caption) # Set game window title
    ship = Ship(ai_settings, screen) #initialize the ship
    bullets = Group() # creating a group, similar to a list i think for the bullets.
    aliens = Group()
    alien = Alien(ai_settings, screen)
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")
    sb = Scoreboard(ai_settings, screen, stats)
    
    gf.create_fleet(ai_settings, screen, ship, aliens)

    
    while(True):
        gf.check_events(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets) 
        if stats.game_active:
                bullets.update()    
                ship.update()
                gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)        
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

              
run_game()