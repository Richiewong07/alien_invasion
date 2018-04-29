import sys

import pygame

def check_events(ship):
    """Respond to keypresses and mouse events."""



    for event in pygame.event.get(): # ACCESSES EVENT
        if event.type == pygame.QUIT:   # EVENT TO CLOSE SYSTEM
            sys.exit()


        elif event.type == pygame.KEYDOWN:  # RESPONSES TO KEYDOWN EVENT
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
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
