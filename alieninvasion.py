import sys, pygame

class AlienInvasion:

    def __init__(self):
        '''Initialising the screen attributes for the objects'''
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Alien Invasion')

    def runGame(self):
        '''Game runs by executing the while loop'''
        while True:
            '''each event only represents one event'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()