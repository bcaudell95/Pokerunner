from enum import Enum

class Elements(Enum):
	NORMAL = 0
	
elementImagesDict = {'NORMAL': 'runningcat_50.png'}

def getElementSheetFile(element):
	imagesDirectory = 'assets/images/'
	return imagesDirectory + elementImagesDict[element]
