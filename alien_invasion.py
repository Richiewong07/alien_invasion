import sys

import pygame

def run_game():
    # INITIALIZE GAME AND CREATE A SCREEN OBJECT.
    pygame.init()   # INITIALIZES BACKGROUND SETTING
    screen = pygame.display.set_mode((600, 400))   # CREATE DISPLAY WINDOW
    pygame.display.set_caption("Alien Invasion")

    # SET THE BACKGROUND COLOR.
    bg_color = (230, 230, 230)

    # START MAIN LOOP FOR THE GAME.
    while True: # EVENT LOOP MANAGESS SCREEN UPDATES

        # WATCH FOR KEYBOARD AND MOUSE EVENTS.
        for event in pygame.event.get(): # ACCESSES EVENT
            if event.type == pygame.QUIT:   # EVENT TO CLOSE SYSTEM
                sys.exit()

        # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP.
        screen.fill(bg_color)

        # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE.
        pygame.display.flip()

run_game()
