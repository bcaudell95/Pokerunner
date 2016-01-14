screenSize = (1024,768)
floorY = 641
scoreBorderDimensions = (256, 64)

playerFramesPerAnimation = 4
playerForms = 2
playerInputFrameSize = (784, 614)
playerFrameScale = .35
playerFrameSize = list(map(lambda x : playerFrameScale*x, playerInputFrameSize))
playerFrameBottomMargin = 8
playerDrawCoords = (10, floorY-playerFrameSize[1]+playerFrameBottomMargin)

scoreFontFile = 'assets/fonts/AndaleMono.ttf'
scoreFontSizePts = 48
scoreFontColor = (0, 0, 0)
scoreDrawCoords = (5, 10)

# Color of the health bar changes depending on health
healthMinY = 20
healthMaxY = 80
healthMaxX = 1000
healthDrawColors = [
	(255,0,0), 		# Red - Low
	(255,106,0),	# Orange
	(255,216,0),	# Yellow
	(182,255,0),	# Lime
	(0,255,33)]		# Green - High