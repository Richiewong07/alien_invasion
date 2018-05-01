import sys

import pygame

from bullet import Bullet

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
        # CREATE A NEW BULLET AND ADD IT TO THE BULLETS GROUP.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet) # .add --> ADDS THE SPRITE TO THE GROUP


def check_key_up_events(event, ship):
    """ Respond to keypresses."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on screen and flip to the new screen."""

    # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP.
    screen.fill(ai_settings.bg_color)

    # DRAW SHIP ONSCREEN
    ship.blitme()

    # REDRAW ALL BULLETS BEHIND SHIP AND ALIENS.
    for bullet in bullets.sprites():    # bullets.sprites() --> RETURNS A LIST OF ALL SPRITES IN THE GROUP
        bullet.draw_bullet()

    # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE.
    pygame.display.flip()
