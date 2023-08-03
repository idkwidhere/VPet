import pygame

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    screen.blit(surface, rect)


class statsMenu():
    def __init__(self, screen, currentmon):
        self.w = 160
        self.h = 120
        self.screen = screen
        self.open = False
        self.info = currentmon

        self.rect = pygame.Rect(40, 20, self.w, self.h)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        draw_text(self.screen, "Happiness: " + str(self.info.happiness), 20, (0,0,0), 45, 25)
        draw_text(self.screen, "Hunger: " + str(self.info.hunger), 20, (0,0,0), 45, 40)


class foodMenu():
    def __init__(self, screen, hunger, items):
        self.hunger = hunger
        self.items = items
        self.screen = screen
        self.w = 160
        self.h = 120
        self.open = False

        self.rect = pygame.Rect(40, 20, self.w, self.h)


    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

        draw_text(self.screen, "Meals: ", 20, (0,0,0), 45, 25)
