import pygame.font

class Button:
    '''Manages all the methods and attributes related to buttons'''
    def __init__(self, ai_obj, msg):
        self.screen = ai_obj.screen
        self.screen_rect = self.screen.get_rect()

        '''Button attributes'''
        self.width, self.height = 200, 50
        self.bg_colour = (0, 135, 0)
        self.font_colour = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Converting the msg into image'''
        self.msg_image = self.font.render(msg, True, self.font_colour, self.bg_colour)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Places the button on the center of the screen'''
        self.screen.fill(self.bg_colour, self.rect) #Fills the button with the colour
        self.screen.blit(self.msg_image, self.msg_image_rect)
