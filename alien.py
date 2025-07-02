import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''This class creates an alien'''

    def __init__(self, ai_obj):
        super().__init__()

        #initialising the screen and other attributes to an alien object
        self.alien_screen = ai_obj.screen
        self.alien_settings = ai_obj.settings

        '''Since we're using sprite's default draw method, we should implement image and rect 
        rather than our own attribute names'''
        #providing alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #positioning the alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #converting x attribute to float for facilitating speed control
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
    
    def update(self):
        self.x += self.alien_settings.alien_speed
        self.rect.x = self.x
        