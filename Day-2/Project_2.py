# Welcome message
print("Welcome to the Tip Calculator!")

# Asking for total bill amount and converting it to a floating-point number
total_bill = float(input("Enter the total bill amount:"))

# Asking for the tip percentage as an integer
tip_percentage = int(input("Enter the tip percentage (10, 15, 20):"))

# Asking for the number of people as an integer
num_people = int(input("Enter the number of people:"))

# Calculating tip amount based on total bill and tip percentage
tip_amount = (total_bill * tip_percentage) / 100

# Calculating total amount by adding the bill and tip
total_amount = total_bill + tip_amount

# Calculating the amount each person should pay
amount_per_person = total_amount / num_people

# Displaying the result using an F-string
print(f"Each person should pay {amount_per_person}")
