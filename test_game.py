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
def test_add_player(self):
        self.game.add_player("Alice")
        self.assertEqual(len(self.game.players), 1)
        self.assertEqual(self.game.players[0].get_name(), "Alice")

def test_set_computer_player(self):
        self.game.set_computer_player(level=1)
        self.assertEqual(len(self.game.players), 1)
        self.assertEqual(self.game.players[0].get_name(), "Computer")
        self.assertIsInstance(self.game.intelligence, Intelligence)

def test_switch_player(self):
        self.game.add_player("Alice")
        self.game.add_player("Bob")
        self.assertEqual(self.game.get_current_player().get_name(), "Alice")
        self.game.switch_player()
        self.assertEqual(self.game.get_current_player().get_name(), "Bob")
        self.game.switch_player()
        self.assertEqual(self.game.get_current_player().get_name(), "Alice")

@patch('builtins.input', side_effect=['roll', 'hold'])
@patch.object(DiceHand, 'roll_all', return_value=[4, 5])
def test_play_round_human(self, mock_roll_all, mock_input):
        self.game.add_player("Alice")
        self.game.play_round()
        player = self.game.get_current_player()
        self.assertEqual(player.get_score(), 9)

@patch('builtins.input', side_effect=['roll', 'roll', 'hold'])
@patch.object(DiceHand, 'roll_all', side_effect=[[4, 5], [1, 3]])
def test_play_round_human_lose_points(self, mock_roll_all, mock_input):
        self.game.add_player("Alice")
        self.game.play_round()
        player = self.game.get_current_player()
        self.assertEqual(player.get_score(), 0)

@patch.object(Intelligence, 'make_decision', side_effect=['roll', 'hold'])
@patch.object(DiceHand, 'roll_all', return_value=[4, 5])
def test_play_round_computer(self, mock_roll_all, mock_decision):
        self.game.set_computer_player(level=1)
        self.game.play_round()
        player = self.game.get_current_player()
        self.assertEqual(player.get_score(), 9)

def test_check_winner(self):
        self.game.add_player("Alice")
        self.game.add_player("Bob")
        self.game.players[0].add_score(100)
        self.assertTrue(self.game.check_winner())
        self.assertEqual(self.game.highscore.get_scores()["Alice"]["total_score"], 100)

def test_show_high_scores(self):
        self.game.add_player("Alice")
        self.game.players[0].add_score(100)
        self.game.highscore.update_score("Alice", 100)
        with patch('builtins.print') as mock_print:
            self.game.show_high_scores()
            mock_print.assert_any_call('Alice: 1 games, 100 points')

def test_show_rules(self):
        with patch('builtins.print') as mock_print:
            self.game.show_rules()
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()