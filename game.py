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

    def set_computer_player(self, level):
        """
        Sets up a computer player with a specified intelligence level.
        """
        self.intelligence = Intelligence(level)
        self.add_player('Computer')

    def switch_player(self):
        """
        Switches to the next player.
        """
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    
    def get_current_player(self):
        """
        Returns the current player.
        """
        return self.players[self.current_player_index]
    
    def play_round(self):
        """
        Plays a round for the current player.
        """
        player = self.get_current_player()
        print(f"{player.get_name()}'s turn")
        while True:
            if player.get_name() == 'Computer':
                decision = self.intelligence.make_decision(player.get_score())
                print(f"Computer decides to {decision}")
            else:
                decision = input("Do you want to 'roll', 'hold', or 'cheat'? ")

            if decision == 'cheat':
                if self.cheat_to_win():
                    return  # End the round immediately if cheat is used
            elif decision == 'roll':
                roll = self.dice_hand.roll_all()
                print(f"Rolled: {roll}")
                if 1 in roll:
                    player.reset_score()
                    print(f"{player.get_name()} rolled one 1 and lost all points!")
                    break
                else:
                    player.add_score(sum(roll))
                    print(f"{player.get_name()}'s score: {player.get_score()}")
            elif decision == 'hold':
                print(f"{player.get_name()} holds with score: {player.get_score()}")
                break
            else:
                print("Invalid decision, please choose 'roll', 'hold' or 'cheat'")
        self.switch_player()
    
    def check_winner(self):
        """
        Checks if any player has won the game.
        """
        for player in self.players:
            if player.get_score() >= 100:
                print(f"{player.get_name()} wins with a score of {player.get_score()}!")
                self.highscore.update_score(player.get_name(), player.get_score())
                return True
        return False
    
    def show_rules(self):
        """
        Displays the game rules.
        """
        print("""\n
            Rules for Two-Pig Dice:

            1. The game is played with two dice.
            2. Players take turns to roll the dice as many times as they like.
            3. The goal is to reach 100 points.
            4. On a turn, a player can roll the dice repeatedly to accumulate points.
            5. If a player rolls a single '1', their turn ends and no points are added.
            6. If a player rolls two '1's, their entire score is reset to zero.
            7. A player can choose to 'pass' to end their turn and keep the points accumulated in that turn.
            8. The first player to reach 100 points wins the game.\n""")
