#!/usr/bin/python3
# This program simulates a shopping cart where users can add items and calculate the total cost.
# Initialize an empty shopping cart

item = input("what item would you like to buy?: ") # ask the user for the item they want to buy
price = float(input("what is the price?: ")) # ask the user for the price of the item and convert it to a float
quantity = int(input("How many would you like?: ")) # ask the user for the quantity of the item and convert it to an integer
total = price * quantity # Calculate the total cost of the item based on the price and quantity
print(total) # Print the total cost of the item to the console
