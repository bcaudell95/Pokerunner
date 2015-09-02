import pygame
from GUI import GuiConfig
from GameStates.GamePlayingState.Obstacle import Obstacles

pygame.font.init()


class GamePlayingDisplay:
    backdropSize = (3072, 768)

    backdropFiles = ['assets/images/backdrop.png', 'assets/images/backdrop1.png']
    backdrops = [pygame.image.load(file) for file in backdropFiles]

    playerDrawCoordinates = (100, 512)
    playerSpeedX = 10

    scoreBorderImage = pygame.image.load('assets/images/ScoreBorder.png')
    scoreBorderDimensions = (256, 64)

    scoreFontFile = 'assets/fonts/AndaleMono.ttf'
    scoreFont = pygame.font.Font(scoreFontFile, 48)
    scoreFontColor = (0, 0, 0)
    scoreCountDrawCoords = (5, 10)

    def __init__(self, screen):
        self.currentBackdropIndex = 0
        self.playerX = 0
        self.score = 0
        self.screen = screen
        self.obstaclesList = []
        self.spawnNewObstacle(Obstacles.basicObstacle)

    def setScore(self, score):
        self.score = score

    def updateScreen(self):
        self.drawBackdrop()
        self.drawObstacles()
        self.moveObstacles()
        self.drawScore()
        self.drawPlayer()

    def updatePlayerData(self, playerState):
        self.playerState = playerState
        self.movePlayer()

    def movePlayer(self):
        self.playerX += GamePlayingDisplay.playerSpeedX
        self.checkPlayerRollover()

    def checkPlayerRollover(self):
        if self.playerX >= GamePlayingDisplay.backdropSize[0]:
            self.playerX -= GamePlayingDisplay.backdropSize[0]
            self.endOfBackdropReached()

    def drawBackdrop(self):
        self.drawImage(self.getCurrentBackdrop(), self.getCoordinatesForCurrentBackdrop())
        if self.isBackDropBoundaryVisible():
            self.drawImage(self.getNextBackdrop(), self.getCoordinatesForNextBackdrop())

    def drawImage(self, image, coordinates):
        self.screen.blit(image, coordinates)

    def getCurrentBackdrop(self):
        return GamePlayingDisplay.backdrops[self.currentBackdropIndex]

    def getCoordinatesForCurrentBackdrop(self):
        return (-1 * self.playerX, 0)

    def isBackDropBoundaryVisible(self):
        return self.playerX >= GamePlayingDisplay.backdropSize[0] - GuiConfig.screenSize[0]

    def getCoordinatesForNextBackdrop(self):
        return (GamePlayingDisplay.backdropSize[0] - self.playerX, 0)

    def getNextBackdrop(self):
        if self.currentBackdropIndex + 1 < len(GamePlayingDisplay.backdrops):
            return GamePlayingDisplay.backdrops[self.currentBackdropIndex + 1]
        else:
            return GamePlayingDisplay.backdrops[0]

    def endOfBackdropReached(self):
        self.currentBackdropIndex += 1
        if self.currentBackdropIndex == len(GamePlayingDisplay.backdrops):
            self.currentBackdropIndex = 0

    def drawObstacles(self):
        for ob in self.obstaclesList:
            image = ob[0].getImage()
            coords = ob[1]
            self.drawImage(image, coords)

    def moveObstacles(self):
        for ob in self.obstaclesList:
            oldCoords = ob[1]
            newCoords = (oldCoords[0] - GamePlayingDisplay.playerSpeedX, oldCoords[1])
            imageWidth = ob[0].getImage().get_size()[0]
            if (newCoords[0] + imageWidth > 0):
                ob[1] = newCoords
            else:
                self.obstaclesList.pop()
                self.spawnNewObstacle(Obstacles.basicObstacle)

    def drawScore(self):
        self.drawScoreBorder()
        self.drawScoreCounter()

    def drawScoreBorder(self):
        self.drawImage(GamePlayingDisplay.scoreBorderImage, (0, 0))

    def drawScoreCounter(self):
        self.drawImage(self.getScoreNumberImage(), GamePlayingDisplay.scoreCountDrawCoords)

    def getScoreNumberImage(self):
        scoreString = self.getScoreAsFormattedString()
        return GamePlayingDisplay.scoreFont.render(scoreString, True, GamePlayingDisplay.scoreFontColor)

    def getScoreAsFormattedString(self):
        return '{0:08d}'.format(self.score)

    def drawPlayer(self):
        self.drawImage(self.playerState.image, self.calculatePlayerDrawCoordinates())

    def calculatePlayerDrawCoordinates(self):
        x = GamePlayingDisplay.playerDrawCoordinates[0]
        y = GamePlayingDisplay.playerDrawCoordinates[1] - self.playerState.height
        return (x, y)

    def spawnNewObstacle(self, obstacle):
        coords = (GuiConfig.screenSize[0], GuiConfig.floorY - obstacle.getImage().get_size()[1])
        newObstacle = [obstacle, coords]
        self.obstaclesList.append(newObstacle)
