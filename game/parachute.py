
class Parachute:
    """A class that controls the creation and adaptability of the user's parachute
    
    args:

    
    """
    
    def __init__(self):
        """An instance of Parachute
        
        args:

        """
        self.parachute = ['   _______', '\n / _______ \ ', '\n \  _____  /', '\n  \       /', '\n   \     /', '\n    \   /', '\n      O', '\n     /|\ ', '\n     / \ \n', '\n ^^^^^^^^^^']

    def create_parachute(self):
        
        chute = ' '.join(self.parachute)
        return chute
       
    def update_chute(self, check):
        
        if check == False:
            parachute = self.parachute
            parachute.pop(0)
            if len(parachute) < 5:
                parachute[0] = '      X'
            cut_chute = ' '.join(parachute)
            return cut_chute
        else:
            current_chute = ' '.join(self.parachute)
            return current_chute

    def strings_left(self):

        if len(self.parachute) < 5:
            print("Sorry, your jumper died!!\n")
            return True
        else:
            return False