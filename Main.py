import random

import pygame
from pygame import key
from Shooter import Shooter
from Backround import *
from Bullet import *
from Enemy import *

pygame.init()
pygame.display.set_caption("Galaga")
window = pygame.display.set_mode((700, 700))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
running = True
chars = [Shooter('galagaShooter.png', 600, 350, screen),
         Shooter('galagaShooter.png', 600, 350, screen),
         Shooter('galagaShooter.png', 600, 350, screen)]
level = 1
currChar = 0
chars[1].active = False
chars[2].active = False
back = Backround(screen)
bullets = []
enemy = []
pause = 0


def startScreen():
    font = pygame.font.Font("chiki-font/ChikiBubbles-rg9xp.ttf", 70)
    button = font.render("Start game", True, (116, 42, 133), None)
    buttonRect = button.get_rect()
    buttonRect.center = (pygame.Surface.get_width(screen) / 2, pygame.Surface.get_height(screen) / 2)
    start = False
    while not start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif pygame.mouse.get_pressed()[0] and buttonRect.inflate(10, 10).collidepoint(pygame.mouse.get_pos()):
                start = True

        screen.fill((255, 255, 255))
        screen.blit(button, buttonRect)
        pygame.draw.rect(screen, (144, 23, 59), buttonRect.inflate(10, 10), 1, 5)

        pygame.display.flip()
        clock.tick(60)
    return


def checkInput():
    global chars, currChar, bullets, pause
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_a] or keysPressed[pygame.K_LEFT]:
        chars[currChar].dX = -5
    if keysPressed[pygame.K_d] or keysPressed[pygame.K_RIGHT]:
        chars[currChar].dX = 5
    if keysPressed[pygame.K_w] or keysPressed[pygame.K_UP]:
        chars[currChar].dY = -5
    if keysPressed[pygame.K_s] or keysPressed[pygame.K_DOWN]:
        chars[currChar].dY = 5
    if keysPressed[pygame.K_SPACE]:
        if pause == 0:
            bullets.append(Bullet(screen, chars[currChar].x + 35, chars[currChar].y))
            pause += 1
        else:
            if pause == 15:
                pause = 0
            else:
                pause += 1


def resetSpeed():
    global chars, currChar
    chars[currChar].dY = 0
    chars[currChar].dX = 0


def drawBullets():
    global bullets
    for i in range(len(bullets)):
        bullets[i].draw()
        bullets[i].update()


def checkShots():
    global bullets, chars, currChar, running, enemy
    for i in range(len(bullets) - 1, -1, -1):
        if bullets[i].y < 0 or bullets[i].y > 700:
            bullets.remove(bullets[i])
        else:
            if bullets[i].dY == -10:
                for j in range(len(enemy) - 1, -1, -1):
                    if pygame.Rect.colliderect(bullets[i].getCollisionRect(), enemy[j].getCollisionRect()):
                        bullets.remove(bullets[i])
                        enemy.remove(enemy[j])
                        break
            else:
                if pygame.Rect.colliderect(bullets[i].getCollisionRect(), chars[currChar].getCollisionRect()):
                    running = False


def spawnEnemies():
    global enemy, screen

    enemy.append(EnemyOne('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))
    enemy.append(EnemyOne('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))
    enemy.append(EnemyOne('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))
    enemy.append(EnemyOne('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))
    enemy.append(EnemyOne('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))
    enemy.append(EnemyOne('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))
    enemy.append(EnemyTwo('galagaEnemyOne.png',
                          random.randint(0, pygame.Surface.get_width(screen)), 10, screen))


def updateEnemies():
    global enemy, screen

    for i in range(len(enemy)):
        enemy[i].update(screen)


def drawEnemies():
    global enemy, screen

    for i in range(len(enemy)):
        enemy[i].draw(screen)
        enemy[i].drawCollisionRect(screen)


def enemyShoot():
    global bullets, enemy
    for i in range(len(enemy)):
        rand = random.randint(1, 100)
        if rand == 1:
            bullets.append(Bullet(screen, enemy[i].x + 35, enemy[i].y + 55))
            bullets[len(bullets) - 1].dY = 5


startScreen()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    back.draw(screen)
    checkInput()
    checkShots()
    chars[currChar].draw(screen)
    chars[currChar].drawCollisionRect(screen)
    drawEnemies()
    chars[currChar].update(screen)
    updateEnemies()
    enemyShoot()
    drawBullets()
    resetSpeed()
    if len(enemy) == 0:
        level += 1
        spawnEnemies()

    pygame.display.flip()
    clock.tick(60)
