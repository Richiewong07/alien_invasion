import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # LOAD THE SHIP IMAGE AND GET ITS RECT.
        self.image = pygame.image.load('images/ship.bmp')   # LOADS IMAGE
        self.rect = self.image.get_rect()   # ACCESS SURFACE'S RECT ATTRIBUTE --> TREATS IT LIKE A RECTANGLE
        self.screen_rect = screen.get_rect()

        # START EACH SHIP AT THE BOTTOM CENTER OF THE SCREEN
        self.rect.centerx = self.screen_rect.centerx # MATCH X COORDINATE OF SHIP = X COORDINATE OF SCREEN
        self.rect.bottom = self.screen_rect.bottom # MATCH Y COORDINATE OF SHIP BOTTOM MATCH SCREEN BOTTOM

        # STORE A DECIMAL VALUE FOR THE SHIP'S CENTER
        self.center = float(self.rect.centerx)

        # MOVEMENT FLAG
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # UPDATE THE SHIP'S CENTER VALUE, NOT THE RECT.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # UPDATE RECT OBJECT FROM SELF.CENTER
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) # DRAW IMAGE BY RECT
