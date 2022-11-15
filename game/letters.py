import random
import functools

class Letters:
    """A class that handles the user's guess and the words to be guessed
    
    args:
        word_pool: A list of words to guess

    
    """
    def __init__(self):
        """An instance of Letters
        
        args:
        
        """
        word_pool = ["chess", "heart", "light", "adieu", "broke", "horse", "spirit", "panther", "dog", "cable", "weather"]
        self.word = random.choice(word_pool)
        self.board = ['_'] * len(self.word)
        self.dict = []
      
    def create_board(self):
        """A function to create the letter board
        
        args: self: an instance of letters
        """
        board = ["_", "_", "_", "_", "_"]
        full_board = ' '.join(board)
        return full_board
        
    def input(self, guess):
        
        if guess not in self.dict:
            self.dict.append(guess)
        else:
            print(f"\nYou already guessed {guess}, choose another")
        return self.dict


    def check_guess(self, guess):
        """A function to check the users guess
        
        args:
        """
        board = self.board
        word = self.word
        
        if guess in word:            
            for i in range(len(word)):
                if word[i] == guess:
                    board[i] = guess
                    full_board = ' '.join(board)  
            return full_board        
        else:       
            board = ' '.join(self.board)
            return board
        
    def check_full(self):

        word = []
        board = self.board
        word[:0] = self.word
       
        if board == word:
            print("You win!")
            return True
        else: 
            return False

               
        

    
       
        