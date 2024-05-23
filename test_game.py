import unittest
from unittest.mock import patch, MagicMock
from src.game import Game
from src.player import Player
from src.dice import DiceHand
from src.highscore import HighScore
from src.intelligence import Intelligence

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
