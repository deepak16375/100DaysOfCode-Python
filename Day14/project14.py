# Import necessary modules for the game.
import random  # For generating random accounts
from replit import clear  # For clearing the console screen
from art import logo, vs  # For displaying game logos
from game_data import data  # For accessing the list of Instagram accounts

# Function to get data from a random account.
def get_random_account():
    """Get data from a random account."""
    return random.choice(data)

# Function to format account data into a printable format.
def format_data(account):
    """Format account into printable format: name, description, and country."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# Function to check if the user's guess is correct.
def check_answer(guess, a_followers, b_followers):
    """Check followers against the user's guess and return True if they got it right, False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Function to run the Higher-Lower game.
def game():
    """Run the Higher-Lower game."""
    print(logo)  # Display the game logo
    score = 0  # Initialize the player's score
    game_should_continue = True  # Flag to control game continuation
    account_a = get_random_account()  # Get the first random account
    account_b = get_random_account()  # Get the second random account

    # Main game loop
    while game_should_continue:
        account_a = account_b  # Move the second account to the first position
        account_b = get_random_account()  # Get a new random account for the second position

        # Ensure that the accounts are not the same
        while account_a == account_b:
            account_b = get_random_account()

        # Display the accounts for comparison
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Ask the user for their guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)  # Check if the guess is correct

        clear()  # Clear the console screen
        print(logo)  # Display the game logo again

        # Provide feedback to the user based on their guess
        if is_correct:
            score += 1  # Increment the score for a correct guess
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False  # End the game if the guess is incorrect
            print(f"Sorry, that's wrong. Final score: {score}")

# Run the game.
game()
