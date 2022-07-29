#function no_three_sum
#take three integer values from user as arguments
#return their sum
#if value is multiple of three value = 0
#except multiples between 20-29
#separate function fix_three(n)
#takes int value
#returns value true to rule

def no_three_sum(a, b, c):
    num = (a, b, c) #assign argument to variable 'num'
    total = 0 # store total count
#===================================================
    for int in num: #int - integer
        if fix_three(int):
            total += int # add every int in num(a,b,c)
    return 'The total sum =' ,total
#===================================================
def fix_three(n):
    if n % 3 != 0: # n value (a,b, or c) divisible by 3 is not equal to 0
        return n 
    if 20 < n < 29: # n value between 20-29 
        return n
#===================================================
a = int(input("Enter a positive number: "))
b = int(input("Enter a positive number: "))
c = int(input("Enter a positive number: "))
#===================================================
#input validation
try:
    if a < 0:
        raise ValueError
    elif b < 0:
        raise ValueError
    elif c < 0:
        raise ValueError
#ensures only positive integers are entered
#===================================================
except ValueError:
    print("Please enter a positive number!")
    quit()
#===================================================
#call function
print(no_three_sum(a, b, c,))


