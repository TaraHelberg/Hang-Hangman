"""
Used for libraries and imports
"""
import random    # Randomly selects word for Game
import os   # to use to clear screen
import colorama  # Adds color to game text
from colorama import Fore, Style
from constants import LOGO   # Hangman introduction Logo from constants.py
from constants import OPTIONS   # Hangman Options selection from constants.py
from constants import lives_left   # Hangman Lives visual from constants.py
from constants import GAMELEVEL   # Hangman level selection from constatnts.py
from constants import RULES   # Hangman Rules from constants.py

colorama.init(autoreset=True)


def game_intro():
    """
    Game Name "Logo" from patorjk.com
    Welcome's user, request users name and prints Hello users name
    """
    for logo in LOGO:
        print(f"{Fore.BLUE+Style.BRIGHT}{logo}")
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
            clear_screen()
            level = "default"
            num_lives = 10
            word = get_random_word()
            run_game(word, num_lives)
            return level
        elif choice == "2":
            start = True
            clear_screen()
            num_lives = select_game_level()
            word = get_random_word()
            run_game(word, num_lives)
        elif choice == "3":
            hangman_rules()
            input("Enter to return to Menu \n")
            print("\n")
            clear_screen()
            return start_game()
        else:
            print(f"{Fore.RED+Style.BRIGHT}Please select a level "
                  f"1 , 2 or 3 to make your Choice")
        clear_screen()


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
    for gamelevel in GAMELEVEL:
        print(f"{Fore.BLUE+Style.BRIGHT}{gamelevel}")
    level = False
    while not level:
        options = input("\n ").upper()
        if options == "E":
            level = True
            clear_screen()
            num_lives = 12
            return num_lives
        elif options == "M":
            level = True
            clear_screen()
            num_lives = 10
            return num_lives
        elif options == "H":
            level = True
            clear_screen()
            num_lives = 8
            return num_lives
        else:
            print(f"{Fore.RED+Style.BRIGHT}Please select a level E , M or H "
                  f"to make your Game Level Choice")


def get_random_word():
    """
    Picks a random word from words.txt & file encoding for hangman game
    How to found on stckoverflow: adpated for use in Hang-Hangman
    https://stackoverflow.com/questions/40835800/getting-a-random-word-from-a-text-file
    https://stackoverflow.com/questions/9896508/python-encoding-decoding-for-writing-to-a-text-file
    """
    random_word = random.choice(
        open("words.txt", "r", encoding="utf8").read().split('\n')
        )
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
    word_to_guess = "_" * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print("\n")
    print(f"Lives: {lives}\n")
    print("The word to guess: " + " ".join(word_to_guess) + "\n")

    while not game_over and lives > 0:
        user_try = input("Guess a letter:\n ").upper()
        try:
            if len(user_try) > 1:
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"You can only guess 1 letter at a time. "
                                 f"You guessed {len(user_try)} letter.")
            elif not user_try.isalpha():
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"You can only guess letters."
                                 f"You guessed {user_try},is not a letter.")
            elif len(user_try) == 1 and user_try.isalpha():
                if user_try in guesses:
                    raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                     f"You have already guessed {user_try}.")
                elif user_try not in word:
                    clear_screen()
                    print(f"{Fore.RED+Style.BRIGHT}"
                          f"{(user_try)} is not in the word.")
                    print(f"{Fore.RED+Style.BRIGHT}Sorry You Lose a Life!")
                    guesses.append(user_try)
                    lives -= 1
                else:
                    clear_screen()
                    print(f"{Fore.GREEN+Style.BRIGHT}"
                          f"{user_try} is in the word. Well done!")

                    guesses.append(user_try)
                    word_to_guess_list = list(word_to_guess)
                    indices = [i for i, letter in enumerate(word)
                               if letter == user_try]
                    for index in indices:
                        word_to_guess_list[index] = user_try
                        word_to_guess = "".join(word_to_guess_list)
                    if "_" not in word_to_guess:
                        game_over = True

        except ValueError as e_values:
            print(f"{e_values}.\n Please try again. :D\n")
            continue

        print(hangman_lives(lives))

        if lives > 0:
            print(f"Lives: {lives}\n")
            print("The word to guess: " + " ".join(word_to_guess) + "\n")
            print("Letters guessed: " + ", ".join(sorted(guesses)) + "\n")

    if game_over:
        print(f"{Fore.GREEN+Style.BRIGHT}Congratulations! YOU WON !")
    else:
        print(f"{Fore.RED+Style.BRIGHT}Sorry :( You Loose !! "
              f"The word you had to Guess was {word}")

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


def clear_screen():
    """
    Used to clear Terminal screen
    Credit: https://www.101computing.net/python-typing-text-effect/
    """
    os.system("clear")


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
