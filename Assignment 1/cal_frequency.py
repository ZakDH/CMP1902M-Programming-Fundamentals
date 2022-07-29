#function cal_frequency
#calculate frequency of only letter occurrence
#sort letters into order of frequency displaying occurrence

def cal_frequency():
#========================================================================
    Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l",
                "m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # sorts alphabet into a list
    sentence = input("Please enter a sentence: ").lower() # ensures all characters are lowercase
    sentence = sentence.replace(" ","") # removes spaces
    count = {}
#========================================================================
    try:
        for letter in sentence:
            if (letter in Alphabet):
                if letter in count.keys(): # if letter is keyword in count + 1 each time
                    count[letter]+=1
                else:
                    count[letter]=1 #if letter not keyword in count = 1
            else:
                raise ValueError # if letter not in alphabet raise error
#========================================================================
        print(sorted(count.items(),key = lambda x:x[1],reverse=True))
        #prints the letter & frequency in decending order
        #'sorted' allows the 'count.items' to be sorted i 'reverse' order
        #reverse order being decending order
        #x - relates to letter in count dictionary
        #x[1] relates to the letters frequency count
        #lambda takes any argument 'letter + frequency'
#========================================================================
    except ValueError: # executes validation error
        print("You have entered an incorrect character!")
#calls function
cal_frequency()
