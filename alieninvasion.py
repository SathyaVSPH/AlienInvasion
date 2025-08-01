import sys, pygame
from settings import Settings
from game_stats import GameStat
from scoreboard import ScoreBoard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep


class AlienInvasion:
    '''This class handles all the events related to this game'''
    
    def __init__(self):

        '''Initialising Settings'''
        pygame.init()
        self.settings = Settings()

        '''Initialising the screen attributes for the objects'''
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        '''Instantiating the stats before the other game elements.'''
        self.gameStat = GameStat(self)

        '''Instantiating Scoreboard'''
        self.sb = ScoreBoard(self)

        #Game State
        self.gameActive = False

        """Instantiating play button"""
        self.play_button = Button(self, 'Play')

        '''Initiating the ship and providing the necessary resources'''
        self.ship = Ship(self)

        '''Instantiating the bullets via sprite'''
        self.bullets = pygame.sprite.Group()

        '''Instantitating the alien via sprite'''
        self.aliens = pygame.sprite.Group()
        self._create_aliens()
        
        '''Initialising the clock to lock frame rate'''
        self.clock = pygame.time.Clock()


    def runGame(self):
        '''Game runs by executing the while loop'''
        while True:
            '''each event only represents one event'''
            self._check_events()

            if self.gameActive:

                '''Updates the position of the ship at each iteration'''
                self.ship.update_ship()
                
                '''Updates the positon of the bullets at each iteration'''
                self.bullets.update()
                
                #This removes the aliens that have been hit by the bullets
                collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

                if collisions:
                    for aliens in collisions.values():
                        self.gameStat.score += self.settings.alien_points * len(aliens)
                        self.sb.prep_score()
                        self.sb.check_highscore()

                #Adding aliens if the fleet is empty
                if not self.aliens:
                    self.bullets.empty() #Destroy the existing bullets in sprite
                    self._create_aliens()
                    self._increase_speed()
                    self._increase_score()
                    self.settings.current_level += 1
                    self.sb.prep_level_display()

                #Updates the position of the aliens
                self._update_aliens()

                '''Remove bullets outside territory'''
                self._remove_bullets()
            
            #create aliens fleet. This must be placed in init to prevent recreating the fleets 60 times per iteration
            #self._create_aliens()

            '''Updates the screen with the changes'''
            self._update_screen()    
            
            '''Capping to 60 fps'''
            self.clock.tick(60)

    def _increase_speed(self):
        '''Increase difficulty'''
        self.settings.alien_speed *= self.settings.speedup_scale
        self.settings.bullet_speed *= self.settings.speedup_scale

    def _increase_score(self):
         self.settings.alien_points *= self.settings.score_levelup

    def _reset_game(self):
        if self.gameStat.ship_remaining > 0:
            self.gameStat.ship_remaining -= 1
            self._reset_components()
        else:
            self.gameActive = False
            self.sb.prep_score()
            self.sb.check_highscore()
            self.sb.prep_highscore()
            self.gameStat.reset_stat()
            pygame.mouse.set_visible(True)

    def _reset_components(self):
        self.aliens.empty()
        self.bullets.empty()
        self._create_aliens()
        self.ship.repos_ship()
        sleep(0.5) #Pause
        #print('Ship hit!!!')

    def _update_aliens(self):
        self._fleet_edge_check()
        self.aliens.update()
        self._collision_check()

        
    def _collision_check(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._reset_game()
            self.sb.prep_ship()
            
        for alien in self.aliens.sprites(): #aliens reaching bottom
            if alien.rect.bottom >= self.settings.screen_height:
                self._reset_game()
                break

    def _fleet_edge_check(self):

        for alien in self.aliens.sprites():
            if alien.edge_check:
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.y += self.settings.alien_down_speed
            alien.rect.y = alien.y
        self.settings.alien_fleet_direction *= -1

    def _create_aliens(self):
        #instantiating the first alien
        first_alien = Alien(self)
        
        #assigning the width and height of the alien rectangle
        first_alien_width, first_alien_height = first_alien.rect.size

        #initiating current positions for the while loop
        current_x, current_y = first_alien_width, first_alien_height
        
        while current_y < (self.settings.screen_height - 4 * first_alien_height):

            while current_x < (self.settings.screen_width - 2*first_alien_width):
                '''This conditon helps in preventing the alien to be placed at the right most edge'''
                #refactoring

                #places the alien horizontally            
                self._aliens_fleet(current_x, current_y)

                #incrementing so that each alien is spaced with a gap of alien's width
                current_x += 2 * first_alien_width
            current_x = first_alien_width
            current_y += 2 * first_alien_height


    def _aliens_fleet(self, current_x, current_y):
        #initiating the next alien
        new_alien = Alien(self)
            
        #positioning at the end of the first alien
        new_alien.x = current_x
        
        #positioning at the next line
        new_alien.y = current_y

        #positioning the rectangle at the end of the first alien
        new_alien.rect.x = current_x

        #positioning the rectange at the next line
        new_alien.rect.y = current_y

        #adding the new alien to the fleet
        self.aliens.add(new_alien)


    def _fire_bullets(self):
        if len(self.bullets) < self.settings.max_bullets:
            #instantiating a bullet from the Bullet Class
            new_bullet = Bullet(self)
            #adding the new bullet with its attributes into the self.bullets container
            self.bullets.add(new_bullet)


    def _remove_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
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

        #drawing the alien using default draw of sprite group
        self.aliens.draw(self.screen)

        '''Place the scoreboards'''
        self.sb.draw_score()

        #Play Button
        if not self.gameActive:
            self.play_button.draw_button()
            self.settings.intialise_dynamic_settings()
            self.sb.prep_ship()

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                button_clicked = self.play_button.rect.collidepoint(mouse_pos)#clicked play button
                if button_clicked and not self.gameActive:
                    self.gameStat.reset_stat()
                    self.gameActive = True
                    self._reset_components()
                    self.sb.prep_score()
                    pygame.mouse.set_visible(False)


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