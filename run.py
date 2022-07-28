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
            num_lives = 12
            return num_lives
        elif options == "M":
            difficulty = True
            num_lives = 10
            return num_lives
        elif options == "H":
            difficulty = True
            num_lives = 8
            return num_lives
        else:
            print(f"{Fore.RED+Style.BRIGHT}Please select a level E , M or H to make your Game Level Choice")
    

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


def run_game(word, num_lives):
    """
    Runs the Hang-Hangman game.
    Hang-Hangman is based around the YouTube video https://www.youtube.com/watch?v=m4nEnsavl6w
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
                raise ValueError(f" You can only guess 1 letter at a time, you guessed {len(user_try)} letter")

            elif not user_try.isalpha():
                raise ValueError(f"You can only guess letters, you guessed {(user_try)},which is not a letter")

            elif len(user_try) == 1 and user_try.isalpha():
                if user_try in guesses:
                    raise ValueError(f" You have already guessed {(user_try)}")

                elif user_try not in word:

                    print(f"{(user_try)}is not in the word. Sorry You Lose a Life!")
                                        
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


def main():
    """
    Run all program functions as on Game
    """
    game_intro()
    hangman_rules()
    select_game_level()
    run_game() 

main()
