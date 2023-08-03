import pygame, sys
from cutscenes import CutSceneManager, EggHatch
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


#########################MONS##########################
from random import randint

class Egg():
    def __init__(self):
        self.lifespan = 15
        self.stage = 0

        sprite = pygame.image.load('assets/mons/egg/egg00.png')
        self.sprite = pygame.transform.scale(sprite, (64, 64))
        self.rect = self.sprite.get_rect()
        self.rect.topleft = [20, 20]
        

class Baby():
    def __init__(self):
        self.lifespan = 15
        self.stage = 1
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        if randint(0, 100) > 50:
            self.sex = "Male"
        else:
            self.sex = "Female"
        self.items = ["rattle"]

        sprite = pygame.image.load('./assets/mons/goobermon/goobermon0.png')
        self.sprite = pygame.transform.scale(sprite, (64, 64))

class Toddler():
    def __init__(self, sex, items):
        self.lifespan = 60
        self.stage = 2
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

class Teen():
    def __init__(self, sex, items):
        self.lifespan = 15 
        self.stage = 3
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

class Adult():
    def __init__(self, sex, items):
        self.lifespan = 15
        self.stage = 4
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

class Elder():
    def __init__(self, sex, items):
        self.lifespan = 15
        self.stage = 5
        self.happiness = 0
        self.max_happiness = 10
        self.hunger = 0
        self.max_hunger = 10
        self.sex = sex
        self.items = items

#########################ENDMONS#######################


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
                #pygame.mixer.Sound.play(button_sound)
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

#hatching new egg
def hatch(stage):
    if stage == None:
        print("You got an egg?!")
        newmon = Egg()
        return newmon
    

csm = CutSceneManager(screen)

def evolve(stage):
    match stage:
        case 0:
            print("evolve to a baby")
            csm.start_cutscene(EggHatch(mymon))
            return Baby()
        case 1:
            print("evolve to a toddler")
            return Toddler(mymon.sex, mymon.items)
        case 2:
            print("evolve to a teen")
            return Teen(mymon.sex, mymon.items)
        case 3:
            print("evolve to an adult")
            return Adult(mymon.sex, mymon.items)
        case 4:
            print("evolve to an elder")
            return Elder(mymon.sex, mymon.items)
        case 5:
            print("You died!")
            running = False


stage = None

running = True
while running:

    screen.fill((119, 186, 128))
    screen.blit(background, (0,0))


    #draw buttons
    stats_button.draw()
    eat_button.draw()
    shop_button.draw()


    #age/hatch checks
    if stage == None:
            print("You hatched a new egg!")
            mymon = Egg()
            stage = mymon.stage
            pygame.time.set_timer(pygame.USEREVENT, 1000)
            cycle = mymon.lifespan

    #decrease happiness over time


    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                cycle -= 1
                print(cycle)

                if cycle <= 0:
                    mymon = evolve(mymon.stage)
                    print(mymon.sex, mymon.items)
                    cycle = mymon.lifespan
                        
    screen.blit(mymon.sprite, (20, 20))

    #print(cycle)
    #print(stage)

    pygame.display.update()
    clock.tick(30)