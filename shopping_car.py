#!/usr/bin/python3
# This program simulates a shopping cart where users can add items and calculate the total cost.
# Initialize an empty shopping cart

#item = input("what item would you like to buy?: ") # ask the user for the item they want to buy
#price = float(input("what is the price?: ")) # ask the user for the price of the item and convert it to a float
#quantity = int(input("How many would you like?: ")) # ask the user for the quantity of the item and convert it to an integer
#total = price * quantity # Calculate the total cost of the item based on the price and quantity
#print(total) # Print the total cost of the item to the console

#exircisw 2 shopping cart

item = input("what item would you like to buy?: ") # ask the user for the item they want to buy
price = float(input("waht is the price?: ")) # ask the user for the price of the item and convert it to a float
quantity = int(input("how many would you like?: ")) # ask the user for the quantity of the item and convert it to an integer
total = price * quantity # Calculate the total cost of the item based on the price and quantity

print(f"You have bought {quantity} x {item}/s") # Print a message to the user confirming their purchase and showing the total cost
print(f"You total is: ${total}") # Print the total cost of the item to the console