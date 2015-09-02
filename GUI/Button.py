import pygame


class Button(object):
    def makeFromImagesList(imagesList):
        return Button(imagesList[0], imagesList[1])

    def __init__(self, onImage, offImage):
        self.onImage = pygame.image.load(onImage)
        self.offImage = pygame.image.load(offImage)
        self.rolloverOn = False

    def setState(self, state):
        if state != self.rolloverOn:
            self.rolloverOn = state

    def getImage(self):
        return (self.onImage if self.rolloverOn else self.offImage)
