33
#using random.randint library
#function guessing_game
#count num. of guesses
#advise whether num is too big/small
#alert user when guess is right

from random import randint

def guessing_game():	
#=======================================================================
#'try' to find error in input
  try:
        guesses = 1
        num = randint(1,100) # assign num random number between 1-100
        guess = int(input("Please enter a number between 1-100: "))
#=======================================================================
 # while guess is not equal to num
        while guess != num:
                if guess <= 0: # guess less than or equals 0 
                    raise ValueError # input validation

                elif guess > 100: # guess greater than 100 
                    raise ValueError    

                elif guess < num: # guess less than number
                    print("That's not right", guess, "is too small")
                    guess = int(input("Guess again please."))
                    guesses = guesses + 1 # guess adds 1 each incorrect guess

                elif guess > num: #guess larger than number
                    print("That's not right", guess, "is too big")
                    guess = int(input("Guess again please."))
                    guesses = guesses + 1
#=======================================================================
#if user guess is correct
        else:
                print("That's right! You took", guesses,"guess(es)")
#=======================================================================
#invaid user input
  except ValueError:
        print("INVALID NUMBER! Please enter a number between 1 and 100!")

#call function
guessing_game()