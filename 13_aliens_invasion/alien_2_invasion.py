def __init__(self):
    self.sjip = Ship(self)
    self/bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()

    self._create_fleet()