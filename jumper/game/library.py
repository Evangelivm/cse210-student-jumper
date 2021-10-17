import random
class Library:
    """A code template for the library. The responsibility of this class 
    of objects is to have the information of every word used on the game 
    and the changes towards it.
    
    Stereotype:
        

    Attributes:
        words (list): The list of words.
        spell_words (list): The list of every word but separated.
        number (number): The position of the word chosen at random.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Library): an instance of Library.
        """
        self.words = ["cup", "house", "mice","computer"]
        self.spell_words = [['_','u','_'], ['_','_','u','_','_'], ['_','_','_','e'], ['_','o','_','p','_','_','e','_']]
        self.number = 0
        self.turn = 0
    def choose_word(self):
        if self.turn == 0:
            self.number = random.randint(0,3)
            self.turn = self.turn + 1
            return
        else:
            return
    def random_word(self):
        word = []
        for word in self.spell_words[self.number]:
            print(word,end=" ")
        return word
    def check(self,letter):
        if letter in self.words[self.number]:
            radar = self.words[self.number].index(letter)
            self.spell_words[self.number][radar] = letter
            if '_' in self.spell_words[self.number]:
                return "correct"
            else:
                return "win"
        else:
            return "incorrect"
