 def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()--snip-
        # Start Alien Invasion in an inactive state.
        self.game_active = False


from game_stats import GameStats
from button import Button



def __init__(self):--snip-
self.game_active = False
        # Make the Play button.
self.play_button = Button(self, "Play")


 def _update_screen(self):--snip-
self.aliens.draw(self.screen)
        # Draw the play button if the game is inactive.
if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()





 def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                --snip-
        elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)


 def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
      if self.play_button.rect.collidepoint(mouse_pos):
        self.game_active = True


def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()


 def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            --snip-
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

 def _ship_hit(self):
        """Respond to ship being hit by alien."""
        if self.stats.ships_left > 0:--snip-
        else:
            self.game_active = False
 pygame.mouse.set_visible(True)