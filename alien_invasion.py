import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # INITIALIZE PYGAME, SETTINGS, AND CREATE A SCREEN OBJECT.
    pygame.init()   # INITIALIZES BACKGROUND SETTING
    ai_settings = Settings()
    screen = pygame.display.set_mode(   # CREATE DISPLAY WINDOW
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # SET THE BACKGROUND COLOR.
    bg_color = (230, 230, 230)

    # START MAIN LOOP FOR THE GAME.
    while True: # EVENT LOOP MANAGESS SCREEN UPDATES

        # WATCH FOR KEYBOARD AND MOUSE EVENTS.
        for event in pygame.event.get(): # ACCESSES EVENT
            if event.type == pygame.QUIT:   # EVENT TO CLOSE SYSTEM
                sys.exit()

        # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP.
        screen.fill(ai_settings.bg_color)

        ship.blitme()

        # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE.
        pygame.display.flip()

run_game()
