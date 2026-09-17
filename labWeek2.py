# Alvin Kim | Set A | ACIT 1515

# Creating variables and assigning values
# Create a variable named x and store an integer (whole number) inside it
x = 5
# Create a variable named y and store a string (any characters between single or double quotes) inside it
y = "Hello"
# Create a variable named z and store a float in it
z = 1.5


# Changing values stored in variables
# Change the value stored in the x variable to a new string
x = "Good morning"
# Change the value stored in the y variable to a new boolean
y = True
# Change the value store in the z variable to a different float
z = 2.5


# Getting input from a user
# Print the value the user entered from the previous section
user_input = input("What's your name? Enter here: ")
print(user_input)
# Print the (current) value of the variable x
print(x)
# Print the *type* (not the value itself) of the value stored in the y variable
print(type(y))

# Concatenation (joining two strings together)
# Create two variables, one containing the string CIT, and another containing the string 1515
course_name = "CIT"
course_number = 1515
# Using the two variables and a hard-coded letter, print the word ACIT1515 to the terminal
print(f"Congrats you're in A{course_name}{course_number}")
print(f'Assignment {5} created')