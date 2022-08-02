import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
""""
Python colorama , color text information
and how to use gotten from the below video
https://www.youtube.com/watch?v=u51Zjlnui4Y
"""


def game_intro():
    """
    Game Name "Logo",Welcome's user,
    request users name
    and prints Hello users name
    """
    print(
        f"""{Fore.BLUE+Style.BRIGHT}
         _   _
        | | | | __ _ _ __   __ _
        | |_| |/ _` | '_ \\ / _` |
        |  _  | (_| | | | | (_| |    _______
        |_| |_|\\__,_|_| |_|\\__, |
        |___/
         _   _
        | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
        | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\
        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                            |___/
        """
    )
    print("Welcome to Hang-Hangman")
    print("We hope you have fun!")
    name = None

    while True:
        name = input(f"{Fore.GREEN+Style.BRIGHT}What is your name?\n")

        if not name.isalpha():
            print(f"{Fore.RED+Style.BRIGHT}Your name must be alphabetic only")
            continue
        else:
            print(f'Hello, {name}')
            break


def start_game():
    """
    Starts the game off with options of:
    1 to play right away
    2 to select level of play
    3 to see the game Rules
    """
    print("Press 1 to Start playing Hang-Hangman")
    print("Press 2 to select the level to play at")
    print("Press 3 to read The Hang-Hangman Rules")
    start = False
    while not start:
        choice = input("\n")
        if choice == "1":
            start = True
            return "default"
        elif choice == "2":
            start = True
            num_lives = select_game_level()
            word = get_random_word()
            run_game(word, num_lives)
        elif choice == "3":
            hangman_rules()
            input("Enter to return to Menu \n")
            print("\n")
            return start_game()
        else:
            print(f"{Fore.RED+Style.BRIGHT}Please select a level"
                  f"1 , 2 or 3 to make your Choice")


def hangman_rules():
    """
    Explains to the User how to play the game.
    """
    print(f"{Fore.BLUE+Style.BRIGHT}Welcome to Hang-Hangman! ")
    print(f"{Fore.BLUE+Style.BRIGHT}How to play Rules :D.")
    print(f"{Fore.BLUE+Style.BRIGHT}This is a guess the word game.")
    print(f"{Fore.BLUE+Style.BRIGHT}Guess 1 letter at a time or "
          f"you can guess the word !")
    print(f"{Fore.BLUE+Style.BRIGHT}If you guess the wrong letter."
          f"You loose a life :( Sorry.")
    print(f"{Fore.BLUE+Style.BRIGHT}Your Hangman will then start to build.")
    print(f"{Fore.BLUE+Style.BRIGHT}When you reach 0 lives :("
          f" You will be HANGED!")
    print(f"{Fore.BLUE+Style.BRIGHT}Don't worry you can restart the game!"
          f"Play again and WIN :D ")


def select_game_level():
    """
    Lets the User select the level of Hang-Hangman.
    The user can select to play E for Easy, M for Medium or H for Hard.
    """
    print("Select the level you wish to play at.")
    print("Press E for Easy")
    print("Press M for Medium")
    print("Press H for Hard")
    level = False
    while not level:
        options = input("\n ").upper()
        if options == "E":
            level = True
            num_lives = 12
            return num_lives
        elif options == "M":
            level = True
            num_lives = 10
            return num_lives
        elif options == "H":
            level = True
            num_lives = 8
            return num_lives
        else:
            print(f"{Fore.RED+Style.BRIGHT}Please select a level E , M or H"
                  f"to make your Game Level Choice")


def get_random_word():
    """
    Picks a random word from words.txt for hangman word to be guessed by user.
    How to found on stckoverflow:
    https://stackoverflow.com/questions/40835800/getting-a-random-word-from-a-text-file
    adpated for use in Hang-Hangman
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def hangman_lives(lives):
    """
    Displays Hang-Hangman visuals to show man been hung on letter not in word.
    """
    lives_left = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
        """,
        """
        |
        |
        |
        ========
        """,
        """
        |
        ========
        """,
        """
        """
    ]
    return lives_left[lives]


def run_game(word, num_lives):
    """
    Runs the Hang-Hangman game.
    Hang-Hangman is based around the YouTube video
    https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    word_dictonary = "_" * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print("\n")
    print(f"Lives: {lives}\n")
    print(f"The word to guess: " + " ".join(word_dictonary) + "\n")

    while not game_over and lives > 0:
        user_try = input(" Guess a letter:\n ").upper()
        try:
            if len(user_try) > 1:
                raise ValueError(f"You can only guess 1 letter at a time,"
                                 f"you guessed {len(user_try)} letter")
            elif not user_try.isalpha():
                raise ValueError(f"You can only guess letters,"
                                 f"you guessed {(user_try)},is not a letter")
            elif len(user_try) == 1 and user_try.isalpha():
                if user_try in guesses:
                    raise ValueError(f" You have already guessed {(user_try)}")
                elif user_try not in word:
                    print(f"{(user_try)}is not in the word."
                          f"Sorry You Lose a Life!")
                    guesses.append(user_try)
                    lives -= 1
                else:
                    print(f"{user_try} is in the word. Well done!")
                    guesses.append(user_try)
                    word_dictonary_list = list(word_dictonary)
                    indices = [i for i, letter in enumerate(word)
                               if letter == user_try]
                    for index in indices:
                        word_dictonary_list[index] = user_try
                        word_dictonary = "".join(word_dictonary_list)
                    if "_" not in word_dictonary:
                        game_over = True

        except ValueError as e:
            print(f"{e}.\n Please try again. :D\n")
        continue

        print(hangman_lives(lives))

        if lives > 0:
            print(f"Lives: {lives}\n")
            print(f"The word to guess: " + " ".join(word_dictonary) + "\n")
            print(f"Letters guessed: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
        print(f"Congratulations! YOU WON !")
    else:
        print(f"The word you had to Guess was {word}")

    restart_game()


def restart_game():
    """
    Gives User the choice to Restart the Game or Return to Introduction
    """
    game_restart = False

    while not game_restart:
        restart = input(f"Would You Like To Play Again :) ?"
                        f"Please Type Y for Yes & N for No: ")
        try:
            if restart == "Y":
                game_restart = True
                start_game()
            elif restart == "N":
                game_restart = True
                print("\n")
                main()
            else:
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"Please type either Y or N,"
                                 f"to make your Choice.You typed{(restart)}")

        except ValueError as e:
            print(f"{Fore.RED+Style.BRIGHT} Please Try again Thank You :D")


def main():
    """
    Run all program functions as on Game
    """
    game_intro()
    level = start_game()
    if level == "default":
        num_lives = 10
    else:
        num_lives = select_game_level()

    word = get_random_word()
    run_game(word, num_lives)


main()
