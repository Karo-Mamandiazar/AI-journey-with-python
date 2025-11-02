print('___While loop guessing game___')

# Player 1 sets a secret number between 1 and 100
answer = int(input("player 1: Please insert the number (1 - 100): "))

# Initialize game state
is_correct = False  # Tracks whether Player 2 guessed correctly
try_count = 0       # Counts the number of guesses made

# Player 2 has up to 10 attempts to guess the correct number
while try_count < 10 and is_correct == False:
    guess = int(input("player 2: Please guess a number: "))  # Player 2 makes a guess

    if guess == answer:
        print("player 2: you won!")  # Correct guess
        is_correct = True            # Update game state
    elif guess > answer:
        print("Your guess is greater than the answer!")  # Too high
        try_count += 1
    else:
        print("Your guess is less than the answer!")     # Too low
        try_count += 1

# If Player 2 fails to guess in 10 tries, they lose
if is_correct == False:
    print("player 2: You Lost!")