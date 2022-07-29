.#Defining the function (str_abba)
#Gets two inputs from user
#Checks inputs only contain letters
#Returns value in format A+B+B+A

def str_abba():
        A = str(input("Please enter a string: "))
        B = str(input("Please enter another string: ")) 

#=======================================================================
#input validation
        try:
           if A.isalpha(): # checks if input contains letters
                   if B.isalpha(): 
                           return(A + B + B + A) # returns values
           else:
                raise ValueError # raise error from inputs

#=======================================================================

        except ValueError:
                print("Ensure only letters are input!")
                quit() # quits the program

print(str_abba()) # Call function      
    
	
	
