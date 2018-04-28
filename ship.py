import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # LOAD THE SHIP IMAGE AND GET ITS RECT.
        self.image = pygame.image.load('images/ship.bmp')   # LOADS IMAGE
        self.rect = self.image.get_rect()   # ACCESS SURFACE'S RECT ATTRIBUTE --> TREATS IT LIKE A RECTANGLE
        self.screen_rect = screen.get_rect()

        # START EACH SHIP AT THE BOTTOM CENTER OF THE SCREEN
        self.rect.centerx = self.screen_rect.centerx # MATCH X COORDINATE OF SHIP = X COORDINATE OF SCREEN
        self.rect.bottom = self.screen_rect.bottom # MATCH Y COORDINATE OF SHIP BOTTOM MATCH SCREEN BOTTOM

        # MOVEMENT FLAG
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # DRAW IMAGE BY RECT
