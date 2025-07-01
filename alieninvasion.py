import sys, pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


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

        '''Instantiating the bullets via sprite'''
        self.bullets = pygame.sprite.Group()

        '''Initialising the clock to lock frame rate'''
        self.clock = pygame.time.Clock()


    def runGame(self):
        '''Game runs by executing the while loop'''
        while True:
            '''each event only represents one event'''
            self._check_events()

            '''Updates the position of the ship at each iteration'''
            self.ship.update_ship()
            
            '''Updates the positon of the bullets at each iteration'''
            self.bullets.update()

            '''Remove bullets outside territory'''
            self._remove_bullets()
            
            '''Updates the screen with the changes'''
            self._update_screen()    
            

            '''Capping to 60 fps'''
            self.clock.tick(60)
    
    def _fire_bullets(self):
        #instantiating a bullet from the Bullet Class
        new_bullet = Bullet(self)
        #adding the new bullet with its attributes into the self.bullets container
        self.bullets.add(new_bullet)

    def _remove_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.bullet_rect.bottom <= 0:
                self.bullets.remove(bullet)
            #print(len(self.bullets))


    def _update_screen(self):
        
        '''Fills the screen with given colour'''
        self.screen.fill(self.settings.bg_colour)

        '''Positioning ship'''
        self.ship.blitme()

        #we are looping over the added bullets to draw the bullets in the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

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
        if event.key == pygame.K_SPACE:
            self._fire_bullets()
    

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