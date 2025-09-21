def classify_number(number):
    """
    Classifies a number as Positive, Negative, or Zero.
    """
    if number > 0:
        return "Positive"  # Returns a positive number
    elif number < 0:
        return "Negative"  # Returns a negative number
    else:
        return "Zero"  # Returns a zero

def get_valid_number():
    """
    Prompts the user for a valid integer using a while loop.
    """
    while True:  # Use a while loop to repeatedly prompt the user.
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Example:
number_to_classify = get_valid_number()
classification = classify_number(number_to_classify)
print(f"The number is: {classification}")