class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # SCREEN SETTINGS
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # SHIP SETTINGS --> HOW FAR TO MOVE SHIP ON EACH PASS THROUGH THE LOOP
        self.ship_speed_factor = 1.5
