from pygame import image
from GUI import images

class BackdropManager(object):

    def __init__(self, drawFunction):
        self.drawFunction = drawFunction
        self.backdropsToDraw = [images.backdrops[0], images.backdrops[1]]

    def draw(self):
        self.drawFunction(self.backdropsToDraw)

    def endOfBackdropReached(self):
        self.backdropsToDraw = [self.backdropsToDraw[1], self.backdropsToDraw[0]]

    @classmethod
    def getBackDropSize(cls):
        return images.backdrops[0].get_size()


