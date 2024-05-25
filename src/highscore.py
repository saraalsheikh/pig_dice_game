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

    def save_scores(self):
        """
        Saves scores to a file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.scores, file)

    def update_score(self, player_name, score):
        """
        Updates the score for a player.
        """
        if player_name in self.scores:
            self.scores[player_name]['games_played'] += 1
            self.scores[player_name]['total_score'] += score
        else:
            self.scores[player_name] = {'games_played': 1, 'total_score': score}
        self.save_scores()

    def get_scores(self):
        """
        Returns all stored scores.
        """
        return self.scores
