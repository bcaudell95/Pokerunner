import pygame
from GUI import images

class PauseDisplay(object):

    def __init__(self, screen):
        self.screen = screen
        self.overlayShown = False

    def updateScreen(self):
        if not self.overlayShown:  # We only blit the overlay once to preserve transparency
            self.drawBackground()

    def resetOverlayFlag(self):
        self.overlayShown = False

    def drawBackground(self):
        self.overlayShown = True
        self.drawImage(images.pauseScreenOverlay, (0, 0))

    def drawImage(self, image, coordinates):
        self.screen.blit(image, coordinates)
