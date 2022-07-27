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


def hangman_rules():
    """
    Explains to the User how to play the game.      
    """
    print(f"{Fore.BLUE+Style.BRIGHT}Welcome to Hang-Hangman How to play Rules:D.")
    print(f"{Fore.BLUE+Style.BRIGHT}This is a guess the word game.")
    print(f"{Fore.BLUE+Style.BRIGHT}Guess 1 letter at a time or guess the entire word !")
    print(f"{Fore.BLUE+Style.BRIGHT}If you guess the wrong letter you loose a life :( Sorry.")
    print(f"{Fore.BLUE+Style.BRIGHT}Your Hang-Hangman will then start to build.")
    print(f"{Fore.BLUE+Style.BRIGHT}When you reach 0 lives your will be HANGED !")
    print(f"{Fore.BLUE+Style.BRIGHT}Don't worry you can restart the game to play again and WIN :D ")


def select_game_level():
    """
    Lets the User select the level of Hang-Hangman. 
    The user can select to play E for Easy, M for Medium or H for Hard. 
    """
    print("Select the level you wish to play at.")
    print("Press E for Easy")
    print("Press M for Medium")
    print("Press H for Hard")
    difficulty = False
    while not difficulty:
        options = input("\n ").upper()
        if options == "E":
            difficulty = True
            num_lives = 10
            return num_lives
        elif options == "M":
            difficulty = True
            num_lives = 7
            return num_lives
        elif options == "H":
            difficulty = True
            num_lives = 5
            return num_lives
        else:
            print(f"{Fore.RED+Style.BRIGHT}Please select a level E , M or H to make your Choice")
    

def get_random_word():
    """
    Picks a random word from words.txt for hangman word to be guessed by user.
    How to found on https://stackoverflow.com/questions/40835800/getting-a-random-word-from-a-text-file
    adpated for use in Hang-Hangman
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def hangman_lives(lives):
    """
    Displays Hang-Hangman visuals to show man been hung on wrong word letter choice
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
        """
    ]
    return lives_left[lives]


def main():
    """
    Run all program functions
    """
    game_intro()
    hangman_rules()
    select_game_level() 

main()
