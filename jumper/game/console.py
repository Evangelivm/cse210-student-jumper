import time
class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        text (string): The prompt to display on each line.
    """
     
    def introduction(self):
        """Gets text input from the user through the screen.

        Args: 
            self (Console): An instance of Console.

        Returns:
            string: The user's input as text.
        """
        print(f"█░░░█ █▀▀ █░░ ▄▀▀ ▄▀▀▄ ██▄██ █▀▀ . ▀█▀ ▄▀▀▄ . ▀█▀ █░█ █▀▀ . ▀▀█ █░░█ ██▄██ █▀▄ █▀▀ █▀▄\
\n█▄█▄█ █▀▀ █░░ █░░ █░░█ █░▀░█ █▀▀ . ░█░ █░░█ . ░█░ █▀█ █▀▀ . ▄░█ █░░█ █░▀░█ █▀░ █▀▀ █▀▄\
\n▀▀░▀▀ ▀▀▀ ▀▀▀ ░▀▀ ░▀▀░ ▀░░░▀ ▀▀▀ . ░▀░ ░▀▀░ . ░▀░ ▀░▀ ▀▀▀ . ░▀░ ░▀▀░ ▀░░░▀ ▀░░ ▀▀▀ ▀░▀\n")
        print("Loading")
        time.sleep(0.5)
        print(".") 
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        
    def write(self, text):
        """Displays the given text on the screen. 

        Args: 
            self (Console): An instance of Console.
            text (string): The text to display.
        """
        return input(text)