import pygame
from GUI.Button import Button
from GUI import images
from GameStates.GameStates import GameState, StateTransition


class MainMenuDisplay(object):
    START_BUTTON_RECT = (412, 400, 200, 100)
    START_BUTTON_DRAW_COORDS = (START_BUTTON_RECT[0], START_BUTTON_RECT[1])

    def __init__(self, screen):
        self.screen = screen
        self.startButton = Button.makeFromImagesList(images.START_BUTTON_IMAGES_FILES)
        self.mousePos = (0, 0)

    def updateScreen(self):
        self.drawBackground()
        self.drawStartButton()

    def drawBackground(self):
        self.drawImage(images.mainMenuBackdropImage, (0, 0))

    def drawStartButton(self):
        self.drawImage(self.startButton.getImage(), MainMenuDisplay.START_BUTTON_DRAW_COORDS)

    def drawImage(self, image, coordinates):
        self.screen.blit(image, coordinates)

    def updateMouseAndButtons(self, coords):
        self.mousePos = coords
        self.updateButtonStates()

    def updateButtonStates(self):
        self.startButton.setState(isPointInRect(self.mousePos, MainMenuDisplay.START_BUTTON_RECT))

    def handleClick(self, clickStates):
        if isLeftClick(clickStates):
            self.handleLeftClick()

    def handleLeftClick(self):
        if self.startButton.rolloverOn:
            self.transitionToGame()

    def transitionToGame(self):
        raise StateTransition(GameState.PLAYING)


def isPointInRect(point, rect):
    inX = (point[0] >= rect[0]) and (point[0] <= (rect[0] + rect[2]))
    inY = (point[1] >= rect[1]) and (point[1] <= (rect[1] + rect[3]))
    return inX and inY


def isLeftClick(clickStates):
    return clickStates[0]
