
class Parachute:
    """A class that controls the creation and adaptability of the user's parachute
    
    args:

    
    """
    
    def __init__(self):
        """An instance of Parachute
        
        args:

        """
    def create_parachute(self):

        self.parachute = ["___\n"
            "/ ___ \\n"
            "\     /\n"
             "\   /\n"
               "O\n"
              "/|\\n"
              "/ \\n"
              "^^^^^^^^^^^" ]
       
    def cut_strings(self):

        self.parachute.pop()

    def strings_left(self):

        if self.parachute <= 5:
            response = "Sorry you died"
            return response
        else:
            return