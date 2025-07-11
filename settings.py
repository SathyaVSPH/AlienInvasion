import pygame

class Settings:
    
    def __init__(self):
        
        #Screen Settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_colour = (230, 230, 230)
        
        #Ship Settings
        self.ship_speed = 2.5
        self.ship_limit = 2

        #Bullet Settings
        self.bullet_colour = (60, 60, 60)
        self.bullet_width = 4
        self.bullet_height = 12
        self.max_bullets = 7

        #Alien Settings
        self.alien_down_speed = 0.2
        self.alien_fleet_direction = 1 #1 for towards right and -1 for left
        
        self.speedup_scale = 1.5
        self.intialise_dynamic_settings()

        #Score Settings
        self.alien_points = 10
        self.score_levelup = 10

    def intialise_dynamic_settings(self):
        '''Initialise Dynamic Settings'''
        self.bullet_speed = 7
        self.alien_speed = 3
        
        #self.ship_speed
