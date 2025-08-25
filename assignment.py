# Assignment Question: Write a python code snippet that demonstrates the use of variables, constants and the print function:

# -----------------------------------------------------------
# Section 1: Variables
#  are used to store data that can change during the program's execution.
# In Python, you don't need to declare the variable type.
# The variable is created the moment you first assign a value to it.

# Assign a new string value to a variable named 'user_name'.
user_name = "Josh"
# Assign a new float value to a variable named 'user_height'.
user_height = 1.25
# Assign a new float value to a variable named 'pi_value' with more precision.
# The value of a variable can be changed later in the code.
pi_value = 3.14159

# -----------------------------------------------------------
# Section 2: Constants
# are usually defined on a module level and written in all capital letters with underscores separating words.

# A constant for the number of days in a week
DAYS_IN_WEEK = 7

# A constant tuple for the days of the week
WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Constants for each day of the week
MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# -----------------------------------------------------------
# Section 3: The print() Function
# The print() function is used to output data to the standard output device (the screen).
# It can display strings, numbers, and the values of variables and constants.

# Print a simple string.

print("")
print("--- User Information ---")

# Print the value of the variables.
# You can concatenate strings and variables using the '+' operator,
# but it's often better to use an f-string (formatted string literal) for readability.
# An f-string is created by placing an 'f' before the opening quotation mark.
print(f"User's name: {user_name}")
print(f"User's height: {user_height} meters")

# Print the value of the constants.
print(WEEKDAYS[0])
print(WEEKDAYS[1])
print(WEEKDAYS[2])
print(WEEKDAYS[3])
print(WEEKDAYS[5])

print(f"The first day of the week is {WEEKDAYS[0]}")