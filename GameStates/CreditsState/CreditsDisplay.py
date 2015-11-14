import pygame
from GUI.Button import Button
from GUI import images
from GameStates.GameStates import GameState, StateTransition


class CreditsDisplay(object):

    def __init__(self, screen):
        self.screen = screen

    def updateScreen(self):
        self.drawBackground()

    def drawBackground(self):
        self.drawImage(images.creditsBackdropImage, (0, 0))
		
    def drawImage(self, image, coordinates):
        self.screen.blit(image, coordinates)
