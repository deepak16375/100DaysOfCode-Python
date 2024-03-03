# Import necessary modules
from turtle import Turtle, Screen
import random

# Set up the race
is_race_on = False  # Flag to control whether the race is on or off
screen = Screen()    # Create a screen for the turtles to race on
screen.setup(width=500, height=400)  # Set the size of the screen
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Enter a color: ")  # Ask user to bet on a turtle's color
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of turtle colors
y_positions = [-70, -40, -10, 20, 50, 80]  # Starting y-positions for each turtle
all_turtles = []  # List to store turtle objects

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle object
    new_turtle.penup()  # Lift the pen to move without drawing
    new_turtle.color(colors[turtle_index])  # Assign a color to the turtle
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Set the starting position
    all_turtles.append(new_turtle)  # Add the turtle to the list

# Check if the user has made a bet
if user_bet:
    is_race_on = True  # If the user made a bet, start the race

# Start the race
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False  # If a turtle reaches the finish line, stop the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount
        rand_distance = random.randint(0, 10)  # Generate a random distance for the turtle to move
        turtle.forward(rand_distance)  # Move the turtle forward by the random distance

# Close the turtle graphics window when clicked
screen.exitonclick()
