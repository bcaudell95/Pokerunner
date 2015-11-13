import pygame
from GUI.Button import Button
from GameStates.GameStates import GameState, StateTransition


class CreditsDisplay(object):
    BACKGROUND_IMAGE_FILE = 'assets/images/GameOver.png'
    BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_IMAGE_FILE)

    def __init__(self, screen):
        self.screen = screen

    def updateScreen(self):
        self.drawBackground()

    def drawBackground(self):
        self.drawImage(CreditsDisplay.BACKGROUND_IMAGE, (0, 0))
		
    def drawImage(self, image, coordinates):
        self.screen.blit(image, coordinates)
