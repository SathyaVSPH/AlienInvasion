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

        
        score = str(self.game_stat.score)
        self.score_image = self.font.render(score, True, self.font_colour, self.settings.bg_colour)
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.top = 20
        self.score_image_rect.right = self.settings.screen_width - 20

    def draw_sb(self):
        self.screen.blit(self.score_image, self.score_image_rect)