import pygame
from GameStates import GameStates
from GameStates.GamePlayingState import GamePlayingStateManager
from GameStates.MainMenuState import MainMenuStateManager
from GUI import GuiConfig

class Pokerunner:

	SCREEN = pygame.display.set_mode(GuiConfig.screenSize)
	FRAMES_PER_SECOND = 30
	stateManagersDict = { 
		GameStates.GameState.MAIN_MENU: MainMenuStateManager.MainMenuStateManager(SCREEN),
		GameStates.GameState.PLAYING : GamePlayingStateManager.GamePlayingStateManager(SCREEN) 
		}

	def __init__(self):
		pygame.init()

		self.clock = pygame.time.Clock()
		self.gameState = GameStates.GameState.MAIN_MENU
		self.manager = Pokerunner.stateManagersDict[GameStates.GameState.MAIN_MENU]

		self.gameExit = False
		
		self.mainLoop()

	def mainLoop(self):
		while not self.gameExit:
			self.handleEvents()
			
			self.manager.tick()
			pygame.display.update()
			
			self.clock.tick(Pokerunner.FRAMES_PER_SECOND)
			
	def handleEvents(self):
		for event in pygame.event.get():
			if isEventQuit(event):
				self.gameExit = True
			else:
				try:
					self.manager.handleEvent(event)
				except GameStates.StateTransition as e:
					self.transitionTo(e.stateToTransitionTo)
	
	def transitionTo(self, state):
		self.manager = Pokerunner.stateManagersDict[state]
	
	def endGame(self):
		pygame.quit()
		quit()

def isEventQuit(event):
	return event.type == pygame.QUIT
		
Pokerunner()