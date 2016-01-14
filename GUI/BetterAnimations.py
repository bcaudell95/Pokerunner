import pygame
from pygame.transform import scale
from GUI import GuiConfig

# Class for a single animation
class BasicAnimation:
	TRANS_BLACK_RGBA = (0, 0, 0, 0)

	def __init__(self, filename, frameSize, offset, frameCount, scaleFactor):
		self.rawImage = pygame.image.load(filename).convert_alpha()
		self.inputFrameSize = frameSize
		self.outputFrameSize = frameSize if scaleFactor == 1 else list(map(lambda x : int(scaleFactor*x), frameSize))
		self.offset = offset
		self.frameCount = frameCount
		self.ticksPerFrame = 3	# Default
		self.callback = None # Default
		self.isScaled = not scaleFactor == 1
		
		self.tickCount = 0
		self.currentFrame = 0
		try:
			self.loadFrames()
		except pygame.error as message:
			print('Unable to create BasicAnimation: ', filename, ' - ', offset)
			quit()
			
	def loadFrames(self):
		self.frames = [self.loadFrameFromRect(r) for r in self.calculateImageRects()]
	
	def calculateImageRects(self):
		return [self.imageRectByIndex(i) for i in range(self.frameCount)]
		
	def imageRectByIndex(self, i):
		w, h = self.inputFrameSize
		x, y = self.offset
		y = y + (i * h)
		return (x, y, w, h)
		
	def loadFrameFromRect(self, r):
		rect = pygame.Rect(r)
		image = pygame.Surface(rect.size).convert_alpha()
		image.fill(BasicAnimation.TRANS_BLACK_RGBA)
		image.blit(self.rawImage, (0,0), rect)
		if self.isScaled:
			image = scale(image, self.outputFrameSize)
		return image
		
	def tick(self):
		if not callable(self.tickCount): # default behavior
			self.tickCount = self.tickCount + 1
			if self.tickCount >= self.ticksPerFrame:
				self.tickCount = 0
				self.currentFrame = self.currentFrame + 1
				if self.currentFrame >= self.frameCount:
					self.currentFrame = 0
					if callable(self.callback):
						self.callback()

	def getCurrentFrame(self):
		if not callable(self.currentFrame):
			return self.frames[self.currentFrame]
		else:
			return self.frames[self.currentFrame()]
			
	def reset(self):
		self.tickCount = 0
		self.currentFrame = 0
		
# Class for multiple animations in a single file
# This is used for multiple Eevee forms in one movement state image file
class AnimationCluster:
	def __init__(self, filename, frameSize, offset, frameCount, animationCount, scaleFactor):
		self.ticksPerFrame = 3 # default
		self.tickCount = 0
		tickQuery = lambda : self.tickCount
		
		self.frameCount = frameCount
		self.currentFrame = 0
		frameQuery = lambda : self.currentFrame
	
		self.currentAnimation = 0
		self.animationCount = animationCount
	
		self.callback = None
	
		self.animations = []
		for a in range(animationCount):
			x, y = offset
			x = x + (frameSize[0] * a)
			animation = BasicAnimation(filename, frameSize, (x,y), frameCount, scaleFactor)
			animation.tickCount = tickQuery
			animation.currentFrame = frameQuery
			self.animations.append(animation)
			
	def tick(self):
		self.tickCount = self.tickCount + 1
		if self.tickCount >= self.ticksPerFrame:
			self.tickCount = 0
			self.currentFrame = self.currentFrame + 1
			if self.currentFrame >= self.frameCount:
				self.currentFrame = 0
				if callable(self.callback):
					self.callback()
		
	def getCurrentFrame(self):
		return self.animations[self.currentAnimation].getCurrentFrame()
		
	def setCurrentAnimation(self, a):
		if a < self.animationCount:
			self.currentAnimation = a
			
	def setCallbacks(self, fn):
		for a in self.animations:
			a.callback = fn
			
	def reset(self):
		self.tickCount = 0
		self.currentFrame = 0

# Class for a player's entire animation suite
# Multiple AnimationCluster's, one for each movement state			
class PlayerAnimation:

	def __init__(self, filenames):
		self.clusters = []
		for file in filenames:
			self.clusters.append(AnimationCluster(file, GuiConfig.playerInputFrameSize, (0,0), GuiConfig.playerFramesPerAnimation, GuiConfig.playerForms, GuiConfig.playerFrameScale))

		self.currentCluster = self.clusters[0]
		self.clusterCount = len(self.clusters)
			
	def setCurrentCluster(self, c):
		if c < self.clusterCount:
			self.currentCluster = self.clusters[c]
			self.currentCluster.reset()
			
	def tick(self):
		self.currentCluster.tick()
			
	def getCurrentFrame(self):
		return self.currentCluster.getCurrentFrame()
		
	def setCurrentForm(self, formIndex):
		for c in self.clusters:
			c.setCurrentAnimation(formIndex)
			
	def getAdjustedFrameCount(self):
		c = self.currentCluster
		return (c.ticksPerFrame * c.currentFrame) + c.tickCount
		
	def setClusterCallback(self, cluster, fn):
		self.clusters[cluster].callback = fn