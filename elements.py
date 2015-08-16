from enum import Enum

class Elements(Enum):
	NORMAL = 0

def getElementSheetFile(element):
	imagesDirectory = 'assets/images/'
	if Elements.NORMAL.name == element:
		return imagesDirectory + 'runningcat_50.png'
	else:
		return ''
