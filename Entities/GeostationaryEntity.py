from Entities.Entity import Entity

class GeostationaryEntity(Entity):
    def __init__(self, image, coords, speed):
        self.image = image
        self.coords = coords
        self.speed = speed

    def getImage(self):
        return self.image

    def tick(self):
        self.move()

    def getCoords(self):
        return self.coords

    def move(self):
        self.coords = [self.coords[0] - self.speed, self.coords[1]]
        if self.coords[0] + self.image.get_size()[0] < 0:
            raise ObjectOffScreenException()

class ObjectOffScreenException(Exception):
    def __init__(self):
        super().__init__()