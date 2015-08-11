import spriteSheet

class FormSheet(object):

    FRAME_DIMENSIONS = (256, 128)    # Dimensions for one image
    ROWS = 8                        # Number of images per sprite sheet
    SHEET_DIMENSIONS = (FRAME_DIMENSIONS[0], FRAME_DIMENSIONS[1]*ROWS)  #Dimensions for a sprite sheet
    STATES_COUNT = 2                # Number of sheets per image
    
    def __init__(self, filename):
        self.sheets = []
        for i in range(FormSheet.STATES_COUNT):
            self.sheets.append(spriteSheet.spritesheet(filename, FormSheet.SHEET_DIMENSIONS, i*FormSheet.SHEET_DIMENSIONS[1], FormSheet.ROWS))

    def getStateSheet(self, i):
        return self.sheets[i]
