import pygame.font
#from game_stats import GameStat

class ScoreBoard:
    '''This class handles all the tasks related to scores'''

    def __init__(self, ai_obj):
        self.screen = ai_obj.screen
        self.screen_rect = self.screen.get_rect()
        self.game_stat = ai_obj.gameStat
        self.settings = ai_obj.settings

        self.font_colour = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_highscore()
        
    def prep_score(self):
        rounded_score = round(self.game_stat.score, -1)
        score = str(f'{rounded_score:,}')
    
        self.score_image = self.font.render(score, True, self.font_colour, self.settings.bg_colour)
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.top = 20
        self.score_image_rect.right = self.settings.screen_width - 20

    def prep_highscore(self):
        self.high_score = str(self.game_stat.high_score)
        self.high_score_image = self.font.render(self.high_score, True, self.font_colour, self.settings.bg_colour)
        self.high_score_image_rect = self.high_score_image.get_rect()

        #positioning @ center
        self.high_score_image_rect.midtop = self.screen_rect.midtop

    #def draw_sb(self):
    def check_highscore(self):
        if self.game_stat.score >= self.game_stat.high_score:
            self.game_stat.high_score = self.game_stat.score
            self.prep_highscore()
    
    #def draw_highsb(self):
        

    def draw_score(self):
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)