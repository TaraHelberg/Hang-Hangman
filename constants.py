"""
Game Name "Logo" Logo from patorjk.com & Welcome's user
"""
LOGO = [
        """
        HH   HH   AAA   NN   NN   GGGG
        HH   HH  AAAAA  NNN  NN  GG  GG
        HHHHHHH AA   AA NN N NN GG         _____
        HH   HH AAAAAAA NN  NNN GG   GG
        HH   HH AA   AA NN   NN  GGGGGG
        """
        """
        HH   HH   AAA   NN   NN   GGGG  MM    MM   AAA   NN   NN
        HH   HH  AAAAA  NNN  NN  GG  GG MMM  MMM  AAAAA  NNN  NN
        HHHHHHH AA   AA NN N NN GG      MM MM MM AA   AA NN N NN
        HH   HH AAAAAAA NN  NNN GG   GG MM    MM AAAAAAA NN  NNN
        HH   HH AA   AA NN   NN  GGGGGG MM    MM AA   AA NN   NN
        """,
        "Welcome to Hang-Hangman",
        "We hope you have fun!"
]
"""
Starts the game off with options of:
    1 to play right away, default level medium
    2 to select level of play
    3 to see the game Rules
"""
OPTIONS = [
    "Press 1 to Start playing Hang-Hangman",
    "Press 2 to select the level to play at",
    "Press 3 to read The Hang-Hangman Rules"
]
"""
Explains to the User how to play the game.
"""
RULES = [
    "Welcome to Hang-Hangman!",
    "How to play Rules :D.",
    "This is a guess the word game.",
    "Guess 1 letter at a time or you can guess the word !",
    "If you guess the wrong letter.You loose a life :( Sorry.",
    "Your Hangman will then start to build.",
    "When you reach 0 lives :( You will be HANGED!",
    "Don't worry you can restart the game!",
    "Play again and WIN :D "
    ]
"""
Lets the User select the level of Hang-Hangman.
"""
GAMELEVEL = [
    "Select the level you wish to play at.",
    "Press E for Easy, 12 Lives",
    "Press M for Medium, 10 Lives",
    "Press H for Hard, 8 Lives"
]
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
