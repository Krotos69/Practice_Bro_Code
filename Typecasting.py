#!/usr/bin/python3
# This is a simple Python script that demonstrates typecasting in Python.
# Typecasting = converting the data type of a value to another data type
# str() = converts a value to a string
# int() = converts a value to an integer
# float() = converts a value to a float
# bool() = converts a value to a boolean


name = "Bro code" # variable assignment (stores the value "Bro code" in the variable name)
age = 35 # variable assignment (stores the value 35 in the variable age)
gpa = 3.2 # variable assignment (stores the value 3.2 in the variable gpa)
is_student = True # variable assignment (stores the value True in the variable is_student)

#type() # type() function (returns the data type of a value)

#print(type(name)) # prints <class 'str'> (the data type of the variable name is str)
#print(type(age)) # prints <class 'int'> (the data type of the variable age is int)
#print(type(gpa)) # prints <class 'float'> (the data type of the variable gpa is float)
#print(type(is_student)) # prints <class 'bool'> (the data type of the variable is_student is bool)

# converting the data type of a value to another data type

gpa = str(gpa) # converts the value of gpa from a float to an integer (3.2 becomes 3)
print(type(gpa)) # prints 3 (the value of gpa is now an integer)

name = int(name) # converts the value of name from a string to an integer (Bro code becomes 0)
print(type(name)) # prints 0 (the value of name is now an integer)