import pygame
from GameStates import GameStates
from GameStates.GamePlayingState import GamePlayingDisplay
from GameStates.GamePlayingState import GamePlayingPlayer

class GamePlayingStateManager(object):
	def __init__(self, screen):
		self.display = GamePlayingDisplay.GamePlayingDisplay(screen)
		self.player = GamePlayingPlayer.GamePlayingPlayer()
		
	def tick(self):
		self.player.stepFrame()
		self.player.incrementScore()
		self.display.setScore(self.player.getScore())
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
		elif event.key == pygame.K_p:
			transitionToPaused()
			
	def reset(self):
		pass

def transitionToPaused():
	raise GameStates.StateTransition(GameStates.GameState.PAUSED)