import sys

import pygame

def run_game():
    # INITIALIZE GAME AND CREATE A SCREEN OBJECT.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # START MAIN LOOP FOR THE GAME.
    while True:
        # WATCH FOR KEYBOARD AND MOUSE EVENTS.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # MAKE THE MOST RECENTLY DRAWN SCREEN VISIBLE.
        pygame.display.flip()

run_game()
