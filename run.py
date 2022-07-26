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
            print(f"{Fore.RED+Style.BRIGHT}Username must be alphabets only")
            continue
        else:
            print(f'Hello, {name}')
            break



def main():
    """
    Run all program functions
    """
    game_intro()

main()
