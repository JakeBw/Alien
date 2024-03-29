import sys
from bullet import Bullet
from alien import Alien
import pygame
from time import sleep

def check_events(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, mouse_x, mouse_y)
            
                
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
     if not stats.game_active:
        play_button.draw_button()
     sb.show_score()
     pygame.display.flip()
     screen.fill(ai_settings.bg_colour)
     ship.blitme()
     aliens.draw(screen)
     
     for bullet in bullets.sprites():
         bullet.draw_bullet()
     
def check_keydown_events(event, ai_settings, screen, ship, bullets): # Detect key down inputs and move the ship by setting the bools.
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
           ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(ai_settings, screen, ship, bullets)   
        elif event.key == pygame.K_q:
            print("Game exiting!")
            sys.exit()
 
            
def check_keyup_events(event,ship): # Detect key up to stop the ship from moving, this also let's us hold down our keys to move around.
    if event.type == pygame.KEYUP:
         if event.key == pygame.K_RIGHT:
            ship.moving_right = False
         elif event.key == pygame.K_LEFT:
             ship.moving_left = False

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
              bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

    
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship) #
        bullets.add(new_bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
    print(len(bullets))
    
    if collisions:
        for aliens in collisions.values():    
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
        
def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_of_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
        
def get_number_of_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        aliens.add(alien)
        
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
        
def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship Hit!")
        ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets)
        
    check_aliens_bottom(ai_settings, stats, screen, ship, sb, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
          change_fleet_direction(ai_settings, aliens)
          break
    
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
         alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1 # -1 * 1 = -1, -1 * -1 = 1, if dir is right set dir to left, if dir is left set dir to right
        
def ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets):
    if stats.ships_left > 0:    
        stats.ships_left -= 1
        
        aliens.empty()
        bullets.empty()
        sb.prep_ships()
        
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
def check_aliens_bottom(ai_settings, stats, screen, ship, sb, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, sb, aliens, bullets)
            break
    
def check_play_button(ai_settings, screen, stats, play_button, ship, sb, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if  button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.score = 0
        stats.level = 1
        
        sb.prep_score()
        sb.prep_level()
        sb.prep_high_score()
        sb.prep_ships()
        
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.game_active = True
        
        aliens.empty()
        bullets.empty()
        
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
        