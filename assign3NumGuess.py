# This is a guess the number game where python pulls in a random number
import random

# Number of attempts starts at 0 
numAttempts = 0

# Ask player to input name
print("Hello! What is your name?")
myName = input()

# Ask player to guess a number and sets the numbers between 1 and 20 also use python to generate random number 
number = random.randint(1, 20)
print("Well, " + myName + ", I am thinking of a number between 1 and 20.")

# Asks you to take a guess at most 3 times
while numAttempts < 3:
    print("Take a guess.") 
    # captures playes guess and converts it to an interger
    guess = input()
    guess = int(guess)

    numAttempts = numAttempts + 1

    # Create conditions for guesses
    if guess < number:
        print("Your guess is too low.") 

    if guess > number:
        print("Your guess is too high.")

    # Output if number is guessed correctly
    if guess == number:
        print("Good job, " + myName + "! You guessed my number in", numAttempts, "guesses.")
        # Stops asking for guesses
        break

# Output if number is not guessed in 3 attempts
if guess != number:
    print("Your three guesses are over. The number I was thinking of was", + number)
    
