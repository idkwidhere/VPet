import pygame, sys
import mons
from random import randrange

pygame.init()

# window settings
SCREEN_WIDTH = 240
SCREEN_HEIGHT = 196
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("vPet v1.0a")
#pygame.display.set_icon("icon.png")
background = pygame.image.load('./assets/backgrounds/background.png')

# game settings
clock = pygame.time.Clock()


#text function
font = pygame.font.SysFont("arialblack", 10)
TEXT_COLOR = (255, 255, 255)
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

######################BUTTONS######################
#button images
status = pygame.image.load("./assets/buttons/stats.png")
status_hover = pygame.image.load("./assets/buttons/stats_hover.png")

eat = pygame.image.load("./assets/buttons/eat.png")
eat_hover = pygame.image.load("./assets/buttons/eat_hover.png")

shop = pygame.image.load("./assets/buttons/shop.png")
shop_hover = pygame.image.load("./assets/buttons/shop_hover.png")


class Button():
    def __init__(self, x, y, image, image_hover, action):
        self.image = image
        self.image_hover = image_hover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.action = action

    def draw(self):
        pos = pygame.mouse.get_pos()
        
        # check for hover
        if self.rect.collidepoint(pos):
            
            screen.blit(self.image_hover, (self.rect.x, self.rect.y))
            if(pygame.mouse.get_pressed()[0] == 1 and self.clicked == False):
                self.clicked = True
                pygame.mixer.Sound.play(button_sound)
                #action

            if(pygame.mouse.get_pressed()[0] == 0):
                self.clicked = False
        else:
            screen.blit(self.image, (self.rect.x, self.rect.y))


# create buttons for game
stats_button = Button(4, 162, status, status_hover, action="show_stats")
eat_button = Button(44, 162, eat, eat_hover, action="food_menu")
shop_button = Button(84, 162, shop, shop_hover, action="show_shop")
#4_button = Button(124, 162, status, status_hover, action="show_stats")
#5_button = Button(164, 162, status, status_hover, action="show_stats")
#6_button = Button(204, 162, status, status_hover, action="show_stats")

#sounds/music
button_sound = pygame.mixer.Sound('./assets/sounds/buttons.wav')


running = True
while running:

    screen.fill((119, 186, 128))
    screen.blit(background, (0,0))

    #draw buttons
    stats_button.draw()
    eat_button.draw()
    shop_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #check for age


    pygame.display.update()
    clock.tick(30)