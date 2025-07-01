import pygame

'''This module handles all the functions related to ship image'''
class Ship:

    def __init__(self, ai_obj):
        '''Providing the screen and rect to the ship'''
        self.ship_screen = ai_obj.screen
        self.ship_screen_rect = self.ship_screen.get_rect()
        
        '''Providing the image and rect to the ship object'''
        self.ship_image = pygame.image.load('images/ship.bmp')
        self.ship_image_rect = self.ship_image.get_rect()

        '''Positioning the ship object at the midbottom of the screen'''
        self.ship_image_rect.midbottom = self.ship_screen_rect.midbottom

        '''Adding the movement flag'''
        self.moving_up = False
        self.mvoing_down = False
        self.moving_left = False
        self.moving_right = False
    
    def update_ship(self):
        '''Adds the ability to move the ship'''
        if self.moving_up:
            self.ship_image_rect.y -= 1
        if self.mvoing_down:
            self.ship_image_rect.y += 1
        if self.moving_left:
            self.ship_image_rect.x -= 1
        if self.moving_right:
            self.ship_image_rect.x += 1

    def blitme(self):
        '''Drawing the ship over the surface'''
        self.ship_screen.blit(self.ship_image, self.ship_image_rect)



