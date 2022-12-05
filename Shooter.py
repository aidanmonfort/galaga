import pygame

from Character import Character


class Shooter(Character):
    active = True

    def __init__(self, file, startX, startY, screen):
        Character.__init__(self, file, startX, startY)
        self.active = True
        self.img = pygame.transform.scale(self.img, ((pygame.Surface.get_width(screen) * .1),
                                          (pygame.Surface.get_height(screen) * .1)))

    def update(self, screen):
        self.y += self.dY
        self.x += self.dX
        if self.x < -15:
            self.x = -15
        if self.x > pygame.Surface.get_width(screen) - 50:
            self.x = pygame.Surface.get_width(screen) - 50
        if self.y < (pygame.Surface.get_height(screen) * .7):
            self.y = pygame.Surface.get_height(screen) * .7
        if self.y > pygame.Surface.get_height(screen)-50:
            self.y = pygame.Surface.get_height(screen)-50

    def drawCollisionRect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x + 10, self.y + 10, 50, 50), 1)

    def getCollisionRect(self):
        return pygame.Rect(self.x + 10, self.y + 10, 50, 50)