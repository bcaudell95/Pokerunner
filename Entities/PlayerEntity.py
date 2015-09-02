from Entities.Entity import Entity
from Elements import Elements, getElementSheetFile
from FormSheet import FormSheet
from GUI.Animation import Animation
import math
from enum import Enum


class MovementStates(Enum):
    RUNNING = 0
    JUMPING = 1


class PlayerEntity(Entity):
    FRAMES_PER_IMAGE = 3
    TOTAL_FRAMES_PER_SHEET = 24
    MAX_JUMP_HEIGHT_PX = 200

    # Coefficient used to calculate jump motion
    PARABOLA_COEFF = -4 * MAX_JUMP_HEIGHT_PX / math.pow(TOTAL_FRAMES_PER_SHEET, 2)

    def __init__(self):
        self.currentMovementState = MovementStates.RUNNING
        self.currentElement = Elements.NORMAL
        self.sheets = [createSheetForElement(e) for e in Elements]
        self.currentAnimation = Animation(self.sheets[0].sheets[0], PlayerEntity.FRAMES_PER_IMAGE)

    def tick(self):
        if self.currentAnimation != None:
            self.currentAnimation.tick()

    def getImage(self):
        return self.currentAnimation.getCurrentImage()

    def getCurrentFormSheet(self):
        return self.sheets[self.currentElement.value]

    def getCurrentSpriteSheet(self):
        return self.getCurrentFormSheet().sheets[self.currentMovementState._value_]

    def checkForEndOfJump(self):
        if MovementStates.JUMPING == self.currentMovementState:
            self.currentMovementState = MovementStates.RUNNING

    def getCurrentPlayerState(self):
        return PlayerState(self.getImage(), self.calculateHeight())

    def changeMovementState(self, state):
        if self.currentMovementState is not state:
            self.currentMovementState = state
            self.loadAnimationForState(state)


    def calculateHeight(self):
        return (self.calculateHeightOfJump() if self.isPlayerJumping() else 0)

    def isPlayerJumping(self):
        return MovementStates.JUMPING == self.currentMovementState

    def calculateHeightOfJump(self):
        ### Parabolic Motion
        frameCount = self.currentAnimation.getAdjustedFrameCount()
        height = PlayerEntity.PARABOLA_COEFF * (frameCount) * ( frameCount - PlayerEntity.TOTAL_FRAMES_PER_SHEET)
        return math.floor(height)

    def endOfJump(self):
        self.changeMovementState(MovementStates.RUNNING)

    def loadAnimationForState(self, state):
        self.currentAnimation = Animation(self.getCurrentSpriteSheet(), PlayerEntity.FRAMES_PER_IMAGE)
        if self.isPlayerJumping():
            self.currentAnimation.onConclusion(self.endOfJump)


def createSheetForElement(element):
    return FormSheet(getElementSheetFile(element.name))


class PlayerState:
    def __init__(self, image, height):
        self.image = image
        self.height = height
