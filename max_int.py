# Design an algorithm that finds the maximum positive integer input by a user.  
# The user repeatedly inputs numbers until a negative value is entered.


# The program runs while user puts in positive numbers, 
# When the user puts in a negative number the loop stops
# The program then prints out the highest number the user entered

num_int = 0
max_int = 0


while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int: 
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line




