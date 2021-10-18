import random
class Library:
    """A code template for the library. The responsibility of this class 
    of objects is to have the information of every word used on the game 
    and the changes towards it.
    
    Stereotype:
        Service Provider

    Attributes:
        words (list): The list of words.
        spell_words (list): The list of every word but separated.
        number (number): The position of the word chosen at random.
        turn(number): Helps allowing once the random library.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Library): an instance of Library.
        """
        self.words = ["cup", "house", "mice","computer", "table", "chair"]
        self.spell_words = [['_','u','_'], ['_','_','u','_','_'], ['_','_','_','e'], ['_','o','_','p','_','_','e','_'],["_", "a", "_", "_", "e"],["c", "_", "a", "_", "_"]]
        self.number = 0
        self.turn = 0
    def choose_word(self):
        """Choose the word to use in the game. 
        Args:
            self (Library): an instance of Library.
        """
        if self.turn == 0:
            self.number = random.randint(0,5)
            self.turn = self.turn + 1
            return
        else:
            return
    def random_word(self):
        """Helps distributing the word to be visualized. 
        Args:
            self (Library): an instance of Library.
        """
        word = []
        for word in self.spell_words[self.number]:
            print(word,end=" ")
        return word
    def check(self,letter):
        """Check the user's answer with the chosen word. 
        Args:
            self (Library): an instance of Library.
            letter (Library): the input to be analyzed.
        """
        if letter in self.words[self.number]:
            radar = self.words[self.number].index(letter)
            self.spell_words[self.number][radar] = letter
            if '_' in self.spell_words[self.number]:
                return "correct"
            else:
                return "win"
        else:
            return "incorrect"
