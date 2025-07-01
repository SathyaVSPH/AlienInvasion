import sys, pygame
from settings import Settings

class AlienInvasion:

    def __init__(self):

        '''Initialising Settings'''
        self.settings = Settings()

        '''Initialising the screen attributes for the objects'''
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        '''Initialising the clock to lock frame rate'''
        self.clock = pygame.time.Clock()

    def runGame(self):
        '''Game runs by executing the while loop'''
        while True:
            '''each event only represents one event'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            '''Fills the screen with given colour'''
            self.screen.fill(self.settings.bg_colour)
            pygame.display.flip()
            '''Capping to 60 fps'''
            self.clock.tick(60)
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()