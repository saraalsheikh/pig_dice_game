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
