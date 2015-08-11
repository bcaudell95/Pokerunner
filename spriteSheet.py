import pygame

class spritesheet(object):
    def __init__(self, filename, dimensions, yOffset, rows):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
            rectWidth = dimensions[0]
            rectHeight = dimensions[1]/rows

            rects = [(0, i*rectHeight + yOffset, rectWidth, rectHeight) for i in range(rows)]
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

    def getImage(self, i):
        return self.images[i]
