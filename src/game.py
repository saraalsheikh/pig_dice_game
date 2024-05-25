from player import Player
from dice import DiceHand
from highscore import HighScore
from intelligence import Intelligence

class Game:
    """
    Represents the game logic and state.
    """

    def __init__(self, name):
        self.name = name
        self.players = []
        self.dice_hand = DiceHand()
        self.highscore = HighScore()
        self.intelligence = None
        self.current_player_index = 0

    def add_player(self, name):
        self.players.append(Player(name))

    def set_computer_player(self, level):
        self.intelligence = Intelligence(level)
        self.add_player('Computer')

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_current_player(self):
        return self.players[self.current_player_index]

    def play_round(self):
        """
        Plays a round for the current player.
        """
        player = self.get_current_player()
        round_score = 0  # Håll koll på poäng för den aktuella rundan
        print(f"{player.get_name()}'s turn. Current total score: {player.get_score()}")
        while True:
            if player.get_name() == 'Computer':
                decision = self.intelligence.make_decision(player.get_score())
                print(f"Computer decides to {decision}")
            else:
                decision = input("Do you want to 'roll', 'hold', or 'cheat'? ")

            if decision == 'cheat':
                if self.cheat_to_win():
                    return  # Avsluta rundan omedelbart om fusk används
            elif decision == 'roll':
                roll = self.dice_hand.roll_all()
                print(f"Rolled: {roll}")
                if 1 in roll:
                    print(f"{player.get_name()} rolled one 1 and lost all points for this round!")
                    round_score = 0  # Nollställ bara rundans poäng, inte hela spelarens poäng
                    break
                else:
                    round_score += sum(roll)
                    print(f"{player.get_name()}'s round score: {round_score}, total score: {player.get_score() + round_score}")
            elif decision == 'hold':
                player.add_score(round_score)  # Lägg till rundans poäng till spelarens totala poäng
                print(f"{player.get_name()} holds with a round score of {round_score} and total score: {player.get_score()}")
                break
            else:
                print("Invalid decision, please choose 'roll', 'hold', or 'cheat'")
        self.switch_player()

    def check_winner(self):
        for player in self.players:
            if player.get_score() >= 100:
                print(f"{player.get_name()} wins with a score of {player.get_score()}!")
                self.highscore.update_score(player.get_name(), player.get_score())
                return True
        return False

    def show_rules(self):
        print("""
        Rules for Two-Pig Dice:

        1. The game is played with two dice.
        2. Players take turns to roll the dice as many times as they like.
        3. The goal is to reach 100 points.
        4. On a turn, a player can roll the dice repeatedly to accumulate points.
        5. If a player rolls a single '1', their turn ends and no points are added.
        6. If a player rolls two '1's, their entire score is reset to zero.
        7. A player can choose to 'pass' to end their turn and keep the points accumulated in that turn.
        8. The first player to reach 100 points wins the game.
        """)

    def show_high_scores(self):
        scores = self.highscore.get_scores()
        for player, data in scores.items():
            print(f"{player}: {data['games_played']} games, {data['total_score']} points")

    def cheat_to_win(self):
        player = self.get_current_player()
        player.add_score(100)
        print(f"{player.get_name()} har fuskat och vinner med en poäng på 100!")
        self.highscore.update_score(player.get_name(), player.get_score())
        return True
