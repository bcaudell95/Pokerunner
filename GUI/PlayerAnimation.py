from SpriteSheet import BetterSpriteSheet, generateSpriteSheetGrid
from Elements import Elements
from Entities.PlayerEntity import MovementStates

class PlayerAnimation(object):
	FORMS_COUNT = 2
	MOVEMENT_STATES_COUNT = 2
	FRAME_COUNT = 8
	FRAME_SIZE = (256, 128)
	IMAGE_SIZE = (FRAME_SIZE[0]*FORMS_COUNT, FRAME_SIZE[1]*FRAME_COUNT*MOVEMENT_STATES_COUNT)

	def __init__(self, filename):
		self.grid = generateSpriteSheetGrid(filename, IMAGE_SIZE, FORMS_COUNT, MOVEMENT_STATES_COUNT, FRAME_COUNT)
		self.currentForm = Elements.NORMAL
		self.currentState = MovementStates.RUNNING
		self.currentImage = 0
		
	def getImage(self):
		return self.grid[self.currentForm][self.currentState].frames[self.currentImage]