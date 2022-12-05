import pygame

class Bullet:
    x = 0
    y = 0
    dY = -10
    screen = pygame.Surface


    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

    def drawCollisionRect(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x - 3, self.y - 3, 6, 6), 1)

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (self.x, self.y), 3)
        self.drawCollisionRect()

    def update(self):
        self.y += self.dY

    def getCollisionRect(self):
        return pygame.Rect(self.x - 3, self.y - 3, 6, 6)

