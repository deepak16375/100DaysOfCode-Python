# Number Guessing Game

# Importing the randint function from the random module and the logo from the art module
from random import randint
from art import logo

# Setting the number of turns for easy and hard levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check the user's guess against the actual answer and return the remaining turns
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Function to set the difficulty level and return the initial number of turns
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Main game function
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Choosing a random number between 1 and 100.
    answer = randint(1, 100)

    turns = set_difficulty()  # Setting the difficulty level

    # Repeat the guessing functionality until the user guesses correctly or runs out of turns.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Check the user's guess, track the number of turns, and provide feedback.
        turns = check_answer(guess, answer, turns)
        
        # Handle game outcomes
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

# Start the game
game()
