from Entities.Entity import Entity
from Entities.GeostationaryEntity import GeostationaryEntity
from MainConfig import Elements
from GUI.BetterAnimations import PlayerAnimation
import math
from enum import Enum

class MovementStates(Enum):
	RUNNING = 0
	JUMPING = 1

class PlayerEntity(Entity):
	FRAMES_PER_IMAGE = 3
	TOTAL_FRAMES_PER_SHEET = 24
	MAX_JUMP_HEIGHT_PX = 200
	STARTING_HEALTH = 12

	# Coefficient used to calculate jump motion
	PARABOLA_COEFF = -4 * MAX_JUMP_HEIGHT_PX / math.pow(TOTAL_FRAMES_PER_SHEET, 2)

	def __init__(self, coords):
		self.currentMovementState = MovementStates.RUNNING
		self.currentElement = Elements.FIRE
		self.animation = PlayerAnimation(['assets/images/running.png', 'assets/images/jumping.png'])
		self.animation.setClusterCallback(1, self.endOfJump)
		self.baseCoords = coords
		self.health = PlayerEntity.STARTING_HEALTH

	def tick(self):
		if self.animation != None:
			self.animation.tick()

	def getImage(self):
		return self.animation.getCurrentFrame()

	def getCoords(self):
		return [self.baseCoords[0], self.baseCoords[1] - self.calculateHeight()]
		
	def getHealth(self):
		return self.health

	def checkForEndOfJump(self):
		if MovementStates.JUMPING == self.currentMovementState:
			self.currentMovementState = MovementStates.RUNNING

	def getCurrentPlayerState(self):
		return PlayerState(self.getImage(), self.calculateHeight())

	def changeMovementState(self, state):
		if self.currentMovementState is not state:
			self.currentMovementState = state
			self.animation.setCurrentCluster(state.value)

	def calculateHeight(self):
		return (self.calculateHeightOfJump() if self.isPlayerJumping() else 0)

	def isPlayerJumping(self):
		return MovementStates.JUMPING == self.currentMovementState

	def calculateHeightOfJump(self):
		### Parabolic Motion
		frameCount = self.animation.getAdjustedFrameCount()
		height = PlayerEntity.PARABOLA_COEFF * (frameCount) * ( frameCount - PlayerEntity.TOTAL_FRAMES_PER_SHEET)
		return math.floor(height)

	def endOfJump(self):
		self.changeMovementState(MovementStates.RUNNING)
		self.animation.setCurrentCluster(0)
			
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
		self.animation.setCurrentForm(element.value)

class PlayerState:
	def __init__(self, image, height):
		self.image = image
		self.height = height
		
class PlayerHealthEmptyException(Exception):
	def __init__(self):
		pass
