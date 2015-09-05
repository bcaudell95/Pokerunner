from pygame import image


class BackdropManager(object):
    backdropFiles = ['assets/images/backdrop.png', 'assets/images/backdrop1.png']
    backdrops = [image.load(file) for file in backdropFiles]

    def __init__(self, drawFunction):
        self.drawFunction = drawFunction
        self.backdropsToDraw = [BackdropManager.backdrops[0], BackdropManager.backdrops[1]]

    def draw(self):
        self.drawFunction(self.backdropsToDraw)

    def endOfBackdropReached(self):
        self.backdropsToDraw = [self.backdropsToDraw[1], self.backdropsToDraw[0]]

    @classmethod
    def getBackDropSize(cls):
        return BackdropManager.backdrops[0].get_size()


