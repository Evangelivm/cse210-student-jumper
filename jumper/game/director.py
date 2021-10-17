from game.console import Console
from game.result import Result
from game.library import Library

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        seeker (Seeker): An instance of the class of objects known as Seeker.
        hider (Hider): An instance of the class of objects known as Hider.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.result = Result()
        self.keep_playing = True
        self.library = Library()
        self.first = 0

        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()


    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        if self.first == 0:
            self.console.introduction()
            self.first = self.first + 1
            self.result.stage("correct")
            self.library.choose_word()
            self.library.random_word()
            word_question = self.console.write("\nGuess a letter [a-z]: ")
            check_status = self.library.check(word_question)
            self.result.stage(check_status)
        else:
            self.library.choose_word()
            self.library.random_word()
            word_question = self.console.write("\nGuess a letter [a-z]: ")
            check_status = self.library.check(word_question)
            self.result.stage(check_status)
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the hider watches the seeker.

        Args:
            self (Director): An instance of Director.
        """
        if (self.result.turn_number == 4) or (self.result.close == True):
            self.keep_playing = False
        else:
            self.keep_playing = True