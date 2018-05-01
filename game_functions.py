import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get(): # ACCESSES EVENT
        if event.type == pygame.QUIT:   # EVENT TO CLOSE SYSTEM
            sys.exit()

        # RESPONSES TO KEYDOWN EVENT
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event,ship)


        elif event.type == pygame.KEYUP:
            check_key_up_events(event,ship)


def check_key_down_events(event, ship):
    """ Respond to keypresses."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_key_up_events(event, ship):
    """ Respond to keypresses."""

    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
            ship.moving_left = False

            
def update_screen(ai_settings, screen, ship):
    """Update images on screen and flip to the new screen."""

    # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP.
    screen.fill(ai_settings.bg_color)

    # DRAW SHIP ONSCREEN
    ship.blitme()

    # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE.
    pygame.display.flip()
