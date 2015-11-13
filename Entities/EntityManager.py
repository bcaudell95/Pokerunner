from Entities.PlayerEntity import PlayerEntity
from Entities.GeostationaryEntity import GeostationaryEntity, ObjectOffScreenException
from GUI import images

class EntityManager(object):
	GEOSTATIONARY_START_COORDS = (0,0)
	GEOSTATIONARY_SPEED = 0

	def __init__(self):
		self.entities = []
		self.activeCollisionPairs = []
		self.playerEntity = None

	def updateAll(self):
		for entity in self.entities:
			self.tickEntity(entity)

	def getAllEntitiesToDraw(self):
		drawEntities = []
		for entity in self.entities:
			drawEntities.append([entity.getImage(), entity.getCoords()])
		return drawEntities

	def addPlayerEntity(self, coords):
		if self.playerEntity == None:
			self.playerEntity = PlayerEntity(coords)
			self.entities.append(self.playerEntity)
		else:
			raise PlayerAlreadyInstantiatedException()

	def getPlayerEntity(self):
		if self.playerEntity != None:
			return self.playerEntity
		else:
			raise PlayerNotInstantiatedException()

	def spawnBasicObstacle(self):
		self.spawnBasicObstacleWithArgs(EntityManager.GEOSTATIONARY_START_COORDS, EntityManager.GEOSTATIONARY_SPEED, True, True)

	def spawnBasicObstacleWithArgs(self, startCoords, speed, adjustForWidth = True, adjustForHeight = True):
		if adjustForWidth:
			startCoords = (startCoords[0] - images.basicObstacle.get_size()[0], startCoords[1])
		if adjustForHeight:
			startCoords = (startCoords[0], startCoords[1] - images.basicObstacle.get_size()[1])
		self.entities.append(GeostationaryEntity(images.basicObstacle,startCoords, speed))

	def tickEntity(self, entity):
		try:
			entity.tick()
		except ObjectOffScreenException as e:
			self.entities.remove(entity)
			self.spawnBasicObstacle()

	def checkForCollisions(self):
		for (entity1, entity2) in self.getAllEntityPairs():
			currentCollisionStatus = self.isPairInActiveCollisionList(entity1, entity2)
			if areColliding(entity1, entity2):
				if not currentCollisionStatus:
					print("Entering Collision...")
					self.activeCollisionPairs.append((entity1, entity2))
			else:
				if currentCollisionStatus:
					self.removePairFromActiveCollisionList(entity1, entity2)

	def getAllEntityPairs(self):
		pairs = []
		for (index, entity1) in enumerate(self.entities):
			for entity2 in self.entities[index+1:]:
				pairs.append((entity1, entity2))
		return pairs
		
	def isPairInActiveCollisionList(self, entity1, entity2):
		return (entity1, entity2) in self.activeCollisionPairs or (entity2, entity1) in self.activeCollisionPairs
		
	def removePairFromActiveCollisionList(self, entity1, entity2):
		if (entity1, entity2) in self.activeCollisionPairs:
			print("Exiting collision")
			self.activeCollisionPairs.remove((entity1, entity2))
		if (entity2, entity1) in self.activeCollisionPairs:
			print("Exiting collision")
			self.activeCollisionPairs.remove((entity2, entity1))
						
def areColliding(entity1, entity2):
	(left1, top1, right1, bottom1) = entity1.getBoundingBox()
	(left2, top2, right2, bottom2) = entity2.getBoundingBox()
	
	return not (left2 > right1 or right2 < left1 or top2 > bottom1 or bottom2 < top1)
	
class PlayerNotInstantiatedException(Exception):
	def __init__(self):
		super().__init__()


class PlayerAlreadyInstantiatedException(Exception):
	def __init__(self):
		super().__init__()
