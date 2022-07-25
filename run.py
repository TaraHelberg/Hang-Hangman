import random
import colorama
from colorama import Fore, Back, Style
colorama.init()


def game_intro():
    """
    Game Name "Logo" , Welcome's user and request users name and prints Hello users name 
    """
    print(
        """
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
    print("Welcome")
    name = input('What is your name?\n')
    print(f'Hello, {name}')
    
game_intro()
