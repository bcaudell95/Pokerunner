import pygame
import FormSheet
import Elements
from enum import Enum
import math

class MovementStates(Enum):
	RUNNING = 0
	JUMPING = 1

class Player:

	FRAMES_PER_IMAGE = 3
	IMAGES_PER_SHEET = 8
	TOTAL_FRAMES_PER_SHEET = FRAMES_PER_IMAGE*IMAGES_PER_SHEET
	MAX_JUMP_HEIGHT_PX = 200
	
	#Coefficient used to calculate jump motion
	PARABOLA_COEFF = -4*MAX_JUMP_HEIGHT_PX/math.pow(TOTAL_FRAMES_PER_SHEET,2)

	def __init__(self):
		self.currentFrame = 0
		self.currentImage = 0
		self.currentMovementState = MovementStates.RUNNING
		self.currentElement = Elements.Elements.NORMAL

		self.sheets = [createSheetForElement(e) for e in Elements.Elements]
			
	def getCurrentImage(self):
		sheet = self.getCurrentSheet()
		state = sheet.getStateSheet(self.currentMovementState.value)
		image = state.getImage(self.currentImage)
		return image
		
	def getCurrentSheet(self):
		return self.sheets[self.currentElement.value]
		
	def stepFrame(self):
		self.currentFrame += 1
		self.checkForFrameRollover()

	def checkForFrameRollover(self):
		if Player.FRAMES_PER_IMAGE == self.currentFrame:
			self.currentFrame = 0
			self.currentImage += 1
			self.checkForImageRollover()
					
	def checkForImageRollover(self):
		if Player.IMAGES_PER_SHEET == self.currentImage:
			self.currentImage = 0
			self.checkForEndOfJump()
					
	def checkForEndOfJump(self):
		if MovementStates.JUMPING == self.currentMovementState:
			self.currentMovementState = MovementStates.RUNNING
			
	def getCurrentPlayerState(self):
		return PlayerState(self.getCurrentImage(), self.calculateHeight())
			
	def changeMovementState(self, state):
		if self.currentMovementState is not state:
			self.currentMovementState = state
			self.currentFrame = self.currentImage = 0

	def calculateHeight(self):
		return (self.calculateHeightOfJump() if self.isPlayerJumping() else 0)

	def isPlayerJumping(self):
		return MovementStates.JUMPING == self.currentMovementState
		
	def calculateHeightOfJump(self):
		### Parabolic Motion
		frameCount = self.getAdjustedFrameCount()
		height = Player.PARABOLA_COEFF*(frameCount)*(frameCount-Player.TOTAL_FRAMES_PER_SHEET)
		return math.floor(height)
	
	def getAdjustedFrameCount(self):
		return (Player.FRAMES_PER_IMAGE*self.currentImage)+self.currentFrame
		
def createSheetForElement(element):
	return FormSheet.FormSheet(Elements.getElementSheetFile(element.name))
		
class PlayerState:
	def __init__(self, image, height):
		self.image = image
		self.height = height
		