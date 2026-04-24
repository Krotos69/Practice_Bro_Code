#!/usr/bin/python3

# input () function taht prompts the user to enter data
# Returns the entered data as a string

#input() # prompts the user to enter data and returns the entered data as a string
name = input("What is your name?") # prompts the user to enter their name and returns the entered name as a string
age  = input("How old are you?:") # prompts the user to enter their age and returns the entered age as a string

print(f"Hello {name}!") # f-string (formatted string literal) (allows you to embed expressions inside string literals, using curly braces {})
print(f"You are {age} years old") # f-string (formatted string literal) (allows you to embed expressions inside string literals, using curly braces {})

