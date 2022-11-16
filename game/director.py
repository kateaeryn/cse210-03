from game.letters import Letters
from game.terminal_service import TerminalService
from game.parachute import Parachute

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not to keep playing.
        terminal_service: (class): For getting and displaying information on the terminal.
        parachute: (class): For drawing the parachute and removing strings
        letters: (class): For getting the word, and creating the playing board
        guess: (string): For storing user input
        jumper: (boolean): whether or not user input matches the guessing word
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._terminal_service = TerminalService()
        self._parachute = Parachute()
        self._letters = Letters()
        self._guess = ""
        self._jumper = True

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print("\nJumper is a guessing game. Choose one letter at a time to guess the word, but be careful, too many wrong guesses will drop your jumper faster!\n")
        self._terminal_service.write_text(self._letters.create_board())
        print()
        self._terminal_service.write_text(self._parachute.create_parachute())
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets the letter guess from the User.

        Args:
            self (Director): An instance of Director.
        """
        self._guess = self._terminal_service.read_letter("\nGuess a letter [a-z]:")
        print()
        self._letters.input(self._guess)
        self._jumper = self._letters.check_guess(self._guess)
            

    def _do_updates(self):
        """Compares letter guess to word.

        Args:
            self (Director): An instance of Director.
        """
    
        self._terminal_service.write_text(self._letters.update_board(self._guess))
        print()
        self._terminal_service.write_text(self._parachute.update_chute(self._jumper))        
        print()
      

    def _do_outputs(self):
        """Gives user another guess or cuts parachute string.

        Args:
            self (Director): An instance of Director.
        """
        if self._letters.check_full():
            self._is_playing = False
            
        if self._parachute.strings_left():
            self._terminal_service.write_text(f"Your word was: {self._letters._word}\n")
            self._is_playing = False
        