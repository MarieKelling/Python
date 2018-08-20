# Assignment 07 - for loops

# Make sure you replace my name with yours
print("Assignment 07 - written by Marie Kelling")

# get user input
num = input("Enter a number: ")

while num.upper()!= "X":

    # check to make sure we have an integer, if not, quit
    if num.isdigit() != True:

        print("A number must be entered.")

        quit()

    # convert the imput string to an integer
    numInt = int(num)

    # prime numbers are greater than 1
    if numInt > 1:
        print("Check for factors.")
        print()

        # put code to check for primes here
        for i in range(2, numInt):
            if (numInt % i) == 0:
               print(numInt, "is NOT a prime number")
               print()
               break
        else:
            print(numInt, "IS a prime number")
            print()
    
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(numInt, " is NOT a prime number")
       print()

    # get user input
    num = input("Enter a number: ")

print("Goodbye!")
