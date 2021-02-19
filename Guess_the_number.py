import random
randNum = random.randint(0, 100)

userGuess = None
Guesses = 0
while(userGuess != randNum):
    userGuess = int(input("Please the number you Guessed : "))
    Guesses += 1
    if userGuess > randNum:
        print("The number you guessed is larger than the number generated")
    elif userGuess < randNum:
        print("The number you guessed is smaller than the number generated")
    else:
        print("Awesome ! you guessed it correctly")

if Guesses == 1:
    print(f"You gussed it right in {Guesses} guess")
else:
    print(f"You gussed it right in {Guesses} guesses")

# print(randNum) --> This can be used to print the random number generated by random module

# Now we will make a file to store the highscores of the game

with open("highscore.txt") as f:
    highscore = int(f.read())

if (Guesses<highscore):
    print("Congratulations! You have made a new high score")
    with open("highscore.txt", 'w') as f:
        f.write(str(Guesses))

    