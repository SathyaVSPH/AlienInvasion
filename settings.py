import pygame

class Settings:
    
    def __init__(self):
        
        #Screen Settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_colour = (230, 230, 230)
        
        #Ship Settings
        self.ship_speed = 2.5

        #Bullet Settings
        self.bullet_colour = (60, 60, 60)
        self.bullet_width = 4
        self.bullet_height = 12
        self.bullet_speed = 4
        
