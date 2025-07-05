import pygame
from settings import Settings

'''This module handles all the functions related to ship image'''

class Ship:
    def __init__(self, ai_obj):
        '''Providing the screen and rect to the ship'''
        self.ship_screen = ai_obj.screen
        self.ship_screen_rect = self.ship_screen.get_rect()
        
        '''Providing the image and rect to the ship object'''
        self.ship_image = pygame.image.load('images/ship.bmp')
        self.rect = self.ship_image.get_rect()

        '''Positioning the ship object at the midbottom of the screen'''
        self.rect.midbottom = self.ship_screen_rect.midbottom

        '''Adding the movement flag'''
        self.moving_up = False
        self.mvoing_down = False
        self.moving_left = False
        self.moving_right = False

        '''Initialising Settings'''
        self.ship_settings = Settings()
    
        '''Converting to float to change the speed'''
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_ship(self):
        '''Adds the ability to move the ship'''
        if self.moving_up and self.rect.top > 0:
            #self.ship_image_rect.y -= 1
            self.y -= self.ship_settings.ship_speed

        if self.mvoing_down and self.rect.bottom < self.ship_screen_rect.bottom:
            #self.ship_image_rect.y += 1
            self.y += self.ship_settings.ship_speed
            
        if self.moving_left and self.rect.x > 0:
            #self.ship_image_rect.x -= 1
            self.x -= self.ship_settings.ship_speed

        if self.moving_right and self.rect.right < self.ship_screen_rect.right:
            #self.ship_image_rect.x += 1
            self.x += self.ship_settings.ship_speed

        '''Assigning back the values to the required variable'''
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def blitme(self):
        '''Drawing the ship over the surface'''
        self.ship_screen.blit(self.ship_image, self.rect)



