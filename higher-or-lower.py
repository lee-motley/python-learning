import random

secretNumber = random.randint(1, 100)
numberOfGuesses = 5
guessNumber = 1


# while guess number is less than number of guesses, guess again and again
                      
while guessNumber <= numberOfGuesses:

    guessNumber = guessNumber + 1
    guess = int(input("What is your guess? "))

    # check if guess equals the secret number, say "Correct" or "Wrong answer!"

    if guess == secretNumber:
        print("Correct!")
        break
    else:
        # check if the guess is higher or lower than secret number

        if guess > secretNumber:
            print("Try lower")
        else:
            print("Try higher")

print("The answer was " + str(secretNumber))