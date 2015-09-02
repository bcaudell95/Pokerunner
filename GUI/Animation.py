from SpriteSheet import SpriteSheet, SpriteSheetDimensions, SpriteSheetFile

class Animation(object):
    def __init__(self, sheet, framesPerImage=1):
        self.framesPerImage = framesPerImage
        self.numberOfImages = len(sheet.images)
        self.sheet = sheet
        self.actionOnConclusion = None

        self.currentFrame = 0
        self.currentImage = 0

    def onConclusion(self, fn):
        self.actionOnConclusion = fn

    def tick(self):
        self.currentFrame += 1
        self.checkForFrameRollover()

    def checkForFrameRollover(self):
        if self.currentFrame == self.framesPerImage:
            self.currentFrame = 0
            self.currentImage += 1
            self.checkForImageRollover()

    def checkForImageRollover(self):
        if self.currentImage == self.numberOfImages:
            self.currentImage = 0
            self.reachedEndOfAnimation()

    def reachedEndOfAnimation(self):
        if callable(self.actionOnConclusion):
            self.actionOnConclusion()

    def getCurrentImage(self):
        return self.sheet.images[self.currentImage]

    def getAdjustedFrameCount(self):
        return self.currentImage*self.framesPerImage + self.currentFrame
