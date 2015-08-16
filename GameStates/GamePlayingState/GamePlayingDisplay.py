import pygame
from GUI import GuiConfig

class GamePlayingDisplay:
	backdropSize = (3072,768)

	backdropFiles = ['assets/images/backdrop.png', 'assets/images/backdrop1.png']
	backdrops = [pygame.image.load(file) for file in backdropFiles]
	
	playerDrawCoordinates = (100, 512)
	playerSpeedX = 10

	def __init__(self, screen):
		self.currentBackdropIndex = 0
		self.playerX = 0
		self.screen = screen

	def updateScreen(self):
		self.drawBackdrop()
		self.drawPlayer()

	def updatePlayerData(self, playerState):
		self.playerState = playerState
		self.movePlayer()
			
	def movePlayer(self):
		self.playerX += GamePlayingDisplay.playerSpeedX
		self.checkPlayerRollover()

	def checkPlayerRollover(self):
		if self.playerX >= GamePlayingDisplay.backdropSize[0]:
			self.playerX -= GamePlayingDisplay.backdropSize[0]
			self.endOfBackdropReached()
			
	def drawBackdrop(self):
		self.drawImage(self.getCurrentBackdrop(), self.getCoordinatesForCurrentBackdrop())
		if self.isBackDropBoundaryVisible():
			self.drawImage(self.getNextBackdrop(), self.getCoordinatesForNextBackdrop())
		
	def drawImage(self, image, coordinates):
		self.screen.blit(image, coordinates)
		
	def getCurrentBackdrop(self):
		return GamePlayingDisplay.backdrops[self.currentBackdropIndex]
		
	def getCoordinatesForCurrentBackdrop(self):
		return (-1 * self.playerX,0)
		
	def isBackDropBoundaryVisible(self):
		return self.playerX >= GamePlayingDisplay.backdropSize[0] - GuiConfig.screenSize[0]
	
	def getCoordinatesForNextBackdrop(self):
		return (GamePlayingDisplay.backdropSize[0] - self.playerX, 0)
	
	def getNextBackdrop(self):
		if self.currentBackdropIndex + 1 < len(GamePlayingDisplay.backdrops):
			return GamePlayingDisplay.backdrops[self.currentBackdropIndex + 1]
		else:
			return GamePlayingDisplay.backdrops[0]
		
	def endOfBackdropReached(self):
		self.currentBackdropIndex += 1
		if self.currentBackdropIndex == len(GamePlayingDisplay.backdrops):
			self.currentBackdropIndex = 0
			
	def drawPlayer(self):
		self.drawImage(self.playerState.image, self.calculatePlayerDrawCoordinates())
	
	def calculatePlayerDrawCoordinates(self):
		x = GamePlayingDisplay.playerDrawCoordinates[0]
		y = GamePlayingDisplay.playerDrawCoordinates[1] - self.playerState.height
		return (x,y)