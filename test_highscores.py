import unittest
from src.highscore import HighScore
import os


class TestHighScore(unittest.TestCase):
    def setUp(self):
        self.test_filename = 'test_highscores.json'
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        self.highscore = HighScore(self.test_filename)
    
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_update_score(self):
        self.highscore.update_score('Player1', 50)
        self.highscore.update_score('Player1', 25)
        self.assertEqual(self.highscore.get_scores()['Player1']['games_played'],2)
        self.assertEqual(self.highscore.get_scores()['Player1']['total_score'], 75)
        self.highscore.update_score('Player2', 100)
        self.assertEqual(self.highscore.get_scores()['Player2']['games_played'], 1)
        self.assertEqual(self.highscore.get_scores()['Player2']['total_score'], 100)

    def test_get_scores(self):
        self.highscore.update_score('Player1', 50)
        self.highscore.update_score('Player2', 100)
        scores = self.highscore.get_scores()
        self.assertEqual(scores['Player1']['games_played'], 1)
        self.assertEqual(scores['Player1']['total_score'], 50)
        self.assertEqual(scores['Player2']['games_played'], 1)
        self.assertEqual(scores['Player2']['total_score'], 100)


if __name__ == '__main__':
    unittest.main()

