import pygame

class Display:

    screenSize = (1024,768)
    backdropSize = (3072,768)

    backdrop1File = 'assets/images/backdrop.png'
    backdrop2File = 'assets/images/backdrop1.png'

    playerDrawCoordinates = (100, 512)
    
    playerSpeedX = 10

    def __init__(self):
        self.screen = pygame.display.set_mode(Display.screenSize)

        backdrop1 = pygame.image.load(Display.backdrop1File)
        backdrop2 = pygame.image.load(Display.backdrop2File)
        self.backdrops = [backdrop1, backdrop2]

        self.currentBackdrop = self.backdrops[0]
        self.nextBackdrop = self.backdrops[1]

        self.playerX = 0

    def update(self, playerState):
        Display.updatePlayer(self, playerState)
        pygame.display.update()

    def updatePlayer(self, playerState):
        self.playerX += Display.playerSpeedX
        if self.playerX >= Display.backdropSize[0]:
            self.playerX -= Display.backdropSize[0]
            temp = self.currentBackdrop
            self.currentBackdrop = self.nextBackdrop
            self.nextBackdrop = temp

        # Blit backdrop
        self.screen.blit(self.currentBackdrop, (-1 * self.playerX,0))
        if self.playerX >= Display.backdropSize[0] - Display.screenSize[0]:
            self.screen.blit(self.nextBackdrop, (Display.backdropSize[0] - self.playerX,0))

        # Blit player image
        coords = (Display.playerDrawCoordinates[0], Display.playerDrawCoordinates[1] - playerState[1])
        self.screen.blit(playerState[0], coords)
