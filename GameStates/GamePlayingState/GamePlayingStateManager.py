import pygame
from GameStates.GamePlayingState import GamePlayingDisplay
from GameStates.GamePlayingState import GamePlayingPlayer

class GamePlayingStateManager(object):
	def __init__(self):
		self.display = GamePlayingDisplay.GamePlayingDisplay()
		self.player = GamePlayingPlayer.GamePlayingPlayer()
		
	def tick(self):
		self.player.stepFrame()
		self.display.updatePlayerData(self.player.getCurrentPlayerState())
		self.display.updateScreen()
		
	def handleEvent(self, event):
		if self.isEventKeyDown(event):
			self.handleKeyEvent(event)
	
	def isEventKeyDown(self, event):
		return event.type == pygame.KEYDOWN
		
	def handleKeyEvent(self, event):
		if event.key == pygame.K_UP:
			self.player.changeMovementState(GamePlayingPlayer.MovementStates.JUMPING)