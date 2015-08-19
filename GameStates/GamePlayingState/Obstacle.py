import pygame
from GUI import images

class Obstacles:

	class Obstacle(object):
		
		def __init__(self, file):
			self.image = pygame.image.load(file)
			self.dimensions = self.image.get_size()
			
		def getImage(self):
			return self.image
			
	basicObstacle = Obstacle(images.basicObstacle)