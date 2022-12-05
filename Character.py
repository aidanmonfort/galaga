import pygame

class Character:
    x = 0
    y = 0
    dY = 0
    dX = 0
    img = 0

    def __init__(self, file, startX, startY):
        self.img = pygame.image.load(file)
        self.x = startX
        self.y = startY

    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))