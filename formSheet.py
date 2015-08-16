import spriteSheet

class FormSheet(object):

	FRAME_DIMENSIONS = (256, 128)   # Dimensions for one image
	ROWS = 8                        # Number of images per sprite sheet
	SHEET_DIMENSIONS = (FRAME_DIMENSIONS[0], FRAME_DIMENSIONS[1]*ROWS)  #Dimensions for a sprite sheet
	STATES_COUNT = 2                # Number of sheets per image
	
	def __init__(self, filename):
		self.filename = filename
		self.sheets = []
		for i in range(FormSheet.STATES_COUNT):
			self.loadSheetByIndex(i)
	
	def loadSheetByIndex(self, index):
		fileData = spriteSheet.SpriteSheetFile(self.filename, index*FormSheet.SHEET_DIMENSIONS[1])
		dimensions = spriteSheet.SpriteSheetDimensions(FormSheet.SHEET_DIMENSIONS, FormSheet.ROWS)
		self.sheets.append(spriteSheet.spritesheet(fileData, dimensions))
	
	def getStateSheet(self, i):
		return self.sheets[i]
