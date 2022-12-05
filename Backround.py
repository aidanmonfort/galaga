import pygame

class Backround:
    back = pygame.image.load('galagaBack.png')
    screen = pygame.Surface

    def __init__(self, screen):
        self.screen = screen
        self.back = pygame.transform.scale(self.back,
                                           (pygame.Surface.get_width(screen), pygame.Surface.get_height(screen)))

    def draw(self, screen):
        screen.blit(self.back, (0, 0))
