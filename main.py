import pygame
import random
import math

# Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.jpeg")

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("launch.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("invader.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(0,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

#Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (200, 200, 15))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY, 2))
    if distance < 27:
        return True
    else:
        return False
#Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((15, 30, 200))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":

                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Enemy movement
    for i in range (num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= -40:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 770:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(0, 150)

        enemy(enemyX[i], enemyY[i], i)

    #Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

