from Entities.Entity import Entity
from Entities.GeostationaryEntity import GeostationaryEntity
from Elements import Elements, getElementSheetFile
from FormSheet import FormSheet
from GUI.Animation import Animation
import math
from enum import Enum


class MovementStates(Enum):
	RUNNING = 0
	JUMPING = 1

class PlayerEntity(Entity):
	FRAMES_PER_IMAGE = 3
	TOTAL_FRAMES_PER_SHEET = 24
	MAX_JUMP_HEIGHT_PX = 200
	STARTING_HEALTH = 3

	# Coefficient used to calculate jump motion
	PARABOLA_COEFF = -4 * MAX_JUMP_HEIGHT_PX / math.pow(TOTAL_FRAMES_PER_SHEET, 2)

	def __init__(self, coords):
		self.currentMovementState = MovementStates.RUNNING
		self.currentElement = Elements.FIRE
		self.sheets = { e : createSheetForElement(e) for e in Elements}
		self.currentAnimation = Animation(self.sheets[self.currentElement].sheets[0], PlayerEntity.FRAMES_PER_IMAGE)
		self.baseCoords = coords
		self.health = PlayerEntity.STARTING_HEALTH

	def tick(self):
		if self.currentAnimation != None:
			self.currentAnimation.tick()

	def getImage(self):
		return self.currentAnimation.getCurrentImage()

	def getCoords(self):
		return [self.baseCoords[0], self.baseCoords[1] - self.calculateHeight()]
		
	def getHealth(self):
		return self.health

	def getCurrentFormSheet(self):
		return self.sheets[self.currentElement]

	def getCurrentSpriteSheet(self):
		return self.getCurrentFormSheet().sheets[self.currentMovementState._value_]

	def checkForEndOfJump(self):
		if MovementStates.JUMPING == self.currentMovementState:
			self.currentMovementState = MovementStates.RUNNING

	def getCurrentPlayerState(self):
		return PlayerState(self.getImage(), self.calculateHeight())

	def changeMovementState(self, state):
		if self.currentMovementState is not state:
			self.currentMovementState = state
			self.loadAnimationForState(state)


	def calculateHeight(self):
		return (self.calculateHeightOfJump() if self.isPlayerJumping() else 0)

	def isPlayerJumping(self):
		return MovementStates.JUMPING == self.currentMovementState

	def calculateHeightOfJump(self):
		### Parabolic Motion
		frameCount = self.currentAnimation.getAdjustedFrameCount()
		height = PlayerEntity.PARABOLA_COEFF * (frameCount) * ( frameCount - PlayerEntity.TOTAL_FRAMES_PER_SHEET)
		return math.floor(height)

	def endOfJump(self):
		self.changeMovementState(MovementStates.RUNNING)

	def loadAnimationForState(self, state):
		self.currentAnimation = Animation(self.getCurrentSpriteSheet(), PlayerEntity.FRAMES_PER_IMAGE)
		if self.isPlayerJumping():
			self.currentAnimation.onConclusion(self.endOfJump)
			
	def getBoundingBox(self):
		x1 = self.baseCoords[0]
		y1 = self.baseCoords[1]
		x2 = x1 + self.getImage().get_size()[0]
		y2 = y1 + self.getImage().get_size()[1]
		return (x1, y1, x2, y2)
		
	def handleCollisionWith(self, otherEntity):
		if isinstance(otherEntity, GeostationaryEntity):
			print("Hit obstacle!")
			self.health -= 1
			self.checkForHealthEmpty()

	def checkForHealthEmpty(self):
		if self.health <= 0:
			raise PlayerHealthEmptyException()
			
	def setElement(self, element):
		self.currentElement = element
		self.currentAnimation = Animation(self.sheets[self.currentElement].sheets[0], PlayerEntity.FRAMES_PER_IMAGE)
	
def createSheetForElement(element):
	return FormSheet(getElementSheetFile(element.name))


class PlayerState:
	def __init__(self, image, height):
		self.image = image
		self.height = height
		
class PlayerHealthEmptyException(Exception):
	def __init__(self):
		pass
