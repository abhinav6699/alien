import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

#background
background = pygame.image.load("background.png")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("planet.png")
pygame.display.set_icon(icon)

#player
playerimg= pygame.image.load("spaceship.png")
playerX= 370
playerY= 480
playerX_change = 0
#enemy
enemyimg= pygame.image.load("enemy.png")
enemyX= random.randint(0,800)
enemyY= random.randint(50, 150)
enemyX_change = 3
enemyY_change = 0
#bullet
bulletimg = pygame.image.load("bullet.png")
bulletX= 0
bulletY= 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def player(x,y):
    screen.blit(playerimg, (x,y))

def enemy(x,y):
    screen.blit(enemyimg, (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x+16,y+10))

#gmae loop
running = True
while running:

    screen.fill((25, 25, 25))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#keystroke

        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY )
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX=736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += 40

    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += 40

#bullet movement
    if bullet_state == "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change
    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
