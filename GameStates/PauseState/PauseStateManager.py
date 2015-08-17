import pygame
from GameStates import GameStates
from GameStates.PauseState import PauseDisplay

class PauseStateManager(object):
	
	def __init__(self, screen):
		self.display = PauseDisplay.PauseDisplay(screen)
	
	def tick(self):
		self.display.updateScreen()
	
	def handleEvent(self, event):
		if isPKeyPressed(event):
			transitionToGame()
			
	def reset(self):
		self.display.resetOverlayFlag()
		
def isPKeyPressed(event):
	return (pygame.KEYDOWN == event.type) and (pygame.key.get_pressed()[pygame.K_p])
	
def transitionToGame():
	raise GameStates.StateTransition(GameStates.GameState.PLAYING)