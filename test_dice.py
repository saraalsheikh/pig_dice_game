import unittest
from src.dice import Dice, DiceHand


class TestDice(unittest.TestCase):
    def test_roll(self):
        dice = Dice(faces=6)
        result = dice.roll()
        self.assertTrue(1 <= result <= 6)

class TestDiceHand(unittest.TestCase):
    def test_roll_all(self):
        dice_hand = DiceHand(num_dice=2)
        result = dice_hand.roll_all()
        self.assertEqual(len(result), 2)
        for roll in result:
            self.assertTrue(1 <= roll <= 6)