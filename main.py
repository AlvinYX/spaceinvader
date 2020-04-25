import sys
import pygame
import random

# Initialize the pygame
pygame.init()

# Creates the display
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background2.jpg')

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player Image
playerImg = pygame.image.load('spaceship.png')
playerX = 362
playerY = 480
playerX_change = 0

# Enemy Image
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(40, 125)
enemyX_change = 2
enemyY_change = 35

# Bullet Image
bulletImg = pygame.image.load('bullet')


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Game Loop
# running = True
while True:

    screen.fill((64, 27, 19))  # RGB Background
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if keystroke is pressed check whether it's left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                playerX_change = -4
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                playerX_change = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT or event.key == ord('a') or event.key == ord('d'):
                playerX_change = 0

    # Checking for boundaries, and keeping spaceship in bound

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
