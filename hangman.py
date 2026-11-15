import urllib.request
import random
import re

def getSecretWord():
    baseWords = "https://raw.githubusercontent.com/lee-motley/python-learning/refs/heads/main/data/words.txt"
    response = urllib.request.urlopen(baseWords)
    data = response.read().decode("utf-8")
    words = data.split(",")
    # words = ["apple","banana","orange"]

    return random.choice(words)

def enterLetter(message):
    letter = input(message)

    if re.fullmatch("[a-zA-Z]", letter):
        return letter
    else:
        return enterLetter(message)



secretWord = getSecretWord()
secretWordLetters = list(secretWord)
secretWordAnswers = ["_"] * len(secretWord)
guess = ""
livesRemaining = 5
gameOver = False
guessedLetters = []

print(secretWordAnswers)


## number of guesses loop
while livesRemaining > 0 and not gameOver:

    guess = enterLetter("Guess a letter: ").lower()
    matches = 0

    # letters in word loop
    for index, letter in enumerate(secretWordLetters):
        if guess == letter.lower():
            secretWordAnswers[index] = guess
            matches = matches + 1

    if matches == 0 :
        guessedLetters.append(guess)
        
        livesRemaining = livesRemaining - 1
    
    print(secretWordAnswers)
    print(f"You have {livesRemaining} lives remaining!")

    print(f"You've already used {guessedLetters}")
    print()

    missingLetters = 0

    # for every letter in secret word answers, then do this
    for letter in secretWordAnswers:
        if letter == "_":
            missingLetters = missingLetters + 1

    if missingLetters == 0:
        print("You guessed it!")
        gameOver = True




    if livesRemaining == 0:
        print("The secret word was " + secretWord)


    # _ _ p _ _ = secretWordAnswers





# 1,a 2,p 3,p 4,l 5,e
# _ _ _ _ _