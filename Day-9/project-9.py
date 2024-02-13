# Secret Auction Project

from replit import clear  # Importing clear function from replit library to clear console
from art import logo  # Importing logo from art library
print(logo)  # Printing the logo at the start of the program

bids = {}  # Dictionary to store bids
bidding_finished = False  # Flag to indicate whether bidding is finished or not

def find_highest_bidder(bidding_record):
    highest_bid = 0  # Variable to track the highest bid
    winner = ""  # Variable to store the winner's name
    for bidder in bidding_record:  # Loop through each bidder in the bidding record
        bid_amount = bidding_record[bidder]  # Retrieve bid amount for the current bidder
        if bid_amount > highest_bid:  # Check if the current bid is higher than the highest bid
            highest_bid = bid_amount  # If yes, update the highest bid
            winner = bidder  # Update the winner's name
    print(f"The winner is {winner} with a bid of ${highest_bid}")  # Print the winner and their bid amount

while not bidding_finished:  # Loop until bidding is finished
    name = input("What is your name?: ")  # Get bidder's name
    price = int(input("What is your bid?: $"))  # Get bid amount
    bids[name] = price  # Add the bid to the bids dictionary
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")  # Ask if there are more bidders
    if should_continue == "no":  # If no more bidders, finish bidding
        bidding_finished = True
        find_highest_bidder(bids)  # Find and announce the highest bidder
    elif should_continue == "yes":  # If there are more bidders, clear console for the next bid
        clear()
