import pygame
from GameStates import GameStates

class PauseDisplay(object):
	PAUSE_IMAGE_FILE = 'assets/images/Pause.png'
	
	def __init__(self, screen):
		self.screen = screen
		self.pauseScreenOverlay = pygame.image.load(PauseDisplay.PAUSE_IMAGE_FILE).convert_alpha()
		self.overlayShown = False
	
	def updateScreen(self):
		if not self.overlayShown: #We only blit the overlay once to preserve transparency
			self.drawBackground()
			
	def resetOverlayFlag(self):
		self.overlayShown = False
		
	def drawBackground(self):
		self.overlayShown = True
		self.drawImage(self.pauseScreenOverlay, (0,0))
		
	def drawImage(self, image, coordinates):
		self.screen.blit(image, coordinates)