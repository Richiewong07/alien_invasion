import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get(): # ACCESSES EVENT
        if event.type == pygame.QUIT:   # EVENT TO CLOSE SYSTEM
            sys.exit()

        # RESPONSES TO KEYDOWN EVENT
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_settings, screen, ship, bullets)


        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)


def check_key_down_events(event, ai_settings, screen, ship, bullets):
    """ Respond to keypresses."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)

    if event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, ship):
    """ Respond to keypresses."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_bullets(bullets):
    """Update the position of the bullets and get rid of old bullets."""
    # UPDATES BULLET ON THE SCREEN.
    bullets.update()

    # GET RID OF BULLETS THAT HAVE DISAPPEARED.
    for bullet in bullets.copy():   # MAKE COPY WITH NOT REMOVE LIST OR GROUP WITHIN FOR LOOP
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullets(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # CREATE A NEW BULLET AND ADD IT TO THE BULLETS GROUP.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet) # .add --> ADDS THE SPRITE TO THE GROUP

def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determmine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai.settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_heigth))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, number_rows):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    # CREATE AN ALIEN AND FIND THE NUMBER OF ALIENS IN A ROW.
    # SPACING BETWEEN EACH ALIEN IS EQUAL TO ONE ALIEN WIDTH.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)


    # CREATE THE FIRST ROW OF ALIENS.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # CREATE AN ALIEN AND PLACE IT IN THE ROW.
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on screen and flip to the new screen."""

    # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP.
    screen.fill(ai_settings.bg_color)

    # DRAW SHIP ONSCREEN
    ship.blitme()

    # DRAW ALIEN ONSCREEN
    aliens.draw(screen)

    # REDRAW ALL BULLETS BEHIND SHIP AND ALIENS.
    for bullet in bullets.sprites():    # bullets.sprites() --> RETURNS A LIST OF ALL SPRITES IN THE GROUP
        bullet.draw_bullet()

    # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE.
    pygame.display.flip()
