#function pig_latin
#take user input
#translate input to 'pig latin'
#return result as new string

def pig_latin():
#======================================================================================
    translation = input(str("Please enter a sentence you would like to be translated: "))
    output = ""
#======================================================================================
#translating to pig latin
    try:
        #translation.replace(' ','') removes space
        if translation.replace(' ','').isalpha(): # check input only letters
            i = translation.split() # split input into letters
#======================================================================================
            for letter in i:
                output += letter[1:] + letter[0] + "ay" + " "
                    #takes first letter from i variable - without code input Hello = Hay
                                                    #    -   with code input Hello = elloHay
                    #takes letter to end of word
                    #places space after each word
            return output
#======================================================================================
#if input isnt only letters
        else:
            raise ValueError
#======================================================================================
#execute input validation
    except ValueError:
        print("Ensure no numbers are input!")
#======================================================================================
print(pig_latin()) #Calls function
