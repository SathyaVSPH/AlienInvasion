import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard:
    '''This class handles all the tasks related to scores'''

    def __init__(self, ai_obj):
        '''Instantiating an instance here'''
        self.ai_obj = ai_obj
        self.screen = ai_obj.screen
        self.screen_rect = self.screen.get_rect()
        self.game_stat = ai_obj.gameStat
        self.settings = ai_obj.settings

        self.font_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_highscore()
        self.prep_level_display()
        self.prep_ship()

        
        
        
    def prep_ship(self):
        self.ships = Group()

        for ship_number in range(0, self.game_stat.ship_remaining + 1):
            ship = Ship(self.ai_obj)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def prep_score(self):
        rounded_score = round(self.game_stat.score, -1)
        score = str(f'{rounded_score:,}')
    
        self.score_image = self.font.render(score, True, self.font_colour, self.settings.bg_colour)
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.top = 20
        self.score_image_rect.right = self.settings.screen_width - 20

    def prep_highscore(self):
        self.high_score = str(self.game_stat.high_score)
        self.high_score_image = self.font.render(f'High Score: {self.high_score}', True, self.font_colour, self.settings.bg_colour)
        self.high_score_image_rect = self.high_score_image.get_rect()

        #positioning @ center
        self.high_score_image_rect.midtop = self.screen_rect.midtop

    #def draw_sb(self):
    def check_highscore(self):
        if self.game_stat.score >= self.game_stat.high_score:
            self.game_stat.high_score = self.game_stat.score
            self.prep_highscore()
    
    #def draw_highsb(self):

    def prep_level_display(self):
        self.level_display_img = self.font.render(f'Level: {self.settings.current_level}', True, self.font_colour, self.settings.bg_colour)
        self.level_display_img_rect = self.level_display_img.get_rect()

        #positioning the display
        self.level_display_img_rect.right = self.score_image_rect.right
        self.level_display_img_rect.top = self.score_image_rect.bottom + 10

    def draw_score(self):
        '''Draw scores and current level'''
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_display_img, self.level_display_img_rect)
        self.ships.draw(self.screen)