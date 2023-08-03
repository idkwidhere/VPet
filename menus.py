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
        draw_text(self.screen, str(self.info.happiness), 20, (0,0,0), 10, 10)
