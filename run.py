"""
Used for libraries and imports
"""
import random    # Randomly selects word for Game
import colorama  # Adds color to game text
from colorama import Fore, Style
from constants import LOGO   # Hangman introduction Logo from constants.py
from constants import OPTIONS   # Hangman Menu Options selection from constants.py
from constants import lives_left   # Hangman Lives visual from constants.py
from constants import RULES   # Hangman Rules from constants.py
colorama.init(autoreset=True)


def game_intro():
    """
    Game Name "Logo"
    Logo from patorjk.com
    ,Welcome's user,
    request users name
    and prints Hello users name
    """
    for logo in LOGO:
        print(f"{Fore.BLUE+Style.BRIGHT}{logo}")
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
    1 to play right away, default level medium
    2 to select level of play
    3 to see the game Rules
    """
    for options in OPTIONS:
        print(f"{Fore.BLUE+Style.BRIGHT}{options}")
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
    for rule in RULES:
        print(f"{Fore.BLUE+Style.BRIGHT}{rule}")


def select_game_level():
    """
    Lets the User select the level of Hang-Hangman.
    The user can select to play E for Easy, M for Medium or H for Hard.
    """
    print("Select the level you wish to play at.")
    print("Press E for Easy, 12 Lives")
    print("Press M for Medium, 10 Lives")
    print("Press H for Hard, 8 Lives")
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
    for _ in lives_left:
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
    print("The word to guess: " + " ".join(word_dictonary) + "\n")

    while not game_over and lives > 0:
        user_try = input(" Guess a letter:\n ").upper()
        try:
            if len(user_try) > 1:
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"You can only guess 1 letter at a time,"
                                 f"you guessed {len(user_try)} letter")
            elif not user_try.isalpha():
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"You can only guess letters,"
                                 f"you guessed {(user_try)},is not a letter")
            elif len(user_try) == 1 and user_try.isalpha():
                if user_try in guesses:
                    raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                     f"You have already guessed {(user_try)}")
                elif user_try not in word:
                    print(f"{Fore.RED+Style.BRIGHT}"
                          f"{(user_try)} is not in the word.")
                    print(f"{Fore.RED+Style.BRIGHT}Sorry You Lose a Life!")
                    guesses.append(user_try)
                    lives -= 1
                else:
                    print(f"{Fore.GREEN+Style.BRIGHT}"
                          f"{user_try} is in the word. Well done!")

                    guesses.append(user_try)
                    word_dictonary_list = list(word_dictonary)
                    indices = [i for i, letter in enumerate(word)
                               if letter == user_try]
                    for index in indices:
                        word_dictonary_list[index] = user_try
                        word_dictonary = "".join(word_dictonary_list)
                    if "_" not in word_dictonary:
                        game_over = True

        except ValueError as e_values:
            print(f"{e_values}.\n Please try again. :D\n")
            continue

        print(hangman_lives(lives))

        if lives > 0:
            print(f"Lives: {lives}\n")
            print("The word to guess: " + " ".join(word_dictonary) + "\n")
            print("Letters guessed: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
        print(f"{Fore.GREEN+Style.BRIGHT}Congratulations! YOU WON !")
    else:
        print(f"The word you had to Guess was {word}")

    restart_game()


def restart_game():
    """
    Gives User the choice to Restart the Game or Return to Introduction
    """
    game_restart = False

    while not game_restart:
        restart = input(f"{Fore.GREEN+Style.BRIGHT}"
                        f"Would You Like To Play Again :) ? "
                        f"Please Type Y for Yes & N for No: ").upper()
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

        except ValueError as e_values:
            print(f"{e_values}.\n{Fore.RED+Style.BRIGHT}"
                  f"Please Try again Thank You :D\n")


def main():
    """
    Runs all program functions used for the Game
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
