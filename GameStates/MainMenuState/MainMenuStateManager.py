import pygame
from GameStates.MainMenuState import MainMenuDisplay

class MainMenuStateManager(object):
	
	def __init__(self, screen):
		self.display = MainMenuDisplay.MainMenuDisplay(screen)
	
	def tick(self):
		self.display.updateScreen()
	
	def handleEvent(self, event):
		if pygame.MOUSEMOTION == event.type:
			self.display.setMouseCoords(pygame.mouse.get_pos())
		elif pygame.MOUSEBUTTONDOWN == event.type:
			self.display.clicked(pygame.mouse.get_pressed())
	
	def changeMouseOver(self, newMousePos):
		self.mousePos = newMousePos
		
	def reset(self):
		pass
		