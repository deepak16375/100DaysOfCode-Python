# Importing the random module for generating random elements
import random

# Lists of letters, numbers, and symbols for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcoming the user to the Password Generator
print("Welcome to the PyPassword Generator!")

# Asking the user for the number of letters, symbols, and numbers in the password
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level: Generating password using concatenation
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# Hard Level: Generating password using a list
password_list = []

# Adding random letters to the password list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Adding random symbols to the password list
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Adding random numbers to the password list
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Shuffling the password list to mix the elements
random.shuffle(password_list)

# Joining the elements of the password list to create the final password
password = ""
for char in password_list:
    password += char

# Displaying the generated password
print(f"Your password is: {password}")
