import pygame
from GUI import GuiConfig, images
from GameStates.GamePlayingState.GamePlayingBackdropManager import BackdropManager
from math import floor

pygame.font.init()


class GamePlayingDisplay:
	backdropSize = BackdropManager.getBackDropSize()
	floorY = GuiConfig.floorY

	playerDrawCoordinates = GuiConfig.playerDrawCoords
	playerSpeedX = 10

	scoreBorderImage = images.scoreBorderImage
	scoreBorderDimensions = GuiConfig.scoreBorderDimensions

	scoreFont = pygame.font.Font(GuiConfig.scoreFontFile, GuiConfig.scoreFontSizePts)
	scoreFontColor = GuiConfig.scoreFontColor
	scoreDrawCoords = GuiConfig.scoreDrawCoords

	def __init__(self, screen):
		self.backdropManager = BackdropManager(self.drawBackdrops)
		self.playerX = 0
		self.score = 0
		self.playerState = None
		self.screen = screen
		self.healthQuery = None
		
	def setHealthQuery(self, query):
		self.healthQuery = query

	def setScore(self, score):
		self.score = score

	def updateScreen(self, entitiesToDraw):
		self.backdropManager.draw()
		self.drawScore()
		for entity in entitiesToDraw:
			self.drawImage(entity[0], entity[1])
		self.drawHealth()

	def updatePlayerData(self, playerState):
		self.playerState = playerState
		self.movePlayer()

	def movePlayer(self):
		self.playerX += GamePlayingDisplay.playerSpeedX
		self.checkPlayerRollover()

	def checkPlayerRollover(self):
		if self.playerX >= GamePlayingDisplay.backdropSize[0]:
			self.playerX -= GamePlayingDisplay.backdropSize[0]
			self.backdropManager.endOfBackdropReached()

	def drawBackdrops(self, backdrops):
		self.drawImage(backdrops[0], self.getCoordinatesForCurrentBackdrop())
		if self.isBackDropBoundaryVisible():
			self.drawImage(backdrops[1], self.getCoordinatesForNextBackdrop())

	def drawImage(self, image, coordinates):
		self.screen.blit(image, coordinates)

	def isBackDropBoundaryVisible(self):
		return self.playerX >= GamePlayingDisplay.backdropSize[0] - GuiConfig.screenSize[0]

	def getCoordinatesForCurrentBackdrop(self):
		return (-1 * self.playerX, 0)

	def getCoordinatesForNextBackdrop(self):
		return (GamePlayingDisplay.backdropSize[0] - self.playerX, 0)

	def drawScore(self):
		self.drawScoreBorder()
		self.drawScoreCounter()

	def drawScoreBorder(self):
		self.drawImage(GamePlayingDisplay.scoreBorderImage, (0, 0))

	def drawScoreCounter(self):
		self.drawImage(self.getScoreNumberImage(), GamePlayingDisplay.scoreDrawCoords)

	def getScoreNumberImage(self):
		scoreString = self.getScoreAsFormattedString()
		return GamePlayingDisplay.scoreFont.render(scoreString, True, GamePlayingDisplay.scoreFontColor)

	def getScoreAsFormattedString(self):
		return '{0:08d}'.format(self.score)

	def drawHealth(self):
		if self.healthQuery != None:
			if self.healthQuery() > 0:
				health = self.healthQuery()
				index = floor(health/20)
				index = 4 if index==5 else index
				color = GuiConfig.healthDrawColors[index]
				healthRect = (
					GuiConfig.healthMaxX-(health*2), 
					GuiConfig.healthMinY, 
					health*2, 
					GuiConfig.healthMaxY-GuiConfig.healthMinY)
				self.screen.fill(color, healthRect)
		