import unittest
from src.highscore import HighScore
import os


class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'test_highscores.json'
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        self.highscore = HighScore(self.test_filename)