import random


class Dice:
    """
    Represents a single die with a specified number of faces.
    """

    def __init__(self, faces=6):
        """
        Initializes a die with the given number of faces.
        """
        self.faces = faces

    def roll(self):
        """
        Rolls the die and returns a random value.
        """
        return random.randint(1, self.faces)
    

class DiceHand:
    """
    Represents a hand of dice.
    """

    def __init__(self, num_dice=2):
        """
        Initializes a hand with a given number of dice.
        """
        self.dice = [Dice() for _ in range(num_dice)]

    def roll_all(self):
        """
        Rolls all dice in the hand and returns the results.
        """
        return [dice.roll() for dice in self.dice]
