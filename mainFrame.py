import sys
from telnetlib import SE
import pygame
from settings import Settings

#   This is the main frame of the 2D platform 
class mainFrame:
    def _init_(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))        
        self.backGroundColor = self.settings.bgColor  
        pygame.display.set_caption("2D Platform")
 # you can choose every color you like  
    def run_game(self):
        while True: # create keyboard and mouse listener
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # reprint the screen in each loop
            self.screen.fill(self.settings.backGroundColor)
            # make the main frame visualable
            pygame.display.flip()       




