import json
import os


class HighScore:
    """
    Manages the high scores for the game.
    """

def __init__(self, filename='highscores.json'):
        """
        Initializes the high score manager with a file to store scores.
        """
        self.filename = filename
        self.scores = self.load_scores()

