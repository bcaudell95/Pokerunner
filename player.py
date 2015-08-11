import pygame
import formSheet
import elements
from enum import Enum
import math

class States(Enum):
    RUNNING = 0
    JUMPING = 1

class Player:

    FRAMES_PER_IMAGE = 3
    IMAGES_PER_SHEET = 8

    JUMP_HEIGHT_PIXELS = 200

    def __init__(self):
        self.currentFrame = 0
        self.currentImage = 0
        self.currentState = States.RUNNING
        self.currentElement = elements.Elements.NORMAL

        self.sheets = []
        for element in elements.Elements:
            self.sheets.append(formSheet.FormSheet(elements.getElementSheetFile(element.name)))

    def getCurrentImage(self):
        return self.sheets[self.currentElement.value].getStateSheet(self.currentState.value).getImage(self.currentImage)

    def stepFrame(self):
        self.currentFrame += 1
        if Player.FRAMES_PER_IMAGE == self.currentFrame:
            self.currentFrame = 0
            self.currentImage += 1
            if Player.IMAGES_PER_SHEET == self.currentImage:
                self.currentImage = 0
                if States.JUMPING == self.currentState:
                    self.currentState = States.RUNNING

        if States.JUMPING == self.currentState:
            return [self.getCurrentImage(), self.calculateHeight()]
        else:
            return [self.getCurrentImage(), 0]

    def changeState(self, state):
        if self.currentState is not state:
            self.currentState = state
            self.currentFrame = 0
            self.currentImage = 0

    def calculateHeight(self):
        ### Parabolic Motion
        frameCount = (Player.FRAMES_PER_IMAGE*self.currentImage)+self.currentFrame
        midpoint = Player.FRAMES_PER_IMAGE*Player.IMAGES_PER_SHEET/2
        maxHeight = Player.JUMP_HEIGHT_PIXELS/(midpoint*midpoint)
        coeff = -1*maxHeight
        height = coeff*(frameCount)*(frameCount-Player.FRAMES_PER_IMAGE*Player.IMAGES_PER_SHEET)
        height = math.floor(height)
        return height
