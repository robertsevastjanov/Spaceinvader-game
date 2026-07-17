import pygame

# Initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("launch.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480

def player(x, y):
    screen.blit(playerImg, (x, y))


#Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((15, 30, 200))
    playerX += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX, playerY)
    pygame.display.update()
