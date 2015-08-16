import pygame
import Display
import Player

class Pokerunner:

	FRAMES_PER_SECOND = 30

	def __init__(self):
		pygame.init()

		self.clock = pygame.time.Clock()
		self.display = Display.Display()
		self.player = Player.Player()

		self.gameExit = False
		
		self.mainLoop()

	def mainLoop(self):
		while not self.gameExit:
			self.handleEvents()
			
			self.player.stepFrame()
			self.display.updatePlayerData(self.player.getCurrentPlayerState())
			self.display.updateScreen()
			self.clock.tick(Pokerunner.FRAMES_PER_SECOND)

	def handleEvents(self):
		for event in pygame.event.get():
			if self.isEventQuit(event):
				self.gameExit = True
			elif self.isEventKeyDown(event):
				self.handleKeyEvent(event)
					
	def isEventQuit(self, event):
		return event.type == pygame.QUIT
		
	def isEventKeyDown(self, event):
		return event.type == pygame.KEYDOWN
		
	def handleKeyEvent(self, event):
		if event.key == pygame.K_UP:
			self.player.changeMovementState(Player.MovementStates.JUMPING)
					
	def endGame(self):
		pygame.quit()
		quit()

Pokerunner()