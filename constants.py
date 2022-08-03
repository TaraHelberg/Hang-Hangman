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
