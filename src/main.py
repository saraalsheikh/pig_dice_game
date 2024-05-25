from game import Game

def main():
    """
    The main function to run the game.
    """
    while True:
        print("\n1. Play against computer\n2. Play with friend\n3. Show high scores\n4. Show rules\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
            game = Game(name)  # Initiera spelet med spelarens namn
            game.add_player(name)
            level = input("Choose computer difficulty (easy, medium, hard): ")
            game.set_computer_player(level)
            while True:
                game.play_round()
                if game.check_winner():
                    break
        elif choice == '2':
            name1 = input("Enter name for Player 1: ")
            name2 = input("Enter name for Player 2: ")
            game = Game(name1)  # Initiera spelet med den första spelarens namn
            game.add_player(name1)
            game.add_player(name2)
            while True:
                game.play_round()
                if game.check_winner():
                    break
        elif choice == '3':
            game = Game("HighScoresViewer")  # Temporär initiering för att visa höga poäng
            game.show_high_scores()
        elif choice == '4':
            game = Game("RulesViewer")  # Temporär initiering för att visa regler
            game.show_rules()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
