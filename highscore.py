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

def load_scores(self):
        """
        Loads scores from a file.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}