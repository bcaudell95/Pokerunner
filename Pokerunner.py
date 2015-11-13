import pygame
from GameStates.GameStates import GameState
from GameStates.GameStates import StateTransition
from GameStates.GamePlayingState.GamePlayingStateManager import GamePlayingStateManager
from GameStates.MainMenuState.MainMenuStateManager import MainMenuStateManager
from GameStates.CreditsState.CreditsStateManager import CreditsStateManager
from GameStates.PauseState.PauseStateManager import PauseStateManager
from GUI import GuiConfig

pygame.init()


class Pokerunner:
	SCREEN = pygame.display.set_mode(GuiConfig.screenSize)
	FRAMES_PER_SECOND = 30
	stateManagersDict = {
		GameState.MAIN_MENU: MainMenuStateManager(SCREEN),
		GameState.PLAYING: GamePlayingStateManager(SCREEN),
		GameState.PAUSED: PauseStateManager(SCREEN),
		GameState.CREDITS: CreditsStateManager(SCREEN)
	}

	def __init__(self):
		self.clock = pygame.time.Clock()
		self.gameState = GameState.MAIN_MENU
		self.manager = Pokerunner.stateManagersDict[GameState.MAIN_MENU]

		self.gameExit = False

		self.startMainLoop()

	def startMainLoop(self):
		while not self.gameExit:
			self.iterateMainLoop()
		self.endGame()

	def iterateMainLoop(self):
		try:
			self.handleEvents()
			self.manager.tick()
			pygame.display.update()
			self.clock.tick(Pokerunner.FRAMES_PER_SECOND)
		except StateTransition as e:
			self.transitionTo(e.stateToTransitionTo)

	def handleEvents(self):
		for event in pygame.event.get():
			self.handleEvent(event)

	def handleEvent(self, event):
		if isEventQuit(event):
			self.gameExit = True
		else:
			self.sendEventToManager(event)

	def sendEventToManager(self, event):
		self.manager.handleEvent(event)

	def transitionTo(self, state):
		self.manager.reset()
		self.manager = Pokerunner.stateManagersDict[state]

	def endGame(self):
		pygame.quit()
		quit()


def isEventQuit(event):
	return event.type == pygame.QUIT


Pokerunner()
