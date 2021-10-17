class Result:
    """A code template for a the result manager. The 
    responsibility of this class of objects is display 
    the result of the parachute in the game.
    
    Stereotype:
        Service Provider

    Attributes:
        turn_number (integer): Count the number of errors.
        close (boolean): Determines if the game should end.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Result): An instance of Result.
        """
        self.turn_number = 0
        self.close = False

    def stage(self,result):
        """The class constructor.
        
        Args:
            self (Result): an instance of Result.
            result(string): Helps determine the state of the parachute as the game progresses.
        """
        if result == "correct" and self.turn_number == 0 :
            print(f"\n  ___ \
            \n /___\ \
            \n \   / \
            \n  \ /  \
            \n   0   \
            \n  /|\  \
            \n  / \  \
            \n          \
            \n^^^^^^^")

        elif result == "correct" and self.turn_number == 1:
            print(f"\n /___\ \
        \n \   / \
        \n  \ /  \
        \n   0   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")
        elif result == "correct" and self.turn_number == 2:
            print(f"\n \   / \
        \n  \ /  \
        \n   0   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")

        elif result == "correct" and self.turn_number == 3:
            print(f"\n  \ /  \
        \n   0   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")
        elif result == "incorrect" and self.turn_number == 0:
            self.turn_number = self.turn_number + 1
            print(f"\n /___\ \
        \n \   / \
        \n  \ /  \
        \n   0   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")
        elif result == "incorrect" and self.turn_number == 1:
            self.turn_number = self.turn_number + 1
            print(f"\n \   / \
        \n  \ /  \
        \n   0   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")
        elif result == "incorrect" and self.turn_number == 2:
            self.turn_number = self.turn_number + 1
            print(f"\n  \ /  \
        \n   0   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")
        elif result == "incorrect" and self.turn_number == 3:
            self.turn_number = self.turn_number + 1
            print(f"\n   x   \
        \n  /|\  \
        \n  / \  \
        \n          \
        \n^^^^^^^")
            print(f"█░█ ▄▀▀▄ █░░█ . █░░ ▄▀▀▄ ▄▀▀ █▀▀ █\
    \n▀█▀ █░░█ █░░█ . █░░ █░░█ ░▀▄ █▀▀ ▀\
    \n░▀░ ░▀▀░ ░▀▀░ . ▀▀▀ ░▀▀░ ▀▀░ ▀▀▀ ▀")
            self.close = True
        if result == "win":
            print(f"█░░░█ ▀█▀ █▄░█ █▄░█ █▀▀ █▀▄\
\n█▄█▄█ ░█░ █▀██ █▀██ █▀▀ █▀▄\
\n▀▀░▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀░▀")
            self.close = True