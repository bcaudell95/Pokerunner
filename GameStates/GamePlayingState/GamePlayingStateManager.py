import pygame
from GameStates.GameStates import GameState, StateTransition
from GameStates.GamePlayingState.GamePlayingDisplay import GamePlayingDisplay
from Entities.PlayerEntity import PlayerEntity, MovementStates, PlayerHealthEmptyException
from Entities.EntityManager import EntityManager
from MainConfig import Elements
from GUI import GuiConfig


class GamePlayingStateManager(object):
	SCORE_DELTA = 10

	def __init__(self, screen):
		self.display = GamePlayingDisplay(screen)
		self.setUpEntityManager()
		self.player = self.entityManager.getPlayerEntity()
		self.display.setHealthQuery(self.player.getHealth)
		self.score = 0

	def tick(self):
		try:
			self.entityManager.updateAll()
			self.entityManager.checkForCollisions()
			self.incrementScore()
			self.display.setScore(self.getScore())
			self.display.updatePlayerData(self.player.getCurrentPlayerState())
			self.display.updateScreen(self.entityManager.getAllEntitiesToDraw())
		except PlayerHealthEmptyException:
			gameOver()

	def handleEvent(self, event):
		if self.isEventKeyDown(event):
			self.handleKeyEvent(event)

	def isEventKeyDown(self, event):
		return event.type == pygame.KEYDOWN

	def handleKeyEvent(self, event):
		if event.key == pygame.K_UP:
			self.player.changeMovementState(MovementStates.JUMPING)
		elif event.key == pygame.K_p:
			transitionToPaused()
		elif event.key == pygame.K_1:
			self.player.setElement(Elements.NORMAL)
		elif event.key == pygame.K_2:
			self.player.setElement(Elements.FIRE)

	def reset(self):
		pass

	def incrementScore(self):
		self.score += GamePlayingStateManager.SCORE_DELTA

	def getScore(self):
		return self.score

	def spwawnObstacle(self):
		self.entityManager.spawnBasicObstacleObstacle()

	def setUpEntityManager(self):
		self.entityManager = EntityManager()
		EntityManager.GEOSTATIONARY_START_COORDS = (GuiConfig.screenSize[0], GuiConfig.floorY)
		EntityManager.GEOSTATIONARY_SPEED = GamePlayingDisplay.playerSpeedX
		self.entityManager.addPlayerEntity(GamePlayingDisplay.playerDrawCoordinates)
		self.entityManager.spawnBasicObstacle()


def transitionToPaused():
	raise StateTransition(GameState.PAUSED)
	
def gameOver():
	raise StateTransition(GameState.CREDITS)
