import pygame 

class craft:

    def __init__(self, mainFrame):

        self.screen = mainFrame.screen
        self.screen_rect = mainFrame.screen.get_rect()
        # locd the craft image and its outer rectangle
        self.image = pygame.image.load(r'D:/Users/VSCode/Py_Project/2DAirCraft/ship.bmp')
        self.rect = self.image.get_rect()

        # find the position to put the craft
        self.rect.midbuttom = self.csreen_rect.midbuttom
