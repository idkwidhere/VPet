import pygame, os


def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    screen.blit(surface, rect)


class CutSceneManager:

    def __init__(self, screen):
        self.cutscene_complete = []
        self.cutscene = None
        self.cutscene_running = False

        #drawing variables
        self.screen = screen
        self.window_size = 0
    
    def start_cutscene(self, cutscene):
        if(cutscene.name not in self.cutscene_complete):
            self.cutscene_complete.append(cutscene.name)
            self.cutscene = cutscene
            self.cutscene_running = True

    def end_cutscene(self):
        self.cutscene = None
        self.cutscene_running = False

    def update(self):
        if(self.cutscene_running):
            self.cutscene.update()
        else:
            self.end_cutscene()

    def draw(self):
        if(self.cutscene_running):
            self.cutscene.draw(self.screen)
            
class EggHatch:
    def __init__(self, mon):
        self.sprites = []
        i = 10
        for i in range(10, 17):
            self.sprites.append(pygame.image.load('./assets/cutscenes/evolve/evolve'+ str(i)+'.png'))
            i += 1
        self.csprite = 0
        self.image = self.sprites[self.csprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)




        self.name = "egg_hatch"
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cutsene_running = True

        self.mon = mon

        self.text = {
            'one': "Oh?",
            'two': "The egg hatched!"
        }
        self.text_counter = 0


    def update(self):

        pressed = pygame.mouse.get_pressed()[0]

        self.csprite += 1

        if self.csprite >= len(self.sprites):
            self.csprite = 0
        self.image = self.sprites[self.csprite]


        if pressed:
                self.cutsene_running = False

        # if self.step == 0:
        #     if(int(self.text_counter) < len(self.text['one'])):
        #         self.text_counter += 0.4
        #     else:
        #         if pressed:
        #             self.step = 1

        # if self.step == 1:
        #     if(int(self.text_counter) < len(self.text['two'])):
        #         self.text_counter += 0.4
        #     else:
        #         if pressed:
        #             self.cutsene_running = False

        return self.cutsene_running

    def draw(self, screen):
        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                10,
                (255, 255, 255),
                20, 20
            )
        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                10,
                (255, 255, 255),
                20, 20
            )