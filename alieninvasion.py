import sys, pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''This class handles all the events related to this game'''
    
    def __init__(self):

        '''Initialising Settings'''
        self.settings = Settings()

        '''Initialising the screen attributes for the objects'''
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        '''Initiating the ship and providing the necessary resources'''
        self.ship = Ship(self)

        '''Initialising the clock to lock frame rate'''
        self.clock = pygame.time.Clock()


    def runGame(self):
        '''Game runs by executing the while loop'''
        while True:
            '''each event only represents one event'''
            self._check_events()

            '''Updates the position of the ship at each instance'''
            self.ship.update_ship()
            
            '''Updates the screen with the changes'''
            self._update_screen()    
            
            '''Capping to 60 fps'''
            self.clock.tick(60)
    
    
    def _update_screen(self):
        
        '''Fills the screen with given colour'''
        self.screen.fill(self.settings.bg_colour)

        '''Positioning ship'''
        self.ship.blitme()

        '''Draws the changes in the screen'''
        pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)


    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.mvoing_down = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_q:
            sys.exit()
    

    def _keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.mvoing_down = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()