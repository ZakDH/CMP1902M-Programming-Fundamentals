#function compare_ages
#ask for users age
#respond with
    #being the same age
    #being older or younger
#display age difference

def compare_ages():   
    myAge = 18
    print("My age is",myAge)
    userAge = int(input("Please enter your age: "))
#==================================================================
#input validation
    try:
        if userAge < 0: # age less than 0 raise error
            raise ValueError 
#==================================================================
#greater/less than 18
        if userAge > myAge: # userage greater than 18
            diff = userAge - myAge
            print("You are older than me by", diff, "year(s).")
        elif userAge < myAge: # userage less than 18
            diff = myAge - userAge
            print("You are younger than me by", diff, "year(s).")
        else: # user age same age
            print("You are the same age as me.")
#==================================================================
#validation error statement
    except ValueError:
        print("Please enter a positive integer!")
#==================================================================
compare_ages() # calls function
 
