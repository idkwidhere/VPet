import pygame


class statsMenu():
    def __init__(self, screen):
        self.w = 160
        self.h = 120
        self.screen = screen
        self.menu_rect = pygame.Surface((self.w, self.h))
        self.open = False

    def draw(self):
        self.menugroup = pygame.sprite.Group()
        self.screen.blit(self.menu_rect, (40, 20))
        #self.screen.blit(self.menu_rect, (40, 20))
    #   self.menu_rect(self.screen, (255, 255, 255), [40, 20, self.w, self.h])

    def destroy(self):
        self.menugroup.clear(self.screen)