from src.game import Game

def main():
    """
    The main function to run the game.
    """
    game = Game()

    while True:
        print("\n1. Play against computer\n2. Play with friend\n3. Show high scores\n4. Show rules\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter your name: ")
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
            game.add_player(name1)
            game.add_player(name2)
            while True:
                game.play_round()
                if game.check_winner():
                    break
        elif choice == '3':
            game.show_high_scores()
        elif choice == '4':
            game.show_rules()
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()