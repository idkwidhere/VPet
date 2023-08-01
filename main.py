import pygame, sys
import mons, buttons
from random import randrange

pygame.init()

# window settings
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 160
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("vPet v1.0a")
#pygame.display.set_icon("icon.png")

# game settings
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(30)