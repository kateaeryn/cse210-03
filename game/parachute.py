
class Parachute:
    """A class that controls the creation and adaptation of the user's parachute
    
    The Parachute class creates the visual for the jumper's parachute and removes pieces
    if wrong letters are guessed.

        Attributes: parachute(list): For storing the strings to create the parachute graphic
    """
    
    def __init__(self):
        """Constructs a new instance of Parachute
        
        args:self: an instance of parachute

        """
        self._parachute = ['   _______', '\n / _______ \ ', '\n \  _____  /', '\n  \       /', '\n   \     /', '\n    \   /', '\n      O', '\n     /|\ ', '\n     / \ \n', '\n ^^^^^^^^^^']

    def create_parachute(self):
        """A function to create a graphically pleasing parachute from a list of lines
        
            args: self: and instance of parachute

            returns: list formatted as a string
        """
        chute = ' '.join(self._parachute)
        return chute
       
    def update_chute(self, check):
        """A function that removes strings from the parachute in accoradance to wrong guesses
        
        args: self: an instance of parachute
              check: a boolean to test if the user's guess is part of the puzzle word

              returns: a list formatted as a string
        """
        if check == False:
            parachute = self._parachute
            parachute.pop(0)
            if len(parachute) < 5:
                parachute[0] = '      X'
            cut_chute = ' '.join(parachute)
            return cut_chute
        else:
            current_chute = ' '.join(self._parachute)
            return current_chute

    def strings_left(self):
        """A function that checks how many strings are left on the parachute
        
        args: self: an instance of parachute
        
        returns: true or false
        """
        if len(self._parachute) < 5:
            print("Sorry, your jumper died!!\n")
            return True
        else:
            return False