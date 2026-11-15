
secretWord = "apple"
secretWordLetters = list(secretWord)
secretWordAnswers = ["_"] * len(secretWord)
guess = ""
livesRemaining = 5
gameOver = False


print(secretWordAnswers)


## number of guesses loop
while livesRemaining > 0 and not gameOver:
    print(f"You have {livesRemaining} lives")
    guess = input("Guess a letter: ")
    matches = 0

    # letters in word loop
    for index, letter in enumerate(secretWordLetters):
        if guess == letter :
            secretWordAnswers[index] = guess
            matches = matches + 1

    if matches == 0 :
        livesRemaining = livesRemaining - 1
    
    print(secretWordAnswers)


    missingLetters = 0

    # for every letter in secret word answers, then do this
    for letter in secretWordAnswers:
        if letter == "_":
            missingLetters = missingLetters + 1

    if missingLetters == 0:
        print("You guessed it!")
        gameOver = True



    # _ _ p _ _ = secretWordAnswers





# 1,a 2,p 3,p 4,l 5,e
# _ _ _ _ _