import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group




def run_game():
    # INITIALIZE PYGAME, SETTINGS, AND CREATE A SCREEN OBJECT.
    pygame.init()   # INITIALIZES BACKGROUND SETTING

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # CREATE DISPLAY WINDOW

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings, screen)

    # MAKE GROUP TO STORE BULLETS IN.
    bullets = Group()

    # MAKE GROUP OF ALIENS.
    aliens = Group()

    # CREATE FLEET OF ALIENS.
    gf.create_fleet(ai_settings, screen, aliens)




    # START MAIN LOOP FOR THE GAME.
    while True: # EVENT LOOP MANAGESS SCREEN UPDATES

        # WATCH FOR KEYBOARD AND MOUSE EVENTS.
        gf.check_events(ai_settings, screen, ship, bullets)

        # UPDATES THE SHIP'S POSITION.
        ship.update()


        # UPDATES BULLET ON THE SCREEN.
        gf.update_bullets(bullets)

        # UDATES SCREEN WITH NEW IMAGES
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
