import unittest
from Pokerunner import Pokerunner
from GameStates.GameStates import GameStates

class PokerunnerTest(unittest.TestCase):
	def setUp(self):
		self.game = Pokerunner()
		
	def testShowMainMenu(self):
		self.game.showMainMenu()
		self.assertEqual(self.game.currentState, GameStates.MAIN_MENU)
