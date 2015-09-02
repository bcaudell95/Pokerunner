import pygame
from GameStates.GameStates import GameStates

class Pokerunner(object):
	def __init__(self):
		self.currentState = None
		
	def start(self):
		pass
		
	def showMainMenu(self):
		self.currentState = GameStates.MAIN_MENU
		