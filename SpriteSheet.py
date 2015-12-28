import pygame

class SpriteSheet(object):
	TRANS_BLACK_RGBA = (0, 0, 0, 0)

	def __init__(self, fileData, sheetDimensions):
		self.fileData = fileData
		self.sheetDimensions = sheetDimensions
		try:
			self.loadImageRects()
		except pygame.error as message:
			print('Unable to load SpriteSheet image:', fileData.filename)
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
		height = self.sheetDimensions.height / self.sheetDimensions.rows
		x = 0
		y = index * height + self.fileData.yOffsetInImage
		return (x, y, width, height)

	def loadImageRect(self, r):
		rect = pygame.Rect(r)
		image = pygame.Surface(rect.size).convert_alpha()
		image.fill(SpriteSheet.TRANS_BLACK_RGBA)
		image.blit(self.sheet, (0, 0), rect)
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
		
class BetterSpriteSheet(object):
	def __init__(self, filename, frameDimensions, frameCount, origin):
		self.filename = filename
		self.frameDimensions = frameDimensions
		self.frameCount = frameCount
		self.origin = origin
		try:
			self.loadFrames()
		except pygame.error as message:
			print('Unable to load BetterSpriteSheet image:', fileData.filename)
			quit()
		
	def loadFrames(self):
		self.rawFileImage = pygame.image.load(self.fileData.filename).convert_alpha()
		self.frames = [loadImageRect(r) for r in self.calculateImageRects()]

	def calculateImageRects(self):
		rects = []
		for y in map(lambda i: i*frameDimensions[1] + origin[1], range(frameCount)):
			(x, y, width, height) = (self.origin[0], y, frameDimensions[0], frameDimensions[1])
			rects.append((x, y, width, height))
		return rects
			
	def loadImageRect(self, r):
		rect = pygame.Rect(r)
		image = pygame.Surface(rect.size).convert_alpha()
		image.fill(SpriteSheet.TRANS_BLACK_RGBA)
		image.blit(self.sheet, (0, 0), rect)
		return image

def generateSpriteSheetGrid(filename, dimensions, columns, rows, imagesPerSheet):
	output = []
	spriteSheetDimensions = (dimensions[0]/columns, dimensions[1]/rows)
	frameDimensions = (spriteSheetDimensions[0], spriteSheetDimensions[1]/imagesPerSheet)
	for x in map(lambda i : i*spriteSheetDimensions[0], range(columns)):
		thisColumn = []
		for y in map(lambda i : i*spriteSheetDimensions[1], range(rows)):
			thisColumn.append(BetterSpriteSheet(filename, frameDimensions, imagesPerSheet, (x, y)))
		output.append(thisColumn)
	return output

