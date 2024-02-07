# Importing the random module to make the computer's choice random
import random

# ASCII art for Rock, Paper, and Scissors options
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of ASCII images for Rock, Paper, and Scissors
game_images = [rock, paper, scissors]

# Getting user input for their choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
print(game_images[user_choice])

# Generating a random choice for the computer
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Checking the game logic and determining the winner
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")