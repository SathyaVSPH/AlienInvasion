import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_obj):

        super().__init__()

        #providing the screen and settings to the bullet object
        self.bullet_screen = ai_obj.screen
        self.bullet_settings = ai_obj.settings

        #creating the bullet
        self.bullet_rect = pygame.Rect(0, 0, self.bullet_settings.bullet_width, self.bullet_settings.bullet_height)
        
        #placing the bullet at the top center of the ship
        self.bullet_rect.midtop = ai_obj.ship.ship_image_rect.midtop

        #store the bullet speed in float
        self.y = float(self.bullet_rect.y)

    def update_bullet(self):
        '''Updating the bullet position according to speed'''
        self.y -= self.bullet_settings.bullet_speed

        #restoring the bullet speed
        self.bullet_rect.y = int(self.y)

    def draw_bullet(self):
        '''Draw the bullet at the given position'''
        pygame.draw.rect(self.bullet_screen, self.bullet_settings.bullet_colour, self.bullet_rect)

