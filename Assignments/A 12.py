#A 12

print("Program Written by Marie Kelling")

#Implement 2 separate print statements on the same line
print("Marie", end = " ")
print("Kelling")

# This is a guess the number game
import random

print ('Hello, what is your name?')
name = input()

print ('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)
print ('secretNumber = ' + str(secretNumber))

#Implement array to keep track of user guesses:
userGuesses = []

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    userGuesses.append(guess)
    
    if guess < secretNumber:    
        print ('Your guess is too low.')
        print('Already Guessed: ', userGuesses)
    elif guess > secretNumber:
        print ('Your guess is too high.')
        print('Already Guessed: ', userGuesses)
    else:
        break # this indicates a correct guess
    
if guess == secretNumber:
    print('Good job, ' + name + '! Your guess the number in ' + str(guessesTaken) + ' guesses!') 
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


