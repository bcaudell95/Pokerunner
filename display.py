import pygame

class spritesheet(object):
    def __init__(self, filename, dimensions, rows):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
            rectWidth = dimensions[0]
            rectHeight = dimensions[1]/rows

            rects = [(0, i*rectHeight, rectWidth, rectHeight) for i in range(rows)]
            self.images = []
            for r in rects:
                rect = pygame.Rect(r)
                image = pygame.Surface(rect.size).convert_alpha()
                image.fill((0,0,0,0))
                image.blit(self.sheet, (0,0), rect)
                self.images.append(image)                 
        except pygame.error as message:
            print('Unable to load spritesheet image:', filename)
            quit()

class Display:

    screenSize = (1024,768)
    backdropSize = (3072,768)

    backdrop1File = 'assets/images/backdrop.png'
    backdrop2File = 'assets/images/backdrop1.png'

    playerSpriteSheetFile = 'assets/images/runningcat_50.png'
    playerSpriteSheetSize = (256,1024)
    playerSpriteCount = 8
    playerDrawCoordinates = (100, 512)
    
    playerSpeedX = 10
    framesPerPlayerMove = 3

    def __init__(self):
        self.screen = pygame.display.set_mode(Display.screenSize)

        backdrop1 = pygame.image.load(Display.backdrop1File)
        backdrop2 = pygame.image.load(Display.backdrop2File)
        self.backdrops = [backdrop1, backdrop2]
        
        self.playerSprites = spritesheet(Display.playerSpriteSheetFile, Display.playerSpriteSheetSize, Display.playerSpriteCount)
        self.currentPlayerImage = 0
        self.frameCount = 0

        self.currentBackdrop = self.backdrops[0]
        self.nextBackdrop = self.backdrops[1]

        self.playerX = 0

    def update(self):
        Display.updatePlayer(self)
        pygame.display.update()

    def updatePlayer(self):
        self.playerX += Display.playerSpeedX
        if self.playerX >= Display.backdropSize[0]:
            self.playerX -= Display.backdropSize[0]
            temp = self.currentBackdrop
            self.currentBackdrop = self.nextBackdrop
            self.nextBackdrop = temp

        self.screen.blit(self.currentBackdrop, (-1 * self.playerX,0))
        if self.playerX >= Display.backdropSize[0] - Display.screenSize[0]:
            self.screen.blit(self.nextBackdrop, (Display.backdropSize[0] - self.playerX,0))

        self.screen.blit(self.playerSprites.images[self.currentPlayerImage], Display.playerDrawCoordinates)
        self.frameCount += 1
        if self.frameCount == Display.framesPerPlayerMove:
            self.frameCount = 0
            self.currentPlayerImage += 1
            if self.currentPlayerImage == Display.playerSpriteCount:
                self.currentPlayerImage = 0
