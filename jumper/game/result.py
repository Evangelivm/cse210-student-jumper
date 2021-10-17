class Result:
    """A code template for a the result manager. The 
    responsibility of this class of objects is display 
    the result of the parachute in the game.
    
    Stereotype:
        

    Attributes:
        location (integer): The location of the Seeker (1-1000).
        distance (list): The distance travelled with each move.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self.turn_number = 0
        self.close = False

    def stage(self,result):
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