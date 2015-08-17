import pygame
from GameStates import GameStates
from GameStates.GamePlayingState import GamePlayingStateManager
from GameStates.MainMenuState import MainMenuStateManager
from GameStates.PauseState import PauseStateManager
from GUI import GuiConfig

class Pokerunner:

	SCREEN = pygame.display.set_mode(GuiConfig.screenSize)
	FRAMES_PER_SECOND = 30
	stateManagersDict = { 
		GameStates.GameState.MAIN_MENU: MainMenuStateManager.MainMenuStateManager(SCREEN),
		GameStates.GameState.PLAYING : GamePlayingStateManager.GamePlayingStateManager(SCREEN),
		GameStates.GameState.PAUSED : PauseStateManager.PauseStateManager(SCREEN)
		}

	def __init__(self):
		pygame.init()

		self.clock = pygame.time.Clock()
		self.gameState = GameStates.GameState.MAIN_MENU
		self.manager = Pokerunner.stateManagersDict[GameStates.GameState.MAIN_MENU]

		self.gameExit = False
		
		self.startMainLoop()

	def startMainLoop(self):
		while not self.gameExit:
			self.iterateMainLoop()
		self.endGame()
		
	def iterateMainLoop(self):
		self.handleEvents()
		
		self.manager.tick()
		pygame.display.update()
		
		self.clock.tick(Pokerunner.FRAMES_PER_SECOND)
			
	def handleEvents(self):
		for event in pygame.event.get():
			self.handleEvent(event)
			
	def handleEvent(self, event):
		if isEventQuit(event):
			self.gameExit = True
		else:
			self.sendEventToManager(event)
	
	def sendEventToManager(self, event):
		try:
			self.manager.handleEvent(event)
		except GameStates.StateTransition as e:
			self.transitionTo(e.stateToTransitionTo)
	
	def transitionTo(self, state):
		self.manager.reset()
		self.manager = Pokerunner.stateManagersDict[state]
	
	def endGame(self):
		pygame.quit()
		quit()

def isEventQuit(event):
	return event.type == pygame.QUIT
		
Pokerunner()