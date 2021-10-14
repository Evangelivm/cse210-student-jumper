import random

class Hider:
    """A code template for a the seeker who looks for the hider. The 
    responsibility of this class of objects is to move from location to 
    location in pursuit of the Hider.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Seeker (1-1000).
        distance (list): The distance travelled with each move.
    """

    def __init__(self):
        self.location = 0
        self.distance = [0]
    def get_hint(self):
        if round(abs(self.distance[-1])) == self.distance[0]:
            return "(;.;) You found me!"
        if abs(self.distance[-2]-self.distance[-1]) < 200:
            return "(>.<) Getting warmer!"
        elif abs(self.distance[-2]-self.distance[-1]) > 200:
            return "(^.^) Getting colder!"
    def watch(self,location):
        self.location = float(location)
        self.distance.append(location)
        return self.location