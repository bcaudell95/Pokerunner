from enum import Enum


class Elements(Enum):
	NORMAL = 0
	FIRE = 1


elementImagesDict = {'NORMAL': 'runningcat_50.png', 'FIRE': 'runningcat_50_2.png'}

def getElementSheetFile(element):
	imagesDirectory = 'assets/images/'
	if element in elementImagesDict.keys():
		return imagesDirectory + elementImagesDict[element]
	else:
		return ''
