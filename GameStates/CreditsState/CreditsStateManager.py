import pygame
from GameStates.CreditsState.CreditsDisplay import CreditsDisplay


class CreditsStateManager(object):
    def __init__(self, screen):
        self.display = CreditsDisplay(screen)

    def tick(self):
        self.display.updateScreen()

    def handleEvent(self, event):
        pass

    def reset(self):
        pass
