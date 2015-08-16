from enum import Enum

class GameState(Enum):
	MAIN_MENU = 0
	PLAYING = 1
	PAUSED = 2
	CREDITS = 3
	
class StateTransition(Exception):
	def __init__(self, stateToTransitionTo):
		self.stateToTransitionTo = stateToTransitionTo