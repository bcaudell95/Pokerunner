import pygame
from GUI import Button
from GUI import GuiConfig
from GameStates import GameStates

class MainMenuDisplay(object):
	BACKGROUND_IMAGE_FILE = 'assets/images/MainMenu.png'
	
	START_BUTTON_IMAGES = ['assets/images/Start_on.png', 'assets/images/Start_off.png']
	START_BUTTON_RECT = (412, 400, 200,100)
	START_BUTTON_DRAW_COORDS = (START_BUTTON_RECT[0], START_BUTTON_RECT[1])
	
	def __init__(self, screen):
		self.screen = screen
		self.startButton = Button.Button.makeFromImagesList(MainMenuDisplay.START_BUTTON_IMAGES)
		self.mousePos = (0,0)
	
	def updateScreen(self):
		self.drawBackground()
		self.drawStartButton()
		
	def drawBackground(self):
		self.drawImage(pygame.image.load(MainMenuDisplay.BACKGROUND_IMAGE_FILE), (0,0))
		
	def drawStartButton(self):
		self.drawImage(self.startButton.getImage(), MainMenuDisplay.START_BUTTON_DRAW_COORDS)
		
	def drawImage(self, image, coordinates):
		self.screen.blit(image, coordinates)
		
	def setMouseCoords(self, coords):
		self.mousePos = coords
		self.updateButtonStates()
		
	def updateButtonStates(self):
		self.startButton.setState(isPointInRect(self.mousePos, MainMenuDisplay.START_BUTTON_RECT))
		
	def clicked(self, clickStates):
		if isLeftClick(clickStates):
			if self.startButton.rolloverOn:
				self.transitionToGame()
			
	def transitionToGame(self):
		raise GameStates.StateTransition(GameStates.GameState.PLAYING)
	
def isPointInRect(point, rect):
	inX = (point[0] >= rect[0]) and (point[0] <= (rect[0] + rect[2]))
	inY = (point[1] >= rect[1]) and (point[1] <= (rect[1] + rect[3]))
	return inX and inY
	
def isLeftClick(clickStates):
	return clickStates[0]