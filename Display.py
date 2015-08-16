import pygame

class Display:

	screenSize = (1024,768)
	backdropSize = (3072,768)

	backdropFiles = ['assets/images/backdrop.png', 'assets/images/backdrop1.png']
	backdrops = [pygame.image.load(file) for file in backdropFiles]
	
	playerDrawCoordinates = (100, 512)
	playerSpeedX = 10

	def __init__(self):
		self.screen = pygame.display.set_mode(Display.screenSize)
		self.currentBackdropIndex = 0
		self.playerX = 0

	def updateScreen(self):
		self.drawBackdrop()
		self.drawPlayer()
		pygame.display.update()

	def updatePlayerData(self, playerState):
		self.playerState = playerState
		self.movePlayer()
			
	def movePlayer(self):
		self.playerX += Display.playerSpeedX
		if self.playerX >= Display.backdropSize[0]:
			self.playerX -= Display.backdropSize[0]
			self.endOfBackdropReached()

	def drawBackdrop(self):
		self.drawImage(self.getCurrentBackdrop(), self.getCoordinatesForCurrentBackdrop())
		if self.isBackDropBoundaryVisible():
			self.drawImage(self.getNextBackdrop(), self.getCoordinatesForNextBackdrop())
		
	def drawImage(self, image, coordinates):
		self.screen.blit(image, coordinates)
		
	def getCurrentBackdrop(self):
		return Display.backdrops[self.currentBackdropIndex]
		
	def getCoordinatesForCurrentBackdrop(self):
		return (-1 * self.playerX,0)
		
	def isBackDropBoundaryVisible(self):
		return self.playerX >= Display.backdropSize[0] - Display.screenSize[0]
	
	def getCoordinatesForNextBackdrop(self):
		return (Display.backdropSize[0] - self.playerX, 0)
	
	def getNextBackdrop(self):
		if self.currentBackdropIndex + 1 < len(Display.backdrops):
			return Display.backdrops[self.currentBackdropIndex + 1]
		else:
			return Display.backdrops[0]
		
	def endOfBackdropReached(self):
		self.currentBackdropIndex += 1
		if self.currentBackdropIndex == len(Display.backdrops):
			self.currentBackdropIndex = 0
			
	def drawPlayer(self):
		self.drawImage(self.playerState.image, self.calculatePlayerDrawCoordinates())
	
	def calculatePlayerDrawCoordinates(self):
		x = Display.playerDrawCoordinates[0]
		y = Display.playerDrawCoordinates[1] - self.playerState.height
		return (x,y)