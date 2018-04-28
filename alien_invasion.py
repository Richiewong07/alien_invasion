import pygame

from settings import Settings
from ship import Ship
import game_functions as gf




def run_game():
    # INITIALIZE PYGAME, SETTINGS, AND CREATE A SCREEN OBJECT.
    pygame.init()   # INITIALIZES BACKGROUND SETTING
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # CREATE DISPLAY WINDOW
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    # START MAIN LOOP FOR THE GAME.
    while True: # EVENT LOOP MANAGESS SCREEN UPDATES

        # WATCH FOR KEYBOARD AND MOUSE EVENTS.
        gf.check_events(ship)

        # UPDATES THE SHIP'S POSITION
        ship.update()

        # UDATES SCREEN WITH NEW IMAGES
        gf.update_screen(ai_settings, screen, ship)



run_game()
