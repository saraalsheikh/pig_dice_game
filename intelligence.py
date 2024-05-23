class Intelligence:
    """
    Manages the decision-making logic for the computer player.
    """

    def __init__(self, level='easy'):
        """
        Initializes the intelligence level for the computer player.
        """
        self.level = level

    def make_decision(self, current_score):
        """
        Makes a decision based on the current score and intelligence level.
        """
        if self.level == 'easy':
            return 'roll' if current_score < 20 else 'hold'
        elif self.level == 'medium':
            return 'roll' if current_score < 25 else 'hold'
        elif self.level == 'hard':
            return 'roll' if current_score < 30 else 'hold'
        