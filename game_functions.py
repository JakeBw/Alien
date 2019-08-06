import sys
from bullet import Bullet
import pygame

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
                
def update_screen(ai_settings, screen, ship, bullets):
     pygame.display.flip()
     screen.fill(ai_settings.bg_colour)
     ship.blitme()
     for bullet in bullets.sprites():
         bullet.draw_bullet()
     
def check_keydown_events(event, ai_settings, screen, ship, bullets): # Detect key down inputs and move the ship by setting the bools.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
           ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(ai_settings, screen, ship) #
            bullets.add(new_bullet)
            
def check_keyup_events(event,ship): # Detect key up to stop the ship from moving, this also let's us hold down our keys to move around.
    if event.type == pygame.KEYUP:
         if event.key == pygame.K_RIGHT:
            ship.moving_right = False
         elif event.key == pygame.K_LEFT:
             ship.moving_left = False

    