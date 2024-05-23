import unittest
from src.dice import Dice, DiceHand


class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice(faces=6)
        result = dice.roll()
        self.assertTrue(1 <= result <= 6)