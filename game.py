from src.player import Player
from src.dice import DiceHand
from src.highscore import HighScore
from src.intelligence import Intelligence


class Game:
    """
    Represents the game logic and state.
    """

    def __init__(self):
        """
        Initializes the game with default values.
        """
        self.players = []
        self.dice_hand = DiceHand()
        self.highscore = HighScore()
        self.intelligence = None
        self.current_player_index = 0
    
    def add_player(self, name):
        """
        Adds a new player to the game.
        """
        self.players.append(Player(name))