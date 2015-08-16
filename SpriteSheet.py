import pygame

class spritesheet(object):
	def __init__(self, fileData, sheetDimensions ):
		self.fileData = fileData
		self.sheetDimensions = sheetDimensions
		try:
			self.loadImageRects()
		except pygame.error as message:
			print('Unable to load spritesheet image:', fileData.filename)
			quit()
			
	def loadImageRects(self):
		self.sheet = pygame.image.load(self.fileData.filename).convert_alpha()
		self.images = []
		for r in self.calculateImageRects():
			self.images.append(self.loadImageRect(r))
			
	def calculateImageRects(self):
		rects = [self.imageRectByIndex(i) for i in range(self.sheetDimensions.rows)]
		return rects
		
	def imageRectByIndex(self, index):
		width = self.sheetDimensions.width
		height = self.sheetDimensions.height/self.sheetDimensions.rows
		return (0, index*height + self.fileData.yOffsetInImage, width, height)
		
	def loadImageRect(self, r):
		rect = pygame.Rect(r)
		image = pygame.Surface(rect.size).convert_alpha()
		image.fill((0,0,0,0))
		image.blit(self.sheet, (0,0), rect)
		return image
	
	def getImage(self, i):
		return self.images[i]

class SpriteSheetFile(object):
	def __init__(self, filename, yOffsetInImage):
		self.filename = filename
		self.yOffsetInImage = yOffsetInImage

class SpriteSheetDimensions(object):
	def __init__(self, widthAndHeight, rows):
		self.width = widthAndHeight[0]
		self.height = widthAndHeight[1]
		self.rows = rows
