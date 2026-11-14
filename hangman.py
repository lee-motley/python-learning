
secretWord = "apple"
secretWordLetters = list(secretWord)
secretWordAnswers = ["_"] * len(secretWord)
guess = ""
livesRemaining = 5


print(secretWordAnswers)


## number of guesses loop
while livesRemaining > 0:
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


# 1,a 2,p 3,p 4,l 5,e
# _ _ _ _ _