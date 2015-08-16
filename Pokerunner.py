import pygame
from GameStates.GamePlayingState import GamePlayingStateManager
from GameStates.MainMenuState import MainMenuStateManager
from enum import Enum

class GameState(Enum):
	MAIN_MENU = 0
	PLAYING = 1
	PAUSED = 2
	CREDITS = 3

class Pokerunner:

	FRAMES_PER_SECOND = 30

	def __init__(self):
		pygame.init()

		self.clock = pygame.time.Clock()
		self.gameState = GameState.MAIN_MENU
		self.manager = GamePlayingStateManager.GamePlayingStateManager()

		self.gameExit = False
		
		self.mainLoop()

	def mainLoop(self):
		while not self.gameExit:
			self.handleEvents()
			
			self.manager.tick()
			
			self.clock.tick(Pokerunner.FRAMES_PER_SECOND)
			
	def handleEvents(self):
		for event in pygame.event.get():
			if isEventQuit(event):
				self.gameExit = True
			else:
				self.manager.handleEvent(event)
					
	def endGame(self):
		pygame.quit()
		quit()

def isEventQuit(event):
	return event.type == pygame.QUIT
		
Pokerunner()