import math

import pygame
from Character import *


class EnemyOne(Character):
    bottomed = False
    top = False

    def __init__(self, file, startX, startY, screen):
        Character.__init__(self, file, startX, startY)
        self.dX = -5
        self.dY = 5
        self.img = pygame.transform.scale(self.img, ((pygame.Surface.get_width(screen) * .1),
                                          (pygame.Surface.get_height(screen) * .1)))

    def update(self, screen):
        if not self.bottomed and not self.top:
            self.x += self.dX
            self.y += self.dY
            if self.x < -15:
                self.x = -15
                self.dX *= -1
            if self.x > pygame.Surface.get_width(screen) - 50:
                self.x = pygame.Surface.get_width(screen) - 50
                self.dX *= -1
            if self.y > pygame.Surface.get_height(screen) * .7:
                self.y = pygame.Surface.get_height(screen) * .7
                self.dX = 0
                self.dY = -1
                self.bottomed = True
        elif self.bottomed and not self.top:
            self.y += self.dY
            if self.y < pygame.Surface.get_height(screen) * .2:
                self.y = pygame.Surface.get_height(screen) * .2
                self.dY = 0
                self.dX = -1
                self.top = True
        elif self.top:
            self.x += self.dX
            if self.x < -15:
                self.x = -15
                self.dX *= -1
            if self.x > pygame.Surface.get_width(screen) - 50:
                self.x = pygame.Surface.get_width(screen) - 50
                self.dX *= -1

    def getCollisionRect(self):
        return pygame.Rect(self.x + 15, self.y + 15, 40, 38)

    def drawCollisionRect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.getCollisionRect(), 1)

class EnemyTwo(Character):
    startCircle = False
    endCircle = False
    targetX = 250
    targetY = 250
    currentDegrees = 180

    def __init__(self, file, startX, startY, screen):
        Character.__init__(self, file, startX, startY)
        self.img = pygame.transform.scale(self.img, ((pygame.Surface.get_width(screen) * .1),
                                          (pygame.Surface.get_height(screen) * .1)))

    def update(self, screen):
        if not self.startCircle and (
                (self.x == 250 + (200 * math.cos(180*(math.pi/180)))) and
                (self.y == 250)):
            self.startCircle = True
        else:
            if self.x != 250 + (200 * math.cos(180*(math.pi/180))):
                if (self.x > 250 + (200 * math.cos(180*(math.pi/180)))):
                    self.x += -1
                elif self.x < 250 + (200 * math.cos(180*(math.pi/180))):
                    self.x += 1
            if self.y != 250:
                if self.y > 250:
                    self.y += -1
                elif self.y < 250:
                    self.y += 1
        if self.startCircle:
            self.x = 250 + (200 * math.cos(self.currentDegrees*(math.pi/180)))
            self.y = 250 - (200 * math.sin(self.currentDegrees*(math.pi/180)))
            self.currentDegrees += 1
            if self.currentDegrees == 360:
                self.currentDegrees = 0
        if self.startCircle and (self.x == 250 + (200 * math.cos(self.currentDegrees*(math.pi/180))) and
                (self.y == 250 - (200 * math.sin(self.currentDegrees*(math.pi/180))))):
            self.endCircle = True
            self.startCircle = False


    def getCollisionRect(self):
        return pygame.Rect(self.x + 15, self.y + 15, 40, 38)

    def drawCollisionRect(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.getCollisionRect(), 1)

