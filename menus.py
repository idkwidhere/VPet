import pygame

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    screen.blit(surface, rect)


arrow_rightload = pygame.image.load('./assets/buttons/arrowright.png')
arrow_leftload = pygame.image.load('./assets/buttons/arrowleft.png')

class Button():
    def __init__(self, x, y, image, screen):
        self.image = image
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()
        
        # check for hover
        if self.rect.collidepoint(pos):
            if(pygame.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True

            if(pygame.mouse.get_pressed()[0] == 0):
                self.clicked = False
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
               

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
    def __init__(self, screen, hunger, food):
        self.hunger = hunger
        self.food = food
        self.screen = screen
        self.w = 160
        self.h = 120
        self.open = False

        self.rect = pygame.Rect(40, 20, self.w, self.h)
        self.left_arrow = Button(45, 115, arrow_leftload, self.screen)
        self.right_arrow = Button(160, 115, arrow_rightload, self.screen)


    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

        draw_text(self.screen, "Meals: ", 20, (0,0,0), 45, 25)

        for foods in self.food:
            draw_text(self.screen, str(foods), 20, (0,0,0), 45, 40)
        
        self.left_arrow.draw()
        self.right_arrow.draw()
