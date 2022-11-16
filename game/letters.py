import random

class Letters:
    """A class that handles the user's guess and the words to be guessed
    
    The responsibility of Letters is to choose a word to be guessed, compare the user's guess against the word,
    track which letters the user has guessed, update the puzzle board with correct letters and confirm the win
    when the word is guessed correctly.

    Attributes:
        word_pool: A list of words to guess
        word(string): a randomly chosen word from the word pool
        board(list): a list of underscores to show the user how many letters they are guessing
        dict(list): a list to store the letters the user has guessed
    
    """
    def __init__(self):
        """Creates a new Letters
        
        args:self: an instance of letters
        
        """
        word_pool = ["chess", "heart", "light", "adieu", "broke", "horse", "spirit", "panther", "dog", "cable", "weather", "piano", "water", "video", "parachute", "shiny", "python", "module", "terminate", "maple", "snarl", "wheel"]
        self._word = random.choice(word_pool)
        self._board = ['_'] * len(self._word)
        self._dict = []
      
    def create_board(self):
        """A function to create the letter board
        
        args: self: an instance of letters

        returns: string of underscores as a puzzle board
        """
        board = self._board
        full_board = ' '.join(board)
        return full_board
        
    def input(self, guess):
        """A function to store the user input
        
        args: self: an instance of Letters
              guess: a string of the user's guess

              returns: list of user's guesses
        
        """
        if guess not in self._dict:
            self._dict.append(guess)
        else:
            print(f"\nYou already guessed {guess}, choose another")
        return self._dict


    def check_guess(self, guess):
        """A function to check the users guess against the puzzle word
        
        args:self: an instance of Letters
             guess: a string of the user's guess

             returns: true or false
        """
        word = self._word
        if guess in word:
            return True
        else:
            return False
 
    def update_board(self, guess):
        """A function to update the puzzle board with correctly guessed letters
        
        args: self: an instance of Letters
                guess: a string containing the user's current guess
        
        returns: string of the puzzle board updated with correct guesses, or without changes due to incorrect guesses
        """
        board = self._board
        word = self._word
        if guess in word:            
            for i in range(len(word)):
                if word[i] == guess:
                    board[i] = guess
                    full_board = ' '.join(board)  
            return full_board        
        else:       
            board = ' '.join(self._board)
            return board
        
    def check_full(self):
        """A function to check for completion of the puzzle word
        
        args: self: an instance of Letters
        
        returns: true or false
        """
        word = []
        board = self._board
        word[:0] = self._word
        if board == word:
            print("Congratulations, You Win!")
            return True
        else: 
            return False

               
        

    
       
        