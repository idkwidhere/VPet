import pygame, sys

pygame.init()

# window settings
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 160
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# game settings


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
